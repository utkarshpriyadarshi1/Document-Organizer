# Changelog

All notable changes to the **Document Organizer** (formerly Sanchaya / e-Patra) project will be documented in this file.

---

## [1.0.21] - 2026-06-23

### Refactored
- **Application Renaming**: Renamed application to **Document Organizer** (with tagline 'Store once, find anytime') across config files, build files, and docs.
- **Backend Relocation**: Relocated package structure from `org.sanchaya` to `in.updev` and updated all Java files.
- **Main Entry Class**: Replaced class `SanchayaApplication` with `DocumentOrganizerApplication`.
- **Database Directory Migration**: Standardized SQLite database path to `${user.home}/.documentorganizer/file_metadata.db` with auto-migration from `.sanchaya`, `.e-patra`, and `.notepad`.
- **Theme Preferences Standardisation**: Unified theme `localStorage` persistence key namespaces to `document_organizer_theme`.

### Added
- **Developer Onboarding Automation**: Added one-click script utilities `setup.bat` (Windows) and `setup.sh` (macOS/Linux) for verifying prerequisites, downloading dependencies, and running initial compilations.
- **Progress WebSocket Tracking**: Live terminal stream channel setup to monitor active backup operations directly in UI dashboard consoles.

### UI & Styling Updates
- **Premium Compact Sidebar**: Refactored dashboard sidebar layout to a narrow, high-density icon-only navigation scheme (`w-18`) emphasizing clean margins.
- **Iconography Standardisation**: Cleaned up layout buttons utilizing Font Awesome Free icons. Removed text labels and all `title` attribute tooltips (e.g. sidebar tabs, open folders, backup triggers, and category rename/delete options) for a high-end interface.
- **Telemetry Indicators**: Integrated real-time loopback API connection telemetry in the sidebar displaying status lights and service diagnostic tools.
- **Localization Expansion**: Fully bound dashboard sections, subtitles, search parameters, and category forms to dual English and Hindi locale translation mapping (`t(...)`).

### Fixed
- **Builder Cache OOM**: Resolved undefined `frontendDir` references in `builder/build.js` that caused workspace cleaner scripts to enter infinite recursion loops.
- **Version Bump Syncer**: Corrected `builder/increment_version.py` script to dynamically read `app.config.json` configurations and push product identifiers, window titles, and namespace properties down to `tauri.conf.json` and Maven `pom.xml`.
