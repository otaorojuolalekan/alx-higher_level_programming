#!/usr/bin/node

function add(a, b) {
    return parseInt(a) + parseInt(b);
  }
  
const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (!arg1 || !arg2) console.log(NaN);
else {
const res = add(arg1, arg2);
console.log(res);
}