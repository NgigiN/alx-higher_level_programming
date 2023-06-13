#!/usr/bin/node

const i = 0;
const j = 0;
if (Number(process.argv[2]) === parseInt(process.argv[2])) {
  while (i < process.argv[2]) {
    while (j < process.argv[2]) {
      console.log('X');
      j++;
    }
    i++;
  }
} else {
  console.log('Missing size');
}
