@echo off
setlocal enabledelayedexpansion

:: Change to root directory of project relative to script location
cd /d "%~dp0.."

echo ===================================================
echo        Compiling Document Organizer Production Build       
echo ===================================================
echo.

call :find_maven
if %errorlevel% neq 0 (
    echo.
    pause
    exit /b %errorlevel%
)

echo [1/2] Packaging Backend Service (Spring Boot Jar)...
set MAVEN_OPTS=-XX:+UseSerialGC -Xmx128m -XX:MaxMetaspaceSize=64m
call %MAVEN_CMD% -f backend/pom.xml clean package -DskipTests
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Backend packaging failed!
    pause
    exit /b %errorlevel%
)

echo.
echo [2/2] Compiling Frontend Client (Tauri Standalone App)...
echo Bumping build version...
call python builder\increment_version.py patch
echo Copying help documentation...
xcopy /Y /S /I docs\help frontend\public\help
cd frontend
echo Cleaning Rust compile cache to prevent file locking issues...
cd src-tauri
cargo clean
cd ..
:: Limit parallel compilation jobs to prevent compiler OOM errors
set CARGO_BUILD_JOBS=1
:: Increase compiler thread stack size to avoid crashes
set RUST_MIN_STACK=268435456
:: Limit Node.js memory footprint to avoid paging file commitment errors
set NODE_OPTIONS=--max-old-space-size=256
:: Build production Tauri app
call npm run tauri build
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Tauri desktop build failed!
    cd ..
    pause
    exit /b %errorlevel%
)
cd ..

echo.
echo ===================================================
echo      [SUCCESS] Production build completed!         
echo ===================================================
echo Backend Jar: backend/target/document-organizer-1.0-SNAPSHOT.jar
echo Frontend Standalone App: frontend/src-tauri/target/release/
echo.
pause
exit /b 0

:: Helper subroutine to resolve Maven executable
:find_maven
set MAVEN_CMD=mvn
where mvn >nul 2>nul
if %errorlevel% neq 0 (
    if exist "%USERPROFILE%\.m2\wrapper\dists\apache-maven-3.9.6-bin\3311e1d4\apache-maven-3.9.6\bin\mvn.cmd" (
        set MAVEN_CMD="%USERPROFILE%\.m2\wrapper\dists\apache-maven-3.9.6-bin\3311e1d4\apache-maven-3.9.6\bin\mvn.cmd"
    ) else (
        echo [ERROR] Maven was not found in your PATH or local user directory.
        echo Please ensure Java 17+ and Maven are installed.
        exit /b 1
    )
)
exit /b 0
