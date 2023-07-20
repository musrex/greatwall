document.addEventListener('DOMContentLoaded', (event) => {
    const add_item = document.getElementById('add_item');
    const container = document.getElementById('input_container');


    function addItem(){
        // Container needs to be empty for this to work
        let input = document.createElement('input');
        input.placeholder = 'Test';
        container.appendChild(input);
        }
    
    add_item.addEventListener("click", addItem);
    
    let btn1 = document.getElementById("btn1");
    let btn2 = document.getElementById("btn2");
    let btn3 = document.getElementById("btn3");

    let createTab = document.getElementById("create-tab");
    let deleteTab = document.getElementById("delete-tab");
    let editTab = document.getElementById("edit-tab");

    function switchTab(event) {
        if (event.target.id === "btn1") {
            createTab.style.display = "block";
            btn1.classList.add("tab-active");
            btn2.classList.remove("tab-active");
            btn3.classList.remove("tab-active");
            deleteTab.style.display = "none";
            editTab.style.display = "none";
        } else if (event.target.id === "btn2") {
            createTab.style.display = "none";
            deleteTab.style.display = "block";
            btn1.classList.remove("tab-active");
            btn2.classList.add("tab-active");
            btn3.classList.remove("tab-active");
            editTab.style.display = "none";
        } else if (event.target.id === "btn3") {
            createTab.style.display = "none";
            deleteTab.style.display = "none";
            editTab.style.display = "block";
            btn1.classList.remove("tab-active");
            btn2.classList.remove("tab-active");
            btn3.classList.add("tab-active");
        }
    }
  
    btn1.addEventListener("click", switchTab);
    btn2.addEventListener("click", switchTab);
    btn3.addEventListener("click", switchTab);
    });

    function leftPad(str, len, ch){
        return new Array(len - str.length).fill(!ch && ch !== 0 ? ' ':
        ch).join("") + str
    };
