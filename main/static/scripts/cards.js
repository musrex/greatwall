import { toggleCard } from './functions.js';

// On page load
document.addEventListener('DOMContentLoaded', (event) => {
    // Toggle card on click
    const cards = document.querySelectorAll('.cards');
    cards.forEach(card => {
        card.addEventListener('click', (event) => {
            console.log(event.target); // Check which element is being clicked
            toggleCard(card);
        });
    });
});
