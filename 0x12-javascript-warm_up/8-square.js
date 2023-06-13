#!/usr/bin/node

const sliceArgs = process.argv.slice(2);

if ((sliceArgs.length !== 1) || (isNaN(parseInt(sliceArgs[0])))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sliceArgs[0]; i++) {
    let square = '';
    for (let j = 0; j < sliceArgs[0]; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
