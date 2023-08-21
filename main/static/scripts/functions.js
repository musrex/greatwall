function toggleCategory(event) {
    if (event.target.id === 'new_category_toggle') {
        existingTab.style.display = 'none';
        newTab.style.display = 'block';
        existingCategoryToggle.checked = false;
    } else if ( event.target.id === 'existing_category_toggle') {
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


function switchTab(event) {
    let btn0 = document.getElementById("btn1");
    let btn1 = document.getElementById("btn2");
    let btn2 = document.getElementById("btn3");

    let createTab = document.getElementById("create-tab");
    let deleteTab = document.getElementById("delete-tab");
    let editTab = document.getElementById("edit-tab");
    
    if (event.target.id === "btn0") {
        createTab.style.display = "block";
        btn0.classList.add("tab-active");
        btn1.classList.remove("tab-active");
        btn2.classList.remove("tab-active");
        deleteTab.style.display = "none";
        editTab.style.display = "none";
    } else if (event.target.id === "btn1") {
        createTab.style.display = "none";
        deleteTab.style.display = "block";
        btn0.classList.remove("tab-active");
        btn1.classList.add("tab-active");
        btn2.classList.remove("tab-active");
        editTab.style.display = "none";
    } else if (event.target.id === "btn2") {
        createTab.style.display = "none";
        deleteTab.style.display = "none";
        editTab.style.display = "block";
        btn0.classList.remove("tab-active");
        btn1.classList.remove("tab-active");
        btn2.classList.add("tab-active");
    }
}


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


export { toggleCategory, addItem, switchTab, toggleCard }