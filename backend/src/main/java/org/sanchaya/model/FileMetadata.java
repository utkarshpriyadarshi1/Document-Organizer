package org.sanchaya.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "file_metadata")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class FileMetadata {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String originalPath;
    private String storedPath;
    private String fileType;
    private String year;
    private String month;
    private long fileSize;
    private String hash; // For duplicate detection
}
