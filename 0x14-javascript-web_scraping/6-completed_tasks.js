#!/usr/bin/node
// Script that computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const dict = {};
    const tasks = JSON.parse(body);
    for (const i of tasks) {
      if (i.completed === true) {
        if (i.userId in dict) {
          dict[i.userID] += 1;
        } else {
          diect[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
