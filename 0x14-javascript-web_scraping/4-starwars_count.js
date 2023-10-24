#!/usr/bin/node

const request = require('request');

const api = process.argv[2];

request.get(api, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    if (res.statusCode === 200) {
      const wedge = 18;
      let count = 0;
      const films = JSON.parse(body).results;
      for (const film of films) {
        for (const character of film.characters) {
          if (character.includes(wedge)) {
            count++;
          }
        }
      }
      console.log(count);
    }
  }
});
