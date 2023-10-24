#!/usr/bin/node

const fs = require('node:fs');

const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
