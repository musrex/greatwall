import React, { useState } from 'react';
import axios from 'axios';

const MenuItemForm = () => {
    const [item, setItem] = useState({
        author_id: '',
        category: '',
        code: '',
        dish: '',
        price: '',
    });

const handleChange = (e) => {
    setItem({
        ...item,
        [e.target.name]: e.target.value
    });
};

const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('/api/menu/', item)
        .then(response => {
            // handle success
            console.log(response);
        })
        .catch(error => {
            // handle error
            console.log(error);
        });
    };

return (
    <form onSubmit={handeSubmit}>
        <input type="text" name="author_id" value={item.author_id} onChange={handleChange} placeholder='Author ID'/>
        <input type="text" name="category" value={item.category} onChange={handleChange} placeholder='Category'/>
        <input type="text" name="code" value={item.code} onChange={handleChange} placeholder='Code'/>
        <input type="text" name="dish" value={item.dish} onChange={handleChange} placeholder='Dish'/>
        <input type="text" name="price" value={item.price} onChange={handleChange} placeholder='Price'/>
        <button type="submit">Submit</button>
        
    </form>
)


// Select the div element with 'app' id
const header = document.getElementById('header');
const menu = document.getElementById('menu');

function Header() {
    return (
        <div>
            <div id="mast">
                <h1><img id="logo"
                src="static/greatwall.svg"
                alt="Great Wall"/>
                </h1>
                <h2>Cantonese & Szechuan Cuisine</h2>
                <p><img src="static/greatwall.png"></img></p>
            </div>

            <div id="address">
                <p>EAT IN OR TAKE OUT</p>
                <p>FOR ORDERS TO GO</p>
                <p>5 Central Street,</p>
                <p>Baldwinville, MA 01436</p>
            </div>

            <div id="call">
                <p id="please-call">PLEASE CALL</p>
                <p>Tel.: <a href="tel:9789398600">(978) 939-8600</a></p>
                <p><a href="tel:9789398200">(978) 939-8200</a></p>
            </div>

            <div id="party">
                <p>Party & Catering welcome!</p>
            </div>

            <div id="hours">
                <p>OPEN HOURS</p>
                <p>Mon - Thu 11 AM-9:30 PM</p>
                <p>Fri - Sat 11 AM-10 PM</p>
                <p>Sun 11 AM-9:30 PM</p>
            </div>
        </div>
);
    };

function MenuMaker() {
    console.log("Hi! :)");
    return (
        <article class="boxes">
        <h1>Menu Maker</h1>
        <form id="maker" method="post">
            <label for="category">Menu Title</label>
            <input name="category" id="category" />
            
                
                
                
                <label for="code">Code</label>
                <input name="code" required />
                <label for="dish">Name</label>
                <input name="dish" required />
                <label for="price">Price</label>
                <input name="price" required />
                <div id="item_container">

                </div>

                <input type="submit" value="save" />
        </form>
        </article>
    );
};

ReactDOM.render(<Header/>, header);
