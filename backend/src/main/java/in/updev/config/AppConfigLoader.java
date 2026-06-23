package in.updev.config;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;
import java.util.Map;

public class AppConfigLoader {
    private static String appName = "Document Organizer";
    private static String heading = "Document Organizer";
    private static String subtitle = "Store once, find anytime";
    private static String goal = "All files uploaded via our application remain retrievable in milliseconds, even after decades.";
    private static String version = "1.0.0";

    static {
        loadConfig();
    }

    @SuppressWarnings("unchecked")
    public static void loadConfig() {
        // Look for app.config.json in the current working directory, 
        // the parent directory, or in the classpath resources.
        File file = new File("app.config.json");
        if (!file.exists()) {
            file = new File("../app.config.json");
        }
        
        if (file.exists()) {
            try {
                ObjectMapper mapper = new ObjectMapper();
                Map<String, Object> config = mapper.readValue(file, Map.class);
                if (config.containsKey("appName")) {
                    appName = (String) config.get("appName");
                }
                if (config.containsKey("heading")) {
                    heading = (String) config.get("heading");
                }
                if (config.containsKey("subtitle")) {
                    subtitle = (String) config.get("subtitle");
                }
                if (config.containsKey("goal")) {
                    goal = (String) config.get("goal");
                }
                if (config.containsKey("version")) {
                    version = (String) config.get("version");
                }
                System.out.println(">>> AppConfigLoader: Loaded config from " + file.getAbsolutePath() + ": appName=" + appName + ", version=" + version);
            } catch (IOException e) {
                System.err.println(">>> AppConfigLoader: Failed to parse app.config.json: " + e.getMessage());
            }
        } else {
            // Fallback: search for resource in classpath
            System.out.println(">>> AppConfigLoader: app.config.json not found on disk. Using defaults: appName=" + appName + ", version=" + version);
        }
    }

    public static String getAppName() {
        return appName;
    }

    public static String getAppNameLower() {
        return appName.toLowerCase().replaceAll("[^a-zA-Z0-9.-]", "");
    }

    public static String getHeading() {
        return heading;
    }

    public static String getSubtitle() {
        return subtitle;
    }

    public static String getGoal() {
        return goal;
    }

    public static String getVersion() {
        return version;
    }
}
