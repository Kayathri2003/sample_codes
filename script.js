// Retrieve the canvas element and its context
const canvas = document.getElementById("scoreboard");
const ctx = canvas.getContext("2d");

// Set up the scoreboard properties
const score = 0;

// Function to draw the scoreboard
function drawScoreboard() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Draw the score text
  ctx.font = "24px Arial";
  ctx.fillStyle = "#000";
  ctx.fillText("Score: " + score, 10, 30);
}

// Call the drawScoreboard function to initially draw the scoreboard
drawScoreboard();
