function validateEmail() {
  var x = document.forms["myForm"]["zename"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
