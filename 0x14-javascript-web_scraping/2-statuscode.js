#!/usr/bin/node

const request = require('request');

request.get(process.argv[2]).on('response', (response, err) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
