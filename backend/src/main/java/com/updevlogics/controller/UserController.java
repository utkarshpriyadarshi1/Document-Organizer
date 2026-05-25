package com.updevlogics.controller;

import com.updevlogics.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @PostMapping("/admin/createUser")
    public ResponseEntity<?> createUser(@RequestParam("username") String username,
                                         @RequestParam("password") String password,
                                         @RequestParam("role") Long roleId) {
        userService.createUser(username, password, roleId);
        return ResponseEntity.ok(Map.of("message", "User created successfully!"));
    }

    @PostMapping("/admin/createRole")
    public ResponseEntity<?> createRole(@RequestParam("roleName") String roleName) {
        userService.createRole(roleName);
        return ResponseEntity.ok(Map.of("message", "Role created successfully!"));
    }
}