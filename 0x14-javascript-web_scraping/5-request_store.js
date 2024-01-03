#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const api = process.argv[2];
const file = process.argv[3];

request(api, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
    console.log('code: ' + response.statusCode);
  }
});
