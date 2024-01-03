#!/usr/bin/node

const request = require('request');

const api = 'https://swapi.dev/api/films/' + process.argv[2];

request(api, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach(function (characterUrl) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  } else {
    console.log('code: ' + response.statusCode);
  }
});
