# Standalone Desktop Architecture

This document outlines the architecture for the standalone version of **e-Dastavej**.

## Component Overview

The application is split into two main layers that run entirely on the local user machine:

1. **Frontend (Tauri + React + Tailwind):** 
   - A native desktop window rendered using the host operating system's native Webview (Webkit/WebView2).
   - A React-based Single Page Application (SPA) providing search UI, dashboards, upload forms, and system administration screens.
   - Communicates with the local Java backend service via standard HTTP/REST endpoints.

2. **Backend (Spring Boot 3 + Hibernate + SQLite):**
   - A lightweight Spring Boot application running as a local background service on port `8080`.
   - Embedded SQLite engine to store metadata, categories, users, roles, and change logs.
   - Handles file management operations directly on the local file system (copying uploaded files into organized folders and computing SHA-256 hashes to prevent duplication).

```
┌───────────────────────────────────────┐
│        Desktop Tauri GUI (React)      │
└───────────────────┬───────────────────┘
                    │ REST API / WebSockets
                    ▼
┌───────────────────────────────────────┐
│     Local Spring Boot Backend (JVM)    │
└─────────┬───────────────────┬─────────┘
          │                   │
          ▼ SQL               ▼ IO
┌───────────────────┐   ┌───────────────────────┐
│   SQLite File     │   │ Organized Files Dir   │
│ (file_metadata.db)│   │ (organized/type/year) │
└───────────────────┘   └───────────────────────┘
```

## System Patterns

### 1. Unified Local File Storage
All uploaded files are automatically renamed, structured, and saved in a designated directory on the user's hard drive:
```
organized/{file_type}/{year}/{month}/{filename}
```
Metadata paths are stored relative to this root folder to maintain portability if the database file and organized directory are moved to another drive or folder.

### 2. Duplicate Detection
Before saving any file:
- The backend computes the SHA-256 hash of the input stream.
- It queries the `file_metadata` database table for an existing record with the matching hash.
- If a match is found, the duplicate upload is cancelled, and the user is notified.

### 3. Local Access Control
While this is a standalone app, it retains role-based access control (RBAC):
- Local databases initialize with predefined roles: `ADMIN`, `MANAGER`, `STAFF`, `CLERK`, `PUBLIC`.
- Users log in locally using secure hashed credentials (BCrypt).
- Security policies in Spring Security enforce API-level protection to ensure multi-user role simulation works correctly on local shared workstations.
