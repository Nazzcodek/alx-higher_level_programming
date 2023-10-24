#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2] - 1;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body).results;
    const characters = data[id].characters;
    characters.forEach(character => {
      request.get(character, (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    });
  }
});
