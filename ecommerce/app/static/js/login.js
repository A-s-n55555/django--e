// Get the form elements
var loginContainer = document.getElementById("login-container");
var signupContainer = document.getElementById("signup-container");
var signupButton = document.getElementById("signup-button");
var backButton = document.getElementById("back-button");

// Add event listener for signup button click
signupButton.addEventListener("click", showSignupForm);

// Add event listener for back button click
backButton.addEventListener("click", showLoginForm);

// Function to show the signup form
function showSignupForm() {
  // Hide the login form
  loginContainer.style.display = "none";
  
  // Show the signup form
  signupContainer.style.display = "block";
}

function showLoginForm() {
  // Hide the signup form
  signupContainer.style.display = "none";
  
  // Show the login form
  loginContainer.style.display = "block";
}
// Function to show the login form
