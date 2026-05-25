package com.updevlogics.model;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "backup_records")
@Getter @Setter @NoArgsConstructor @AllArgsConstructor
public class BackupRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String backupPath;
    private LocalDateTime timestamp;
    private String status; // SUCCESS, FAILED, IN_PROGRESS
}
