#!/usr/bin/node
// Script that computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dict = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (dict[tasks[i].userId] === undefined) {
          dict[tasks[i].userId] = 1;
        } else {
          dict[tasks[i].userId]++;
        }
      }
    }
    console.log(dict);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
