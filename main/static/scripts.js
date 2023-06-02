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
});

function leftPad(str, len, ch){
    return new Array(len - str.length).fill(!ch && ch !== 0 ? ' ':
    ch).join("") + str

};

fetch('instance/greatwall.sqlite')
    .then(res => console.log(res))