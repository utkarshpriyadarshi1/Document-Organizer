package com.updevlogics.controller;

import com.updevlogics.model.Category;
import com.updevlogics.model.SubCategory;
import com.updevlogics.service.CategoryService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/categories")
@RequiredArgsConstructor
public class CategoryController {

    private final CategoryService categoryService;

    @GetMapping
    public ResponseEntity<List<Category>> getAllCategories() {
        return ResponseEntity.ok(categoryService.getAllCategories());
    }

    @PostMapping
    public ResponseEntity<?> createCategoryOnly(@RequestParam("name") String name) {
        Category category = categoryService.createCategory(name);
        return ResponseEntity.ok(category);
    }

    @PutMapping("/{id}")
    public ResponseEntity<?> updateCategory(@PathVariable("id") Long id, @RequestParam("name") String name) {
        Category category = categoryService.updateCategory(id, name);
        return ResponseEntity.ok(category);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<?> deleteCategory(@PathVariable("id") Long id) {
        categoryService.deleteCategory(id);
        return ResponseEntity.ok(Map.of("message", "Category deleted successfully"));
    }

    @PostMapping("/{id}/subcategories")
    public ResponseEntity<?> createSubCategory(@PathVariable("id") Long categoryId, @RequestParam("name") String name) {
        SubCategory subCategory = categoryService.createSubCategory(categoryId, name);
        return ResponseEntity.ok(subCategory);
    }

    @PutMapping("/subcategories/{id}")
    public ResponseEntity<?> updateSubCategory(@PathVariable("id") Long id, @RequestParam("name") String name) {
        SubCategory subCategory = categoryService.updateSubCategory(id, name);
        return ResponseEntity.ok(subCategory);
    }

    @DeleteMapping("/subcategories/{id}")
    public ResponseEntity<?> deleteSubCategory(@PathVariable("id") Long id) {
        categoryService.deleteSubCategory(id);
        return ResponseEntity.ok(Map.of("message", "Subcategory deleted successfully"));
    }

    // Keep old endpoints for compatibility
    @PostMapping("/admin/createCategory")
    public ResponseEntity<?> createCategory(@RequestParam("categoryName") String categoryName,
                                             @RequestParam("subCategoryName") String subCategoryName) {
        categoryService.createCategory(categoryName, subCategoryName);
        return ResponseEntity.ok(Map.of("message", "Category and Subcategory created successfully!"));
    }

    @PostMapping("/admin/modifyCategory")
    public ResponseEntity<?> modifyCategory(@RequestParam("categoryId") Long categoryId,
                                             @RequestParam("newCategoryName") String newCategoryName,
                                             @RequestParam("newSubCategoryName") String newSubCategoryName) {
        categoryService.modifyCategory(categoryId, newCategoryName, newSubCategoryName);
        return ResponseEntity.ok(Map.of("message", "Category and Subcategory modified successfully!"));
    }
}