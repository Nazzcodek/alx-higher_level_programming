$(document).ready(function() {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  }
  $('#btn_translate').click(fetchTranslation);

  // Fetch translation when the user presses ENTER in the language_code input field
  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // 13 is the ENTER key
      fetchTranslation();
    }
  });
});
