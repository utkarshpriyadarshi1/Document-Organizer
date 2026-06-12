package org.sanchaya.service;

import org.sanchaya.SanchayaApplication;
import org.sanchaya.model.FileInfo;
import org.sanchaya.model.FileMetadata;
import org.sanchaya.repository.FileMetadataRepository;
import org.sanchaya.repository.FileRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.mock.web.MockMultipartFile;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(classes = SanchayaApplication.class)
public class FileServiceTest {

    @Autowired
    private FileService fileService;

    @Autowired
    private FileRepository fileRepository;

    @Autowired
    private FileMetadataRepository fileMetadataRepository;

    @Autowired
    private JdbcTemplate jdbcTemplate;

    private MockMultipartFile testFile1;
    private MockMultipartFile testFile2;

    @BeforeEach
    public void setUp() {
        cleanDb();
        testFile1 = new MockMultipartFile(
                "file",
                "test_document_1.txt",
                "text/plain",
                "Hello World this is unique content 1".getBytes()
        );
        testFile2 = new MockMultipartFile(
                "file",
                "test_document_2.txt",
                "text/plain",
                "Hello World this is unique content 2".getBytes()
        );
    }

    @AfterEach
    public void tearDown() {
        cleanDb();
    }

    private void cleanDb() {
        jdbcTemplate.execute("DELETE FROM file_info");
        jdbcTemplate.execute("DELETE FROM file_metadata");
    }

    @Test
    public void testSaveFileSuccessAndSearch() throws IOException {
        // Save unique file
        fileService.saveFile(testFile1, "This is the first test file for engineering department", "Engineering", "Docs");

        // Verify database entry in FileInfo
        List<FileInfo> files = fileRepository.getAllFiles();
        boolean foundInfo = files.stream().anyMatch(f -> f.getFileName().equals("test_document_1.txt"));
        assertTrue(foundInfo, "FileInfo record should be created");

        // Verify database entry in FileMetadata
        List<FileMetadata> metadataList = fileMetadataRepository.findAll();
        boolean foundMeta = metadataList.stream().anyMatch(m -> m.getStoredPath().contains("test_document_1.txt"));
        assertTrue(foundMeta, "FileMetadata record should be created");

        // Verify search matching query inside fileName
        List<FileInfo> searchResName = fileRepository.searchFiles("test_document", null, null, null, null, null, null);
        assertFalse(searchResName.isEmpty(), "Should match by fileName");

        // Verify search matching query inside description
        List<FileInfo> searchResDesc = fileRepository.searchFiles("engineering", null, null, null, null, null, null);
        assertFalse(searchResDesc.isEmpty(), "Should match by description (OR predicate)");
    }

    @Test
    public void testSaveDuplicateFileThrowsExceptionAndRollsBack() throws IOException {
        // Save first file
        fileService.saveFile(testFile2, "Original file content", "General", "Test");

        int initialFilesCount = fileRepository.getAllFiles().size();
        int initialMetaCount = fileMetadataRepository.findAll().size();

        // Try to save duplicate file (same byte content, same hash)
        MockMultipartFile duplicateFile = new MockMultipartFile(
                "file",
                "duplicate_doc.txt",
                "text/plain",
                "Hello World this is unique content 2".getBytes()
        );

        assertThrows(RuntimeException.class, () -> {
            fileService.saveFile(duplicateFile, "Duplicate file content", "General", "Test");
        }, "Ingesting duplicate content should throw exception");

        // Verify database rolled back: no new entries in FileInfo or FileMetadata
        int finalFilesCount = fileRepository.getAllFiles().size();
        int finalMetaCount = fileMetadataRepository.findAll().size();

        assertEquals(initialFilesCount, finalFilesCount, "FileInfo database save should rollback");
        assertEquals(initialMetaCount, finalMetaCount, "FileMetadata database save should rollback");
    }
}
