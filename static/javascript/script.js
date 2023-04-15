// Add click handler for the delete button in the new row
$(document).on('click', '.delete-row', function() {
    $(this).closest('tr').remove();
  });

  