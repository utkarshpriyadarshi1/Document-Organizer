# Document Organizer Project Tracker

Document Organizer is a secure, local-first document organizer designed to run completely on your local loopback workstation.

## Completed Tasks

* **Centralized Configuration:** Configured a root-level `app.config.json` containing metadata (AppName, Heading, Subtitle, Version, and Icons) dynamically loaded by frontend client, Spring Boot service, and builder scripts.
* **Directory Architecture Restructuring:** Strictly aligned workspace folders to Standardized Project Management Pattern.
* **Internationalization (i18n):** Implemented English and Hindi support in the frontend client.
* **Cache Management:** Created disk diagnostics and file-count tracker for temporary files, including functional "Clear Cache" button controls mapping to Spring backend controllers.
* **Dynamic Help System:** Integrated tab/section-specific markdown guides fetched dynamically from `docs/help` directly inside the Tauri UI layer. Added GitHub bug reporting links opening in default OS browsers.
* **Fa Iconography migration:** Fully moved legacy layout iconography to Font Awesome Free styles without verbose labels/tooltips.
* **Automated Packaging certs:** Rewrote `setup-cert.ps1` to configure windows signing certificate dynamically.
* **Automated Version bumps:** Updated `increment_version.py` script to bump and synchronize versions across `app.config.json`, `package.json`, `tauri.conf.json`, `Cargo.toml`, and Maven `pom.xml`.
* **UI Simplification & Consolidations:** Streamlined sidebar navigation to three core views (Search & Browse, Ingest Document, System Management) and consolidated Explorer, Telemetry Monitor, Category Master, Backups, and User Preferences as nested sub-tabs.

## Pending Tasks (Roadmap)

* [ ] Add PDF full-text indexing using Apache PDFBox in the backend.
* [ ] Support customized folder layout rules in Preferences (e.g., sorting folders by category instead of file formats).
* [ ] Implement OAuth2 local desktop authentication credentials for enterprise multi-user logs.
* [ ] Configure automatic background file-watcher service to auto-ingest documents from designated inbox directories.
