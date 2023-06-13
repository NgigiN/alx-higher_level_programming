#!/usr/bin/node

function add(arg1, arg2) {
  if ((arg1 === undefined) || (arg2 === undefined)) {
    console.log(`Nan`);
  } else {
    console.log(parseInt(arg1) + parseInt(arg2));
  }
}

if (process.argv.length >= 4) {
  add(process.argv[2], process.argv[3]);
} else {
  add(undefined, undefined);
}
