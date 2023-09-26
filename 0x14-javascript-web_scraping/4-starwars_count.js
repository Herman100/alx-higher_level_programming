#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    for (const film of data.results) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
