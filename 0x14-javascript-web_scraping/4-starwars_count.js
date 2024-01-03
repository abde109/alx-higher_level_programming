#!/usr/bin/node

const request = require('request');
const api = process.argv[2];
let count = 0;

request(api, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    for (const result of results) {
      for (const character of result.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
