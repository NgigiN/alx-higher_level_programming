#!/usr/bin/node

function Biggy (args) {
  if (args.length === 0 || args.length === 1) {
    return 0;
  }

  args.sort((a, b) => a - b);
  return args[args.length - 2];
}

if (process.argv.length > 1) {
  console.log(`${Biggy(process.argv.slice(1))}`);
} else {
  console.log('0');
}
