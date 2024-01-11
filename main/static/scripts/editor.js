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
    // const add_item = document.getElementById('add_item');
    // const container = document.getElementById('item_container');
    // add_item.addEventListener("click", addItem);

    const tabs = document.querySelector('.tabs');
    const tabButtons = document.querySelectorAll('.tab');
    const tabContents = document.querySelectorAll('.tab-content');

    tabs.addEventListener('click', (event) => handleTabClick(event, tabButtons, tabContents));
    
    function updateDOMWithData(data) {
        var dataContainer = document.getElementById('edit_data_container');
        dataContainer.innerHTML = '';

        console.log(data);

        data.forEach(item => {
            var element = document.createElement('div');
            element.innerHTML = item.code + ' ' + item.dish + ' ' + item.price;
            dataContainer.appendChild(element);
        });
    }


    document.getElementById('edit_selector').addEventListener('change', function() {
        var selectedCategory = this.value;

        // Only make AJAX call if a category is selected
        if (selectedCategory) {
            fetch('/edit/' + encodeURIComponent(selectedCategory))
                .then(response => response.json())
                .then(data => {
                    // Update DOM with data
                    updateDOMWithData(data);
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    // Handle errors here
                });
        }
    });
});
