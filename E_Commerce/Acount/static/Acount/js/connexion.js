const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.querySelector('.container');
const signUpForm = document.getElementById('signUpForm');
const signInForm = document.getElementById('signInForm');
const signUpError = document.getElementById('signUpError');
const signInError = document.getElementById('signInError');

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});

signUpForm.addEventListener('submit'), (event) => {
    event.preventDefault('submit');
    const name = document.getElementById('signupName').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
}

document.getElementById('showSignUp').addEventListener('click', function() {
    document.querySelector('.sign-up-container').style.display = 'block';
    document.querySelector('.sign-in-container').style.display = 'none';
});
