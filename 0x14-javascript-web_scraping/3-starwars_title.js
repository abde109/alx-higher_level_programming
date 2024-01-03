#!/usr/bin/node

const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(api, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console('code' + response.statusCode);
  }
});
