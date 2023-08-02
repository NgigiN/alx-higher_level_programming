// script that updates the text of the <header>
// to "New Header!!!" when the user clicks DIV#update_header
// can't use document.querySelector
// must use JQuery API

$(document).ready(function () {
	$('DIV#update_header').click(function () {
		$('header').text("New Header!!!");
	});
});