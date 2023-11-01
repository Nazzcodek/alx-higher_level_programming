$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Update the content of DIV#hello with the value of data.hello
    $('DIV#hello').text(data.hello);
  });
});