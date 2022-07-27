const body = document.querySelector('#gradient'),
color1 = document.querySelector('.color1'),
color2 = document.querySelector('.color2');

function setBackgroundColor(){
    body.style.background = `linear-gradient(to left , ${color1.value} ,${color2.value})`;
}

color1.addEventListener('input', setBackgroundColor)
color2.addEventListener('input', setBackgroundColor)