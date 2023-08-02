// script that fetches and lists the title for all
// movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// all titles must be list in UL#list_movies
// can't use document.querySelector
// must use JQuery API

$(document).ready(function () {
	$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json",
		function (data) {
			data.results.forEach(function (movie) {
				$("<li>").text(movie.title).appendTo("UL#list_movies");
			});
		}
	);
});