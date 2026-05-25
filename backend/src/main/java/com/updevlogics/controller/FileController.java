package com.updevlogics.controller;

import com.updevlogics.model.FileInfo;
import com.updevlogics.service.FileService;
import lombok.RequiredArgsConstructor;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import com.updevlogics.model.FileMetadata;
import com.updevlogics.config.StorageConfig;
import java.io.File;
import java.io.IOException;
import java.util.Date;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/files")
@RequiredArgsConstructor
public class FileController {

    private final FileService fileService;

    @PostMapping("/upload")
    public ResponseEntity<?> uploadFile(@RequestParam("file") MultipartFile file,
                                        @RequestParam("description") String description,
                                        @RequestParam("category") String category,
                                        @RequestParam("subCategory") String subCategory) {
        try {
            fileService.saveFile(file, description, category, subCategory);
            return ResponseEntity.ok(Map.of("message", "File uploaded successfully!"));
        } catch (IOException e) {
            return ResponseEntity.status(500).body(Map.of("message", "File upload failed: " + e.getMessage()));
        }
    }

    @PostMapping("/store-local")
    public ResponseEntity<?> storeLocalFile(@RequestParam("filePath") String filePath) {
        try {
            String result = fileService.storeFile(filePath);
            return ResponseEntity.ok(Map.of("message", result));
        } catch (Exception e) {
            return ResponseEntity.status(500).body(Map.of("message", "Local storage failed: " + e.getMessage()));
        }
    }

    @GetMapping("/all")
    public ResponseEntity<List<FileInfo>> getAllFiles() {
        return ResponseEntity.ok(fileService.getAllFiles());
    }

    @GetMapping("/recent")
    public ResponseEntity<List<FileInfo>> getRecentFiles() {
        return ResponseEntity.ok(fileService.getLast10Files());
    }

    @GetMapping("/search")
    public ResponseEntity<List<FileInfo>> searchFiles(@RequestParam("query") String query,
                                                      @RequestParam(value = "fileType", required = false) String fileType,
                                                      @RequestParam(value = "role", required = false) String role,
                                                      @RequestParam(value = "dateFrom", required = false) @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) Date dateFrom,
                                                      @RequestParam(value = "dateTo", required = false) @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) Date dateTo,
                                                      @RequestParam(value = "category", required = false) String category,
                                                      @RequestParam(value = "subCategory", required = false) String subCategory) {
        List<FileInfo> files = fileService.searchFiles(query, fileType, role, dateFrom, dateTo, category, subCategory);
        return ResponseEntity.ok(files);
    }

    @GetMapping("/metadata")
    public ResponseEntity<List<FileMetadata>> getAllMetadata() {
        return ResponseEntity.ok(fileService.getAllMetadata());
    }

    @GetMapping("/storage-stats")
    public ResponseEntity<?> getStorageStats() {
        File appHomeDir = new File(StorageConfig.getAppHomePath());
        File organizedDir = StorageConfig.getOrganizedDir().toFile();
        File uploadsDir = StorageConfig.getUploadsDir().toFile();
        
        long totalSpace = appHomeDir.getTotalSpace();
        long freeSpace = appHomeDir.getFreeSpace();
        
        long organizedSize = getFolderSize(organizedDir);
        long uploadsSize = getFolderSize(uploadsDir);
        
        return ResponseEntity.ok(Map.of(
            "totalSpace", totalSpace,
            "freeSpace", freeSpace,
            "organizedSize", organizedSize,
            "uploadsSize", uploadsSize,
            "organizedPath", organizedDir.getAbsolutePath(),
            "uploadsPath", uploadsDir.getAbsolutePath()
        ));
    }

    @PostMapping("/metadata/{id}/open-location")
    public ResponseEntity<?> openLocation(@PathVariable("id") Long id) {
        Optional<FileMetadata> metadataOpt = fileService.getMetadataById(id);
        if (metadataOpt.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        FileMetadata metadata = metadataOpt.get();
        File file = new File(StorageConfig.getAppHomePath(), metadata.getStoredPath());
        if (!file.exists()) {
            return ResponseEntity.status(400).body(Map.of("message", "Physical file does not exist on disk: " + file.getAbsolutePath()));
        }
        try {
            // Run Windows Explorer and highlight the file
            new ProcessBuilder("explorer.exe", "/select,", file.getAbsolutePath()).start();
            return ResponseEntity.ok(Map.of("message", "Opened location successfully"));
        } catch (IOException e) {
            return ResponseEntity.status(500).body(Map.of("message", "Failed to open folder location: " + e.getMessage()));
        }
    }

    @PostMapping("/metadata/{id}/run")
    public ResponseEntity<?> runFile(@PathVariable("id") Long id) {
        Optional<FileMetadata> metadataOpt = fileService.getMetadataById(id);
        if (metadataOpt.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        FileMetadata metadata = metadataOpt.get();
        File file = new File(StorageConfig.getAppHomePath(), metadata.getStoredPath());
        if (!file.exists()) {
            return ResponseEntity.status(400).body(Map.of("message", "Physical file does not exist on disk: " + file.getAbsolutePath()));
        }
        try {
            // Run the file using standard OS execution handler (via cmd /c start)
            new ProcessBuilder("cmd.exe", "/c", "start", "", file.getAbsolutePath()).start();
            return ResponseEntity.ok(Map.of("message", "Launched file successfully"));
        } catch (IOException e) {
            return ResponseEntity.status(500).body(Map.of("message", "Failed to launch file: " + e.getMessage()));
        }
    }

    private long getFolderSize(File folder) {
        if (!folder.exists()) return 0;
        long length = 0;
        File[] files = folder.listFiles();
        if (files == null) return 0;
        for (File file : files) {
            if (file.isFile()) {
                length += file.length();
            } else {
                length += getFolderSize(file);
            }
        }
        return length;
    }
}