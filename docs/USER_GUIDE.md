# e-Dastavej User Guide

Welcome to the standalone desktop version of **e-Dastavej**, a local document management system designed to run on a single workstation or network-shared drive.

## Prerequisite Software
- **Java Runtime Environment (JRE) 17 or higher** (to run the local Spring Boot service).
- **Node.js 18 or higher** (for local development and Tauri client UI execution).

## Getting Started

### 1. Launch the Backend Server
From the `backend` directory, start the Spring Boot server:
```bash
cd backend
mvn spring-boot:run
```
The server will initialize a SQLite database file named `file_metadata.db` in the backend root directory and start listening on `http://localhost:8080`.

### 2. Launch the Desktop Client
From the `frontend` directory, start the Tauri desktop GUI:
```bash
cd frontend
npm install
npm run tauri dev
```
A native application window will open, auto-connecting to the local backend.

---

## Key Features

### 1. Role-Based Logins
The application emulates permissions locally:
- **Public:** Search and download public documents.
- **Clerk:** Upload files and categorize them.
- **Staff / Assistant:** Manage files and review metadata.
- **Admin:** Create local users, manage categories, and inspect system audit logs.

### 2. Document Uploads & Deduplication
- Click on the **Upload** page, drag and drop files, and specify a description, category, and subcategory.
- The system automatically hashes the file content. If a duplicate file already exists, it stops the upload and alerts you of the existing document location to save disk space.

### 3. Smart Local Search
- Search documents by filename, content tags, or date range.
- Filters allow sorting by categories, file types (PDF, Images, Text), and roles.
