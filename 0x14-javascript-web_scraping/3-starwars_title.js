#!/usr/bin/node

const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request.get(api + id, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    if (res.statusCode === 200) {
      const film = JSON.parse(body);
      console.log(`${film.title}`);
    }
  }
});
