document.addEventListener ('DOMContentLoaded', function() {
    // finding header
    const h1 = document.querySelector('h1');

    // Pasue animation by default
    h1.style.animationPlayState = 'paused';

    // Wait for button to be clicked
    document.querySelector('button').onclick = () => {
        // If animation is currently paused begin playing it
        if (h1.style.animationPlayState === 'paused') {
            h1.style.animationPlayState = 'running';
        }

        // Otherwise pause the animation
        else {
            h1.style.animationPlayState = 'paused';
        }
    }
});