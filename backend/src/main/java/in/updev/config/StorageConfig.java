package in.updev.config;

import org.springframework.context.annotation.Configuration;
import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

@Configuration
public class StorageConfig {
    
    public static String getAppHomePath() {
        return System.getProperty("user.home") + File.separator + "." + AppConfigLoader.getAppNameLower();
    }
    
    public static Path getUploadsDir() {
        return Paths.get(getAppHomePath(), "uploads").toAbsolutePath();
    }
    
    public static Path getOrganizedDir() {
        return Paths.get(getAppHomePath(), "organized").toAbsolutePath();
    }
    
    public static Path getBackupsDir() {
        return Paths.get(getAppHomePath(), "backups").toAbsolutePath();
    }
}
