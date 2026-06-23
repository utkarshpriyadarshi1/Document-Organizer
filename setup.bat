@echo off
setlocal enabledelayedexpansion

echo ===================================================
echo           Document Organizer Developer Onboarding Setup       
echo ===================================================
echo.

:: 1. Verify Prerequisites
echo Checking system prerequisites...

where node >nul 2>nul
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('node -v') do set NODE_VER=%%i
    echo   - Node.js: Available (!NODE_VER!)
) else (
    echo   - [ERROR] Node.js is not found in your PATH. Please install Node.js 18+.
    exit /b 1
)

where npm >nul 2>nul
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('npm -v') do set NPM_VER=%%i
    echo   - NPM: Available (!NPM_VER!)
) else (
    echo   - [ERROR] NPM is not found in your PATH.
    exit /b 1
)

where java >nul 2>nul
if %errorlevel% equ 0 (
    echo   - Java: Available
) else (
    echo   - [ERROR] Java JDK is not found in your PATH. Please install JDK 17+.
    exit /b 1
)

where mvn >nul 2>nul
if %errorlevel% equ 0 (
    echo   - Maven: Available
) else (
    :: Check if user-local wrapper exists
    if exist "%USERPROFILE%\.m2\wrapper\dists\apache-maven-3.9.6-bin\3311e1d4\apache-maven-3.9.6\bin\mvn.cmd" (
        echo   - Maven: Available (User profile)
    ) else (
        echo   - [WARNING] Maven is not found. Maven wrapper inside backend/ will be used.
    )
)

where cargo >nul 2>nul
if %errorlevel% equ 0 (
    echo   - Rust (Cargo): Available
) else (
    echo   - [WARNING] Rust/Cargo not found. Desktop compilation (Tauri) will fail, 
    echo               but mock sandbox web frontend development will still work.
)

echo.
:: 2. Setup self-signed developer certificate
echo [1/3] Configuring code-signing certificate...
powershell -ExecutionPolicy Bypass -File builder\setup-cert.ps1
if %errorlevel% neq 0 (
    echo [WARNING] Certificate setup failed or skipped. You can import certs/developer.pfx manually.
)

echo.
:: 3. Install frontend dependencies
echo [2/3] Installing frontend dependencies...
cd frontend
call npm install
if %errorlevel% neq 0 (
    echo [ERROR] Frontend installation failed!
    cd ..
    exit /b %errorlevel%
)
cd ..

echo.
:: 4. Compile backend to verify
echo [3/3] Compiling backend and verifying codebase...
call mvn -f backend/pom.xml clean compile
if %errorlevel% neq 0 (
    if exist "backend\mvnw.cmd" (
        echo Retrying compiling using local Maven wrapper...
        call backend\mvnw.cmd -f backend/pom.xml clean compile
    )
    if %errorlevel% neq 0 (
        echo [ERROR] Backend compilation failed! Please verify Java and Maven installation.
        exit /b %errorlevel%
    )
)

echo.
echo ===================================================
echo     [SUCCESS] Developer Environment is Ready!      
echo ===================================================
echo To launch the concurrent development servers:
echo   Windows: .\dev.bat
echo   macOS/Linux: ./dev.sh
echo ===================================================
echo.
pause
exit /b 0
