document.getElementById("colorButton").addEventListener("click", function() {
    const colors = ["red", "green", "blue", "yellow", "purple", "orange"];
    document.body.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
});
