var subjectname = document.getElementById("subjectname")
fetch(window.location.origin + "/getallsubjects", {

    // Adding method type
    method: "POST",

    // Adding body or contents to send
    // body: JSON.stringify(cred),

    // Adding headers to the request
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
    // Converting to JSON
    .then(response => response.json())

    // Displaying results to console
    .then(json => displaySubjectname(json))

function displaySubjectname(json){
    var subid = parseInt(window.location.search.split("=")[1])
    for (let i = 0; i < json.length; i++) {
        if(i == (subid-1)){
            subjectname.innerText=json[i].name
        }
        
    }
}