package in.updev.service;

import in.updev.model.FileMetadata;
import in.updev.model.FileInfo;
import in.updev.repository.FileRepository;
import in.updev.repository.FileMetadataRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import org.springframework.transaction.annotation.Transactional;
import in.updev.config.StorageConfig;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.security.MessageDigest;
import java.util.Date;
import java.util.List;
import java.util.Optional;

@Service
public class FileService {

    private final FileRepository fileRepository;
    private final FileMetadataRepository fileMetadataRepository;

    @Autowired
    public FileService(FileRepository fileRepository, FileMetadataRepository fileMetadataRepository) {
        this.fileRepository = fileRepository;
        this.fileMetadataRepository = fileMetadataRepository;
    }

    @Transactional(rollbackFor = Exception.class)
    public void saveFile(MultipartFile multipartFile, String description, String category, String subCategory) throws IOException {
        String fileName = multipartFile.getOriginalFilename();
        Path uploadDir = StorageConfig.getUploadsDir();
        Files.createDirectories(uploadDir);
        File file = uploadDir.resolve(fileName).toFile();
        
        multipartFile.transferTo(file);

        FileInfo fileInfo = new FileInfo();
        fileInfo.setFileName(fileName);
        fileInfo.setFilePath(file.getPath());
        fileInfo.setFileType(multipartFile.getContentType());
        fileInfo.setFileSize(multipartFile.getSize());
        fileInfo.setDescription(description);
        fileInfo.setCategory(category);
        fileInfo.setSubCategory(subCategory);
        fileInfo.setUploadDate(new Date());

        fileRepository.saveFile(fileInfo);

        try {
            storeFile(file.getPath(), category, subCategory);
        } catch (Exception e) {
            // Delete the temporary uploaded file to prevent orphan files on disk
            if (file.exists()) {
                file.delete();
            }
            throw new RuntimeException("Failed to organize and register file metadata: " + e.getMessage(), e);
        }
    }

    public List<FileInfo> getAllFiles() {
        return fileRepository.getAllFiles();
    }

    public List<FileInfo> searchFiles(String query, String fileType, String role, Date dateFrom, Date dateTo, String category, String subCategory) {
        return fileRepository.searchFiles(query, fileType, role, dateFrom, dateTo, category, subCategory);
    }

    public List<FileInfo> getLast10Files() {
        return fileRepository.getLast10Files();
    }

    public String storeFile(String filePath) throws Exception {
        return storeFile(filePath, null, null);
    }

    public String storeFile(String filePath, String category, String subCategory) throws Exception {
        Path source = Paths.get(filePath);
        String fileType = Files.probeContentType(source);
        if (fileType != null && fileType.contains("/")) {
            fileType = fileType.substring(fileType.indexOf("/") + 1);
        }
        if (fileType == null || fileType.isEmpty()) {
            String name = source.getFileName().toString();
            int lastDot = name.lastIndexOf('.');
            fileType = (lastDot > 0) ? name.substring(lastDot + 1).toLowerCase() : "unknown";
        }
        String year = String.valueOf(Files.getLastModifiedTime(source).toInstant().atZone(java.time.ZoneId.systemDefault()).getYear());
        String month = String.format("%02d", Files.getLastModifiedTime(source).toInstant().atZone(java.time.ZoneId.systemDefault()).getMonthValue());

        String folderLayout = PreferenceService.getFolderLayout();
        String relativePath;

        if ("category".equalsIgnoreCase(folderLayout)) {
            String catFolder = (category != null && !category.trim().isEmpty()) ? category.trim() : "Uncategorized";
            String subCatFolder = (subCategory != null && !subCategory.trim().isEmpty()) ? subCategory.trim() : "General";
            catFolder = catFolder.replaceAll("[\\\\/:*?\"<>|]", "_");
            subCatFolder = subCatFolder.replaceAll("[\\\\/:*?\"<>|]", "_");
            relativePath = "organized/" + catFolder + "/" + subCatFolder + "/" + year + "/" + month + "/" + source.getFileName();
        } else if ("chronological".equalsIgnoreCase(folderLayout)) {
            relativePath = "organized/" + year + "/" + month + "/" + fileType + "/" + source.getFileName();
        } else {
            relativePath = "organized/" + fileType + "/" + year + "/" + month + "/" + source.getFileName();
        }

        Path destination = StorageConfig.resolveStoredPath(relativePath);

        Files.createDirectories(destination.getParent());
        Files.copy(source, destination, StandardCopyOption.REPLACE_EXISTING);

        try {
            String hash = generateFileHash(source);
            String dedupStrategy = PreferenceService.getDedupStrategy();
            if ("sha256".equalsIgnoreCase(dedupStrategy)) {
                Optional<FileMetadata> existingFile = fileMetadataRepository.findByHash(hash);
                if (existingFile.isPresent()) {
                    Files.delete(destination); // Remove duplicate
                    throw new IllegalArgumentException("Duplicate file detected: A file with the same content signature already exists in the archive.");
                }
            }

            FileMetadata metadata = new FileMetadata(null, filePath, relativePath, fileType, year, month, Files.size(source), hash);
            fileMetadataRepository.save(metadata);
        } catch (Exception e) {
            // Clean up copied physical file in organized/ folder to prevent stray disk allocations
            if (Files.exists(destination)) {
                Files.delete(destination);
            }
            throw e;
        }

        return "File stored at: " + relativePath;
    }

    public List<FileMetadata> getAllMetadata() {
        return fileMetadataRepository.findAll();
    }

    public Optional<FileMetadata> getMetadataById(Long id) {
        return fileMetadataRepository.findById(id);
    }

    private String generateFileHash(Path path) throws Exception {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] fileBytes = Files.readAllBytes(path);
        byte[] hash = digest.digest(fileBytes);
        StringBuilder hexString = new StringBuilder();
        for (byte b : hash) {
            hexString.append(String.format("%02x", b));
        }
        return hexString.toString();
    }
}