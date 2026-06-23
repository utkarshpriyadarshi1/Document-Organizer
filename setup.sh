#!/usr/bin/env bash
# setup.sh - Onboarding setup script for macOS/Linux systems.
set -euo pipefail

# Terminal colors
GREEN='\033[0;32m'
NC='\033[0m' # No Color
RED='\033[0;31m'
YELLOW='\033[1;33m'

echo "==================================================="
echo "          Document Organizer Developer Onboarding Setup       "
echo "==================================================="
echo

# Helper function to check command existence
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

echo "Checking system prerequisites..."
# Check Node.js
if command_exists node; then
    echo -e "  - Node.js: ${GREEN}Available${NC} ($(node -v))"
else
    echo -e "  - ${RED}[ERROR] Node.js is not found in your PATH.${NC} Please install Node.js 18+."
    exit 1
fi

# Check NPM
if command_exists npm; then
    echo -e "  - NPM: ${GREEN}Available${NC} ($(npm -v))"
else
    echo -e "  - ${RED}[ERROR] NPM is not found in your PATH.${NC}"
    exit 1
fi

# Check Java
if command_exists java; then
    echo -e "  - Java: ${GREEN}Available${NC}"
else
    echo -e "  - ${RED}[ERROR] Java JDK is not found in your PATH.${NC} Please install JDK 17+."
    exit 1
fi

# Check Maven
MAVEN_CMD="mvn"
if command_exists mvn; then
    echo -e "  - Maven: ${GREEN}Available${NC}"
else
    if [ -f "backend/mvnw" ]; then
        MAVEN_CMD="./mvnw"
        echo -e "  - Maven: ${YELLOW}Using local Maven wrapper (mvnw)${NC}"
    else
        echo -e "  - ${YELLOW}[WARNING] Maven not found. Local backend compiler will use wrapper if present.${NC}"
    fi
fi

# Check Rust/Cargo
if command_exists cargo; then
    echo -e "  - Rust (Cargo): ${GREEN}Available${NC}"
else
    echo -e "  - ${YELLOW}[WARNING] Rust/Cargo not found. Standard desktop wraps (Tauri compilation) will fail,${NC}"
    echo "              but mock sandbox UI development will still function."
fi

echo
echo "[1/2] Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo
echo "[2/2] Compiling backend and verifying codebase..."
if command_exists mvn; then
    mvn -f backend/pom.xml clean compile
else
    if [ -f "backend/mvnw" ]; then
        chmod +x backend/mvnw
        ./backend/mvnw -f backend/pom.xml clean compile
    else
        echo -e "${RED}[ERROR] No Maven or Maven wrapper found to verify backend!${NC}"
        exit 1
    fi
fi

echo
echo -e "${GREEN}===================================================${NC}"
echo -e "${GREEN}     [SUCCESS] Developer Environment is Ready!      ${NC}"
echo -e "${GREEN}===================================================${NC}"
echo "To launch the concurrent development servers:"
echo -e "  ${GREEN}chmod +x dev.sh && ./dev.sh${NC}"
echo "==================================================="
echo
