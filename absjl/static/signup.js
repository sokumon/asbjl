document.getElementById("submit").addEventListener("click", function (event) {
  event.preventDefault()

  var email_id = document.getElementById("email_id").value
  var password = document.getElementById("password").value
  var firstname = document.getElementById("firstname").value
  var lastname = document.getElementById("lastname").value
  localStorage.setItem("firstname", firstname);
  submitsignin(email_id, password, firstname, lastname)
});
function submitsignin(email_id, password, firstname, lastname) {

  cred = {
    email_id: email_id,
    password: password,
    firstname: firstname,
    lastname: lastname
  }
  console.log(cred)
  fetch(window.location.origin + "/signup", {

    // Adding method type
    method: "POST",

    // Adding body or contents to send
    body: JSON.stringify(cred),

    // Adding headers to the request
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
    // Converting to JSON
    .then(response => response.json())

    // Displaying results to console
    // .then(json => console.log(json))
    .then(json => validateRegister(json))
}
 function validateRegister(json){
   
   if(json.message){
     alert(json.message)
   }
   if(json.error){
    alert(json.error)
  }
 }