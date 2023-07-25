#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (err, response, body) {
	if (err) {
		return console.log(err);
	}
	const films = JSON.parse(body).results;
	for (const film of films) {
		for (const character of film.characters) {
			if (character.endsWith('/18/')) {
				count++;
			}
		}
	}
	console.log(count);
}
);
