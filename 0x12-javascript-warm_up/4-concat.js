#!/usr/bin/node
// const { argv } = require('node:process');

function printArguments (arg1, arg2) {
  if (arg2 === undefined) {
    console.log(`${arg1} is undefined`);
  } else {
    console.log(`${arg1} is ${arg2}`);
  }
}

if (process.argv.length > 2) {
  printArguments(process.argv[2], process.argv[3]);
} else if (process.argv.length > 1) {
  printArguments(process.argv[2], undefined);
}
