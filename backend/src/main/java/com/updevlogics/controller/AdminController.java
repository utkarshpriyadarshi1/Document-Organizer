package com.updevlogics.controller;

import com.updevlogics.model.FileInfo;
import com.updevlogics.model.Role;
import com.updevlogics.model.User;
import com.updevlogics.service.FileService;
import com.updevlogics.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/admin")
@RequiredArgsConstructor
public class AdminController {

    private final UserService userService;
    private final FileService fileService;

    @GetMapping("/dashboard")
    public ResponseEntity<?> adminDashboard() {
        List<FileInfo> files = fileService.getLast10Files();
        List<User> users = userService.getAllUsers();
        List<Role> roles = userService.getAllRoles();
        
        return ResponseEntity.ok(Map.of(
            "files", files,
            "users", users,
            "roles", roles
        ));
    }
}