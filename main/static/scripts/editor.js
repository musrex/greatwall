import { toggleCategory, addItem, handleTabClick } from "./functions.js";

// On page load
document.addEventListener('DOMContentLoaded', (event) => {
    // Toggle between new and existing category for new item creation
    const newCategoryToggle = document.getElementById('new_category_toggle');
    const existingCategoryToggle = document.getElementById('existing_category_toggle');

    newCategoryToggle.addEventListener('change', toggleCategory);
    existingCategoryToggle.addEventListener('change', toggleCategory);

    // Add new item to the create item page
    // Not fully implemented yet
    const add_item = document.getElementById('add_item');
    const container = document.getElementById('item_container');
    add_item.addEventListener("click", addItem);

    const tabs = document.querySelector('.tabs');
    const tabButtons = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');

    tabs.addEventListener('click', (event) => handleTabClick(event, tabButtons, tabContents));

    // Switch between tabs on the admin page
//  btn1.addEventListener("click", switchTab);
//  btn2.addEventListener("click", switchTab);
//  btn3.addEventListener("click", switchTab);
});
