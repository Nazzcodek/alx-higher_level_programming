#!/usr/bin/node

const arg = process.argv[2];
const value = parseInt(process.argv[2], 10);
if (arg && value) {
 for (let i = 0; i < arg; i++) {
      console.log('X'.repeat(arg));
 }
} else {
  console.log('Not a number');
}
