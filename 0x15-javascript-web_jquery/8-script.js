$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    for (let movie of data['results']) {
      $('UL#list_movies').append('<LI>' + movie['title'] + '</LI>');
    }
  });
});
  