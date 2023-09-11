#!/usr/bin/node

const value = parseInt(process.argv[2]);

function factorial (n) {
  if (!n) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(value));
