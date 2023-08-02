// script that updates the text color of the
// <header>  element to red (#FF0000)
// can't use JQuery API
// must must be imported from the <head> tag and
// at the end of the HTML

document.addEventListener('DOMContentLoaded', function () {
	document.querySelector('header').style.color = '#FF0000';
}
);