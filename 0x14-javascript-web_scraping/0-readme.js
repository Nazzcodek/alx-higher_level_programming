#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];

fs.readFile(path, 'utf8', (err, content) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
