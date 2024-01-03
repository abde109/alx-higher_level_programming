#!/usr/bin/node

const request = require('request');
const api = 'https://swapi.dev/api/films/' + process.argv[2];

function fetch (api) {
  return new Promise((resolve, reject) => {
    request(api, { json: true }, (err, response, body) => {
      if (err) reject(err);
      resolve(body);
    });
  });
}

fetch(api).then(movie => {
  const character = movie.characters.map(Url => fetch(Url));

  character.reduce((prev, curr) => {
    return prev.then(() => curr.then(character => {
      console.log(character.name);
    }));
  }, Promise.resolve());
}).catch(err => console.error(err));
