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
    const getCharacterName = (character) => {
      return new Promise((resolve, reject) => {
        request.get(character, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const name = JSON.parse(body).name;
            resolve(name);
          }
        });
      });
    };

    Promise.all(characters.map(getCharacterName))
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(err => {
        console.error(err);
      });
  }
});
