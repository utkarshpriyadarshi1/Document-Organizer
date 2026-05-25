package com.updevlogics.controller;

import com.updevlogics.model.BackupRecord;
import com.updevlogics.service.BackupService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;

@RestController
@RequestMapping("/api/backup")
@RequiredArgsConstructor
public class BackupController {

    private final BackupService backupService;

    @GetMapping("/history")
    public List<BackupRecord> getBackupHistory() {
        return backupService.getAllBackups();
    }

    @PostMapping("/create")
    public String createBackup() {
        return backupService.createBackup();
    }
}
