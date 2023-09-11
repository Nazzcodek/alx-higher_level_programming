#!/usr/bin/node

const rep = 'C is fun';
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(rep);
  }
}
