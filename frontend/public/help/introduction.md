### Introduction to e-Patra

e-Patra is a secure, local-first document management system. It compiles logical data records inside an embedded SQLite database and organizes physical resource layouts directly on your workstation disk.

#### Core Objectives:
- **Privacy & Security:** All index databases and files reside strictly on local loopback workstations.
- **Logical Taxonomy:** Documents are structured into Categories and Subcategories for rapid search access.
- **Physical Layout Organization:** Files are renamed and copied into organized folders on disk by file extension and date.
- **Integrity Checks:** Deduplication blocks duplicate files by performing SHA-256 integrity signature matching.
