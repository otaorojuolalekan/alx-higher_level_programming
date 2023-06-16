#!/usr/bin/node
const firstArg = process.argv[2];
const convArg = Math.floor(Number(firstArg));
if (isNaN(convArg)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < convArg; i++) {
    console.log('C is fun');
  }
}
