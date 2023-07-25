#!/usr/bin/node
// Script that prints the title of a Starwars movie where the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
}
);
