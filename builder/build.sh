#!/usr/bin/env bash
# build.sh - Compiles e-Patra Production Build on macOS/Linux.
set -euo pipefail

# Change to root directory of project relative to script location
cd "$(dirname "$0")/.."

echo "==================================================="
echo "       Compiling Sanchaya Production Build      "
echo "==================================================="
echo

# Helper function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 1. Resolve Maven command
MAVEN_CMD="mvn"
if ! command_exists mvn; then
    # Check if local maven wrapper wrapper jar/script exists
    if [ -f "backend/mvnw" ]; then
        MAVEN_CMD="./mvnw"
    else
        echo "[ERROR] Maven ('mvn') is not found in your PATH."
        echo "Please install Maven or ensure it is available in your PATH."
        exit 1
    fi
fi

# 2. Build backend
echo "[1/2] Packaging Backend Service (Spring Boot Jar)..."
MAVEN_OPTS="-XX:+UseSerialGC -Xmx128m -XX:MaxMetaspaceSize=64m" $MAVEN_CMD -f backend/pom.xml clean package -DskipTests

echo
echo "[2/2] Compiling Frontend Client (Tauri Standalone App)..."
echo "Bumping build version..."
python3 builder/increment_version.py patch || python builder/increment_version.py patch

echo "Copying help documentation..."
mkdir -p frontend/public/help
cp -R docs/help/* frontend/public/help/

cd frontend
echo "Cleaning Rust compile cache to prevent file locking issues..."
cd src-tauri
cargo clean
cd ..

# Limit parallel compilation jobs to prevent compiler OOM errors
export CARGO_BUILD_JOBS=1
# Increase compiler thread stack size to avoid crashes
export RUST_MIN_STACK=268435456
# Limit Node.js memory footprint to avoid paging file commitment errors
export NODE_OPTIONS=--max-old-space-size=256

# Build production Tauri app
npm run tauri build

cd ..
echo
echo "==================================================="
echo "     [SUCCESS] Production build completed!         "
echo "==================================================="
echo "Backend Jar: backend/target/sanchaya-1.0-SNAPSHOT.jar"
echo "Frontend Standalone App: frontend/src-tauri/target/release/"
echo
