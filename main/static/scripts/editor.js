import { toggleCategory, addItem, switchTab } from "./functions";

// On page load
document.addEventListener('DOMContentLoaded', (event) => {
    // Toggle between new and existing category for new item creation
    const newCategoryToggle = document.getElementById('new_category_toggle');
    const existingCategoryToggle = document.getElementById('existing_category_toggle');

    let newTab = document.getElementById('category');
    let existingTab = document.getElementById('existing_category')

    newCategoryToggle.addEventListener('change', toggleCategory);
    existingCategoryToggle.addEventListener('change', toggleCategory);

    // Add new item to the create item page
    // Not fully implemented yet
    const add_item = document.getElementById('add_item');
    const container = document.getElementById('item_container');
    add_item.addEventListener("click", addItem);

    // Switch between tabs on the admin page
    let btn1 = document.getElementById("btn1");
    let btn2 = document.getElementById("btn2");
    let btn3 = document.getElementById("btn3");

    let createTab = document.getElementById("create-tab");
    let deleteTab = document.getElementById("delete-tab");
    let editTab = document.getElementById("edit-tab");

    btn1.addEventListener("click", switchTab);
    btn2.addEventListener("click", switchTab);
    btn3.addEventListener("click", switchTab);
})