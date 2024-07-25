// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });

document.addEventListener('DOMContentLoaded', function () {
	setTimeout(function () {
		var toasts = document.getElementsByClassName('toast_message_div');
		for (var i = 0; i < toasts.length; i++) {
			toasts[i].style.display = 'none';
		}
	}, 2000); // 5000 milliseconds = 5 seconds
});