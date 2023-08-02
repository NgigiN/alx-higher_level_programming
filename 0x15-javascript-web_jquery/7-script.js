// script that fetches the character name from a url
// the name is displayed in DIV#character
// can't use document.querySelector
// must use JQuery APi

$(document).ready(function () {
	$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
		$('DIV#character').text(data.name);
	});
});