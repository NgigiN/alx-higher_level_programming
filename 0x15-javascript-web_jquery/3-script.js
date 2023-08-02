// script that adds the class red to the <header> when the
// user clicks on the tag DIV#red_header
// can't use document.querySelector
// must use JQuery API

$(document).ready(function () {
	// Attach a click event handler to the DIV#red_header element
	$('#red_header').on('click', function () {
		// Find the <header> element and add the class "red" to it
		$('header').addClass('red');
	});
});
