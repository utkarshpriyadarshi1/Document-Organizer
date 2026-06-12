package org.sanchaya.service;

import org.sanchaya.model.Category;
import org.sanchaya.model.SubCategory;
import org.sanchaya.repository.CategoryRepository;
import org.sanchaya.repository.SubCategoryRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Service
@RequiredArgsConstructor
@Transactional
public class CategoryService {

    private final CategoryRepository categoryRepository;
    private final SubCategoryRepository subCategoryRepository;

    public Category createCategory(String categoryName) {
        Category category = new Category();
        category.setName(categoryName);
        category.setSubCategories(new HashSet<>());
        return categoryRepository.save(category);
    }

    public void createCategory(String categoryName, String subCategoryName) {
        Category category = new Category();
        category.setName(categoryName);

        SubCategory subCategory = new SubCategory();
        subCategory.setName(subCategoryName);
        subCategory.setCategory(category);

        Set<SubCategory> subCategories = new HashSet<>();
        subCategories.add(subCategory);

        category.setSubCategories(subCategories);

        categoryRepository.save(category);
    }

    public Category updateCategory(Long categoryId, String newCategoryName) {
        Category category = categoryRepository.findById(categoryId)
                .orElseThrow(() -> new RuntimeException("Category not found"));
        category.setName(newCategoryName);
        return categoryRepository.save(category);
    }

    public void modifyCategory(Long categoryId, String newCategoryName, String newSubCategoryName) {
        Category category = categoryRepository.findById(categoryId)
                .orElseThrow(() -> new RuntimeException("Category not found"));
        category.setName(newCategoryName);

        Set<SubCategory> subCategories = category.getSubCategories();
        for (SubCategory subCategory : subCategories) {
            subCategory.setName(newSubCategoryName);
        }

        category.setSubCategories(subCategories);

        categoryRepository.save(category);
    }

    public void deleteCategory(Long categoryId) {
        categoryRepository.deleteById(categoryId);
    }

    public SubCategory createSubCategory(Long categoryId, String subCategoryName) {
        Category category = categoryRepository.findById(categoryId)
                .orElseThrow(() -> new RuntimeException("Category not found"));
        SubCategory subCategory = new SubCategory();
        subCategory.setName(subCategoryName);
        subCategory.setCategory(category);
        return subCategoryRepository.save(subCategory);
    }

    public SubCategory updateSubCategory(Long subCategoryId, String newSubCategoryName) {
        SubCategory subCategory = subCategoryRepository.findById(subCategoryId)
                .orElseThrow(() -> new RuntimeException("Subcategory not found"));
        subCategory.setName(newSubCategoryName);
        return subCategoryRepository.save(subCategory);
    }

    public void deleteSubCategory(Long subCategoryId) {
        subCategoryRepository.deleteById(subCategoryId);
    }

    public List<Category> getAllCategories() {
        return categoryRepository.findAll();
    }
}