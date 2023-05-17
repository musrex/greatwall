document.addEventListener('DOMContentLoaded', (event) => {
    const add_item = document.getElementById('add_item');

    function addItem(htmlStr) {
        let frag = document.createDocumentFragment(),
            temp = document.createElement('div');
        temp.innerHTML = htmlStr;
        while (temp.firstChild) {
            frag.appendChild(temp.firstChild);
        }
        return frag;
    };

    let fragment = addItem(
    '<label for="code">Code</label><input name="code" required /><label for="dish">Name</label><input name="dish" required /><label for="price">Price</label><input name="price" required />');
    
    add_item.addEventListener("click", document.body.insertAdjacentElement(fragment, document.body.childNodes[8]));
});

function leftPad(str, len, ch){
    return new Array(len - str.length).fill(!ch && ch !== 0 ? ' ':
    ch).join("") + str

};