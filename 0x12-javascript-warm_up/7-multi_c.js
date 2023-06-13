#!/usr/bin/node
// const { argv } = require('node:process');

let i = 0;
const myString = 'C is fun';

if (Number(process.argv[2]) === parseInt(process.argv[2])) {
  while (i < process.argv[2]) {
    console.log(myString);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
