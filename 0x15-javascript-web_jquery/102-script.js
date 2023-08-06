// 102-script.js

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();

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
  });
});

