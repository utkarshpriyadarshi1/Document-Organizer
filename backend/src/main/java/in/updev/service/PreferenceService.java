package in.updev.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import in.updev.config.AppConfigLoader;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

@Service
public class PreferenceService {
    private static final ObjectMapper mapper = new ObjectMapper();
    private static final String PREF_FILE_NAME = "preferences.json";
    
    private static Map<String, String> cachedPrefs = new HashMap<>();

    static {
        loadPreferences();
    }

    @SuppressWarnings("unchecked")
    public static synchronized Map<String, String> loadPreferences() {
        File file = getPreferencesFile();
        if (file.exists()) {
            try {
                cachedPrefs = mapper.readValue(file, Map.class);
            } catch (IOException e) {
                System.err.println("Failed to read preferences.json: " + e.getMessage());
                cachedPrefs = new HashMap<>();
            }
        } else {
            cachedPrefs = new HashMap<>();
        }
        
        // Ensure defaults are populated in cache
        boolean modified = false;
        if (!cachedPrefs.containsKey("defaultTab")) {
            cachedPrefs.put("defaultTab", "search");
            modified = true;
        }
        if (!cachedPrefs.containsKey("autoBackup")) {
            cachedPrefs.put("autoBackup", "false");
            modified = true;
        }
        if (!cachedPrefs.containsKey("backupInterval")) {
            cachedPrefs.put("backupInterval", "24");
            modified = true;
        }
        if (!cachedPrefs.containsKey("dedupStrategy")) {
            cachedPrefs.put("dedupStrategy", "sha256");
            modified = true;
        }
        if (!cachedPrefs.containsKey("storageRoot")) {
            cachedPrefs.put("storageRoot", Paths.get(System.getProperty("user.home"), "." + AppConfigLoader.getAppNameLower(), "organized").toAbsolutePath().toString());
            modified = true;
        }
        if (!cachedPrefs.containsKey("ingestTmp")) {
            cachedPrefs.put("ingestTmp", Paths.get(System.getProperty("user.home"), "." + AppConfigLoader.getAppNameLower(), "uploads").toAbsolutePath().toString());
            modified = true;
        }
        if (!cachedPrefs.containsKey("folderLayout")) {
            cachedPrefs.put("folderLayout", "default");
            modified = true;
        }

        if (modified) {
            saveToFile(cachedPrefs);
        }
        
        return cachedPrefs;
    }

    public synchronized Map<String, String> getPreferences() {
        return loadPreferences();
    }

    public synchronized void savePreferences(Map<String, String> newPrefs) {
        cachedPrefs.putAll(newPrefs);
        saveToFile(cachedPrefs);
    }

    private static void saveToFile(Map<String, String> prefs) {
        File file = getPreferencesFile();
        try {
            // Ensure parent directory exists
            File parent = file.getParentFile();
            if (parent != null) {
                parent.mkdirs();
            }
            mapper.writerWithDefaultPrettyPrinter().writeValue(file, prefs);
        } catch (IOException e) {
            System.err.println("Failed to write preferences.json: " + e.getMessage());
        }
    }

    private static File getPreferencesFile() {
        String homePath = System.getProperty("user.home") + File.separator + "." + AppConfigLoader.getAppNameLower();
        return new File(homePath, PREF_FILE_NAME);
    }

    public static String getPreference(String key, String defaultValue) {
        if (cachedPrefs.isEmpty()) {
            loadPreferences();
        }
        return cachedPrefs.getOrDefault(key, defaultValue);
    }
}
