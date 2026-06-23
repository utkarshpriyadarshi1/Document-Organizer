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
        String customPath = PreferenceService.getPreference("ingestTmp", null);
        if (customPath != null && !customPath.trim().isEmpty()) {
            return Paths.get(customPath).toAbsolutePath();
        }
        return Paths.get(getAppHomePath(), "uploads").toAbsolutePath();
    }
    
    public static Path getOrganizedDir() {
        String customPath = PreferenceService.getPreference("storageRoot", null);
        if (customPath != null && !customPath.trim().isEmpty()) {
            return Paths.get(customPath).toAbsolutePath();
        }
        return Paths.get(getAppHomePath(), "organized").toAbsolutePath();
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
