#!/usr/bin/node
const arg1 = process.argv[2];
const size = Math.floor(Number(arg1));
if (isNaN(size)) console.log('Missing size');
else {
  for (let r = 0; r < size; r++) {
    let row = '';
    for (let c = 0; c < size; c++) row += 'X';
    console.log(row);
  }
}
