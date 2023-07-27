#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];

request(URL + id, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    if (response.statusCode === 200) {
      const responseJSON = JSON.parse(response.body);
      console.log(responseJSON);
    }
  }
})
;
