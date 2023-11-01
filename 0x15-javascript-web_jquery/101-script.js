$(document).ready(function() {
  const addElement = $('DIV#add_item').click(function() {
      $('UL.my_list').append('<LI>Item</LI>');
    });
  const removeElement = $('DIV#remove_item').click(function() {
      $('UL.my_list LI:last-child').remove();
    });
  const clearElement = $('DIV#clear_list').click(function() {
      $('UL.my_list').empty();
    });
  });
  