const canvas = document.querySelector('.canvas');
const startButton = document.querySelector('#start-button');
const circleCountInput = document.querySelector('#circle-count');

startButton.addEventListener('click', () => {
    const chosenCircleCount = parseInt(circleCountInput.value);
    startButton.disabled = true;
    canvas.innerHTML = '';
    drawCircle(canvas.clientWidth / 2, canvas.clientHeight / 2, 100, 0, chosenCircleCount);
});

function drawCircle(x, y, radius, depth, maxDepth) {
    if (depth >= maxDepth) {
        startButton.disabled = false;
		 setTimeout(() => {
            removeCircles();
        }, 2000); // Adjust the delay as needed (e.g., 2000ms for 2 seconds)
        return;
    }

    const circle = document.createElement('div');
    circle.classList.add('circle');
    circle.style.width = radius * 3 + 'px';
    circle.style.height = radius * 3 + 'px';
    circle.style.backgroundColor = getRandomColor();
    circle.style.left = x - radius + 'px';
    circle.style.top = y - radius + 'px';

    canvas.appendChild(circle);

    setTimeout(() => {
        drawCircle(x + radius / 2, y, radius / 2, depth + 1, maxDepth);
    }, 1000);
}

function removeCircles() {
    const circles = document.querySelectorAll('.circle');
    circles.forEach(circle => {
        circle.remove();
    });
}

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
