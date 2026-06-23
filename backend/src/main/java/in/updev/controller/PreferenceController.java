package in.updev.controller;

import in.updev.service.PreferenceService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/preferences")
@RequiredArgsConstructor
@CrossOrigin(origins = "*")
public class PreferenceController {

    private final PreferenceService preferenceService;

    @GetMapping
    public ResponseEntity<Map<String, String>> getPreferences() {
        return ResponseEntity.ok(preferenceService.getPreferences());
    }

    @PostMapping
    public ResponseEntity<Map<String, String>> updatePreferences(@RequestBody Map<String, String> preferences) {
        preferenceService.savePreferences(preferences);
        return ResponseEntity.ok(preferenceService.getPreferences());
    }
}
