const cardContaier = document.querySelector('.card-container');
let moving = false;
let transform = 0;
let mouseLastPosition = 0;
let lastPageX = 0;
let transformValue = 0;
window.addEventListener('mousedown', (e) => {
    moving = true;
    mouseLastPosition = e.pageX;
    transform = window.getComputedStyle(cardContaier)
    .getPropertyValue('transform') != 'none'
    ? window.getComputedStyle(cardContaier)
    .getPropertyValue('transform').split(',')[4].trim()
    : 0; 
    console.log(transform);
})


window.addEventListener('mousemove', (e) => {
    if (moving) {
        const diffx = e.pageX - mouseLastPosition;
        if (e.pageX - lastPageX > 0) {
            if (transformValue > 0) return;
        } else {
            if (Math.abs(transformValue) > cardContaier.offsetWidth - 320) return;
        }
        transformValue = parseInt(transform) + diffx;
        cardContaier.style.transform = `translate(${transformValue}px)`;
    }
    lastPageX = e.pageX;
});

window.addEventListener('mouseup', () => {
 moving = false;
});