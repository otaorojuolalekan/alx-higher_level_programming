#!/usr/bin/node
const argLen = process.argv.length; // how many args?
const argList = []; // empty list for future use
if (argLen <= 3) console.log(0);
else {
  for (let i = 2; i < argLen; i++) {
    argList.push(process.argv[i]); // add each args to the list
  }
  argList.sort((a, b) => b - a); // sort in descending order
  console.log(argList[1]); // print 2nd largest -- 2nd item in list
}
