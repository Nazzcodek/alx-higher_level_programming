#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const store = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    if (res.statusCode === 200) {
      fs.writeFile(store, body, 'utf8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  }
});
