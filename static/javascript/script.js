function editPerson(id, lastName, firstName, address, city) {
    document.getElementById("person-id").value = id;
    document.getElementById("last-name").value = lastName;
    document.getElementById("first-name").value = firstName;
    document.getElementById("address").value = address;
    document.getElementById("city").value = city;
    document.getElementById("edit-form-container").style.display = "block";
  }
  
function closeEditForm() {
    document.getElementById("edit-form-container").style.display = "none";
  }