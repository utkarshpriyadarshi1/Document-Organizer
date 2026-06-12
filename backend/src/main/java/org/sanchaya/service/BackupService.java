package org.sanchaya.service;

import org.sanchaya.model.BackupRecord;
import org.sanchaya.repository.BackupRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.sanchaya.config.StorageConfig;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class BackupService {

    private final BackupRepository backupRepository;
    private final BackupProgressHandler progressHandler;

    public List<BackupRecord> getAllBackups() {
        return backupRepository.findAll();
    }

    public String createBackup() {
        try {
            progressHandler.sendProgress("Backup started...");
            Path source = StorageConfig.getOrganizedDir();
            Path destination = StorageConfig.getBackupsDir().resolve("backup_" + System.currentTimeMillis());

            Files.createDirectories(destination);
            progressHandler.sendProgress("Created destination folder. Copying files...");
            copyFolder(source, destination);

            String backupRecordPath = "backups/" + destination.getFileName().toString();
            BackupRecord record = new BackupRecord(null, backupRecordPath, LocalDateTime.now(), "SUCCESS");
            backupRepository.save(record);

            progressHandler.sendProgress("Backup completed successfully.");
            return "Backup created at: " + backupRecordPath;
        } catch (Exception e) {
            progressHandler.sendProgress("Backup failed: " + e.getMessage());
            return "Backup failed: " + e.getMessage();
        }
    }

    private void copyFolder(Path source, Path destination) throws Exception {
        if (!Files.exists(source)) {
            return;
        }
        Files.walk(source).forEach(file -> {
            try {
                Path target = destination.resolve(source.relativize(file));
                if (Files.isDirectory(file)) {
                    Files.createDirectories(target);
                } else {
                    Files.copy(file, target, StandardCopyOption.REPLACE_EXISTING);
                }
            } catch (Exception ignored) {}
        });
    }
}
