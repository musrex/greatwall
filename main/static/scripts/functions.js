function toggleCategory(event) {
    let newCategoryToggle = document.getElementById('new_category_toggle');
    let existingCategoryToggle = document.getElementById('existing_category_toggle');
    let categoryLabel = document.getElementById('category_label');

    let newTab = document.getElementById('category');
    let existingTab = document.getElementById('existing_category')

    if (event.target.id === 'new_category_toggle') {
        categoryLabel.style.dipslay = 'block';
        existingTab.style.display = 'none';
        newTab.style.display = 'block';
        existingCategoryToggle.checked = false;
    } else if ( event.target.id === 'existing_category_toggle') {
        categoryLabel.style.display = 'block';
        existingTab.style.display = 'block';
        newTab.style.display = 'none';
        newCategoryToggle.checked = false;
    }
}


function addItem(){
    // Container needs to be empty for this to work
    let input = document.createElement('input');
    input.placeholder = 'Test';
    container.appendChild(input);
}

function handleTabClick(event, tabButtons, tabContents) {
    if (!event.target.matches('.tab')) return;

    const targetTabContentId = event.target.getAttribute('data-tab-target');
    const targetTabContent = document.getElementById(targetTabContentId);

    tabContents.forEach(function(tabContent) {
        tabContent.style.display = 'none';
    });

    tabButtons.forEach(function(tabButton) {
        tabButton.classList.remove('tab-active');
    });

    targetTabContent.style.display = 'block'
    event.target.classList.add('tab-active');
};

// function switchTab(event) {
//     let btn1 = document.getElementById("btn1");
//     let btn2 = document.getElementById("btn2");
//     let btn3 = document.getElementById("btn3");
// 
//     let createTab = document.getElementById("create-tab");
//     let deleteTab = document.getElementById("delete-tab");
//     let editTab = document.getElementById("edit-tab");
//     
//     if (event.target.id === "btn1") {
//         createTab.style.display = "block";
//         btn1.classList.add("tab-active");
//         btn2.classList.remove("tab-active");
//         btn3.classList.remove("tab-active");
//         deleteTab.style.display = "none";
//         editTab.style.display = "none";
//     } else if (event.target.id === "btn2") {
//         createTab.style.display = "none";
//         deleteTab.style.display = "block";
//         btn1.classList.remove("tab-active");
//         btn2.classList.add("tab-active");
//         btn3.classList.remove("tab-active");
//         editTab.style.display = "none";
//     } else if (event.target.id === "btn3") {
//         createTab.style.display = "none";
//         deleteTab.style.display = "none";
//         editTab.style.display = "block";
//         btn1.classList.remove("tab-active");
//         btn2.classList.remove("tab-active");
//         btn3.classList.add("tab-active");
//     }
// }


function toggleCard(element) {
    if (element.classList.contains('card-expanded')) {
        element.classList.remove('card-expanded');
        element.classList.add('cards');
    } else {
        const expandedCards = document.querySelectorAll('.card-expanded');
        expandedCards.forEach(card => {
            card.classList.remove('card-expanded')
            card.classList.add('cards');
        });
        element.classList.add('card-expanded')
        element.classList.remove('cards');
    }
    };


export { toggleCategory, addItem, handleTabClick, toggleCard }
