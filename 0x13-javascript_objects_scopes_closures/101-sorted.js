#!/usr/bin/node

const dict1 = require('./101-data.js').dict;

const newDict = {};

for (const [userId, occurrence] of Object.entries(dict1)) {
  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }

  newDict[occurrence].push(userId);
}

console.log(newDict);
