### Ingesting Documents

Ingestion imports standalone files into the system workspace, mapping them to categories and calculating file hashes.

#### Process Workflow:
- **Choose Resource:** Select a file or drag and drop it into the ingest target container.
- **Assign Taxonomy:** Map the document to a parent Category and secondary Subcategory.
- **Provide Summary:** Write key terms or descriptive text in the description box to aid retrieval.
- **Submit Indexing:** Click "Index and Store File" to initiate the process.

#### SHA-256 Deduplication:
Document Organizer computes the SHA-256 cryptographic signature of every document. If the signature matches an existing indexed record, the physical storage copy is skipped, saving disk space, and mapping is established logically in the SQLite index database.
