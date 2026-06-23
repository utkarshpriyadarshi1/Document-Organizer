package in.updev;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DocumentOrganizerApplication {
    static {
        // Force config loading
        in.updev.config.AppConfigLoader.loadConfig();
        String appNameLower = in.updev.config.AppConfigLoader.getAppNameLower();
        String homeDir = System.getProperty("user.home");
        java.io.File appFolder = new java.io.File(homeDir, "." + appNameLower);
        if (!appFolder.exists()) {
            appFolder.mkdirs();
        }
        
        // Dynamically set spring datasource url property before spring boot starts
        System.setProperty("spring.datasource.url", "jdbc:sqlite:" + appFolder.getAbsolutePath() + "/file_metadata.db");
        System.out.println(">>> Set datasource URL: " + System.getProperty("spring.datasource.url"));
    }

    public static void main(String[] args) {
        String appNameLower = in.updev.config.AppConfigLoader.getAppNameLower();
        String homeDir = System.getProperty("user.home");
        java.io.File appFolder = new java.io.File(homeDir, "." + appNameLower);
        java.io.File migratedDb = new java.io.File(appFolder, "file_metadata.db");

        // 1. Migrate database from .sanchaya if it exists and new folder doesn't have it yet
        java.io.File oldSanchayaFolder = new java.io.File(homeDir, ".sanchaya");
        java.io.File oldSanchayaDb = new java.io.File(oldSanchayaFolder, "file_metadata.db");
        if (oldSanchayaDb.exists() && !migratedDb.exists()) {
            try {
                java.nio.file.Files.copy(oldSanchayaDb.toPath(), migratedDb.toPath(), java.nio.file.StandardCopyOption.REPLACE_EXISTING);
                System.out.println(">>> Migrated existing SQLite database from .sanchaya to: " + migratedDb.getAbsolutePath());
            } catch (Exception e) {
                System.err.println(">>> Database migration from .sanchaya failed: " + e.getMessage());
            }
        }

        // 2. Migrate existing database to user home if it exists locally in workspace root
        java.io.File localDb = new java.io.File("file_metadata.db");
        if (localDb.exists() && !migratedDb.exists()) {
            try {
                java.nio.file.Files.copy(localDb.toPath(), migratedDb.toPath(), java.nio.file.StandardCopyOption.REPLACE_EXISTING);
                System.out.println(">>> Migrated existing local SQLite database to: " + migratedDb.getAbsolutePath());
            } catch (Exception e) {
                System.err.println(">>> Local database migration failed: " + e.getMessage());
            }
        }

        // 3. Migrate legacy e-Patra SQLite database if it exists (for compatibility if folder name differs)
        java.io.File legacyFolder = new java.io.File(homeDir, ".e-patra");
        java.io.File legacyDb = new java.io.File(legacyFolder, "file_metadata.db");
        if (!legacyFolder.getAbsolutePath().equals(appFolder.getAbsolutePath()) && legacyDb.exists() && !migratedDb.exists()) {
            try {
                java.nio.file.Files.copy(legacyDb.toPath(), migratedDb.toPath(), java.nio.file.StandardCopyOption.REPLACE_EXISTING);
                System.out.println(">>> Migrated legacy e-Patra SQLite database to: " + migratedDb.getAbsolutePath());
            } catch (Exception e) {
                System.err.println(">>> Legacy database migration failed: " + e.getMessage());
            }
        }

        // 4. Migrate legacy notepad SQLite database if it exists
        java.io.File notepadFolder = new java.io.File(homeDir, ".notepad");
        java.io.File notepadDb = new java.io.File(notepadFolder, "file_metadata.db");
        if (!notepadFolder.getAbsolutePath().equals(appFolder.getAbsolutePath()) && notepadDb.exists() && !migratedDb.exists()) {
            try {
                java.nio.file.Files.copy(notepadDb.toPath(), migratedDb.toPath(), java.nio.file.StandardCopyOption.REPLACE_EXISTING);
                System.out.println(">>> Migrated legacy notepad SQLite database to: " + migratedDb.getAbsolutePath());
            } catch (Exception e) {
                System.err.println(">>> Legacy notepad database migration failed: " + e.getMessage());
            }
        }

        SpringApplication.run(DocumentOrganizerApplication.class, args);
    }
}
