#!/usr/bin/node

const request = require('request');

const path = process.argv[2];

request.get(path, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
