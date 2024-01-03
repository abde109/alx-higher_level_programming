#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (response, err) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
