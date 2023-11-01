$(document).ready(function() {
  $('INPUT#btn_translate').click(function() {
    // Fetch the language code from the input field
    const languageCode = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      $('DIV#hello').text(data.hello);
    });
  });
});