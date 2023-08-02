//script that toggles the class of the <header>
// when the user clicks on the tag DIV#toggle_header
// can't use document.querySelector
// must use JQuery API

$(document).ready(function () {
	$('DIV#toggle_header').on('click', function () {
		$('header').toggleClass('red green');
	})
})