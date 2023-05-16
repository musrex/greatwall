// Select the div element with 'app' id
const header = document.getElementById('header');
const menu = document.getElementById('menu');
            
function Header({ title }) {
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
    }

function Menu({category}) {
    return (
        <div>
            <h2>{category}</h2>

        </div>
    );
}





ReactDOM.render(<Header title="Great Wall" />, header)
ReactDOM.render(<Menu category="Luncheon Special" />, menu)


function leftPad(str, len, ch){
    return new Array(len - str.lenth).fill(!ch && ch !== 0 ? ' ':
    ch).join("") + str

}