#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const result = {};
    for (const i of data) {
      const userId = i.userId;

      if (i.completed) {
        if (!result[userId]) {
          result[userId] = 1;
        } else {
          result[userId]++;
        }
      }
    }
    console.log(result);
  }
});
