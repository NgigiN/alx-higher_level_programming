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
    for (const task of tasks) {
      if (task.completed === true) {
        if (task.userId in dict) {
          dict[task.userID] += 1;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
