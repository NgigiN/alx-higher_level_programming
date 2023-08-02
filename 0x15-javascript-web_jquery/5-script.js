// script that adds a <li> element toa list when
// the user clicks on the tac DIV#add_item
// can't use document.querySelector
// must use JQuery API
// new element must be: <li>Item</li>
// new element must be added to UL.my_list

$(document).ready(function () {
	$('DIV#add_item').on('click', function () {
		$('UL.my_list').append('<li>Item</li>');
	})
})
