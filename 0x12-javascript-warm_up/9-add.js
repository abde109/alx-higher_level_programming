#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = process.argv.slice(2).map(Number);
console.log(add(args[0], args[1]));
