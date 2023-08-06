/*
It is observed that the url given does not allow cross origin.
However this can be bypassed by using a proxy server specified below.
*/
const proxy = 'https://cors-anywhere.herokuapp.com/';

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(proxy + url, function (response) {
  const hello = response.hello;
  $('DIV#hello').text(hello);
});
