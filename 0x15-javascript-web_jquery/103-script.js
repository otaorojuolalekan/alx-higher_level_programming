// 102-script.js

$(document).ready(function () {
  function keyorclick () {
    const languageCode = $('INPUT#language_code').val();

    // Check if the language code is not empty
    if (languageCode !== '') {
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${encodeURIComponent(
            languageCode
          )}`;

      // Fetch the translation from the API
      $.get(apiUrl, function (data) {
        const translation = data.hello;

        // Display the translation in the div tag
        $('#hello').text(translation);
      }).fail(function () {
      // Handle errors in case the language code is not found
        $('#hello').text('Translation not found');
      });
    }
  }
  // run on button click
  $('#btn_translate').click(keyorclick());
  // run on enter press
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      keyorclick();
    }
  });
});
