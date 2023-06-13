#!/usr/bin/node
// const { argv } = require('node:process');

if (process.argv.length >= 3) {
  if (Number(process.argv[2]) === parseFloat(process.argv[2])) {
    console.log(`My number: ${process.argv[2]}`);
  } else {
    console.log('Not a number');
  }
}
