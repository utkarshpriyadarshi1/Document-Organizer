package in.updev.config;

import org.springframework.context.annotation.Configuration;
import in.updev.service.PreferenceService;
import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

@Configuration
public class StorageConfig {
    
    public static String getAppHomePath() {
        return System.getProperty("user.home") + File.separator + "." + AppConfigLoader.getAppNameLower();
    }
    
    public static Path getUploadsDir() {
        return Paths.get(PreferenceService.getIngestTmp()).toAbsolutePath();
    }
    
    public static Path getOrganizedDir() {
        return Paths.get(PreferenceService.getStorageRoot()).toAbsolutePath();
    }
    
    public static Path getBackupsDir() {
        return Paths.get(getAppHomePath(), "backups").toAbsolutePath();
    }

    public static Path resolveStoredPath(String storedPath) {
        if (storedPath.startsWith("organized/")) {
            return getOrganizedDir().resolve(storedPath.substring("organized/".length())).toAbsolutePath();
        }
        return getOrganizedDir().resolve(storedPath).toAbsolutePath();
    }
}
