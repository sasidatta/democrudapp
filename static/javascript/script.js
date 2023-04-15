$(document).ready(function() {
    $('#add-student-btn').click(function() {
      var newRow = '<tr>' +
        '<td></td>' +
        '<td><input type="text" name="personid"></td>' +
        '<td><input type="text" name="lastname"></td>' +
        '<td><input type="text" name="firstname"></td>' +
        '<td><input type="text" name="address"></td>' +
        '<td><input type="text" name="city"></td>' +
        '<td><button class="btn btn-danger delete-row">Delete</button></td>' +
        '</tr>';
      $('#student-table tbody').append(newRow);
    });

// Add click handler for the delete button in the new row
$(document).on('click', '.delete-row', function() {
      $(this).closest('tr').remove();
    });
  });

  // Add submit event listener to the form
$('#student-form').submit(function(event) {
  event.preventDefault(); // Prevent the form from submitting normally
  
 // Send the form data to the server using AJAX
 $.ajax({
  type: 'POST',
  url: '/add_student',
  data: $(this).serialize(),
  success: function(response) {
    alert(response.message);
    // Clear the form and add a new empty row
    $('#student-form')[0].reset();
    var newRow = '<tr>' +
      '<td><input type="text" name="personid"></td>' +
      '<td><input type="text" name="lastname"></td>' +
      '<td><input type="text" name="firstname"></td>' +
      '<td><input type="text" name="address"></td>' +
      '<td><input type="text" name="city"></td>' +
      '<td><button class="btn btn-danger delete-row">Delete</button></td>' +
      '</tr>';
    $('#student-table tbody').empty().append(newRow);
  },
  error: function(xhr, status, error) {}