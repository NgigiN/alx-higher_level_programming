#!/usr/bin/node

function add (arg1, arg2) {
  if (isNaN(arg1) || isNaN(arg2)) {
    console.log('Nan');
  } else {
    console.log(parseInt(arg1) + parseInt(arg2));
  }
}

if (process.argv.length === 4) {
  add(process.argv[2], process.argv[3]);
} else {
  console.log('Nan');
}
