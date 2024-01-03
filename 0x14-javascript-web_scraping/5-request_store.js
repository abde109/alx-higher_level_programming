#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const api = process.argv[2];
const file = process.argv[3];

const writeToFile = (data) => {
  fs.writeFile(file, data, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
};

request(api, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    writeToFile(body);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
