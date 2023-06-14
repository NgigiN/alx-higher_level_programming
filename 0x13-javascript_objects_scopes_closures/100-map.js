#!/usr/bin/node

const list1 = require('./100-data.js').list;

let i = -1;

const map1 = list1.map(multiply);

function multiply(element) {
  i++;
  return element * i;
}

console.log(list1);
console.log(map1);
