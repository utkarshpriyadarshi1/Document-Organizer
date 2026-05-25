# e-Dastavej Document Management System

## Overview
This is a standalone, local-first document management system built using a hybrid desktop client-server architecture:
* **Frontend Client (Tauri + React + Tailwind CSS):** A lightweight native desktop window rendering a React-based user interface.
* **Backend Service (Spring Boot 3 + Spring Data JPA + SQLite):** A lightweight background service managing document metadata storage, indexing, and deduplication.

---

## Directory Structure
```
e-dastavej/
├── backend/                  # Spring Boot 3 & SQLite project
│   ├── src/                  # Java source files
│   ├── sql/                  # SQLite tables setup scripts
│   └── pom.xml               # Maven configuration
├── frontend/                 # Tauri desktop window & React client
│   ├── src-tauri/            # Tauri desktop configuration & Rust project
│   ├── src/                  # React & Tailwind UI code
│   └── package.json          # Node configuration
└── docs/                     # Architecture & user guides
```

---

## Getting Started

### Prerequisites
* **Java Development Kit (JDK) 17 or higher**
* **Apache Maven 3.6+**
* **Node.js 18+ and npm**

---

### Step 1: Run the Backend Service
The backend creates and updates the SQLite database `file_metadata.db` locally and listens for incoming REST calls.
```bash
cd backend
mvn spring-boot:run
```
The local service runs on `http://localhost:8080`.

---

### Step 2: Launch the Tauri Desktop App
The Tauri desktop window compiles the Rust application wrapper and serves the React frontend interface.
```bash
cd frontend
npm install
npm run tauri dev
```
A native application window will display the React Dashboard interface.

---

## Features
- **Auto-Deduplication:** Computes SHA-256 hashes of files before storing to prevent duplicate documents on disk.
- **Relational Metadata:** Organizes documents by custom categories and subcategories.
- **Local Access Control:** Simulates role-based access control (Admin, Manager, Staff, Clerk, Public).
- **Fast Full-Text Search:** Indexes document metadata and contents for fast local queries.

## Documentation
- [Architecture Guide](docs/ARCHITECTURE.md)
- [User Guide](docs/USER_GUIDE.md)