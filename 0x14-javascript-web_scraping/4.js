#!/usr/bin/node

const request = require('request');
const API_URL = process.argv[2];

request(API_URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const filmChars = films[film].characters;
      for (const character in filmChars) {
        if (filmChars[character].includes(18)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
