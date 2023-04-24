var subject = document.getElementById('subject')
var sem_no = document.getElementById('sem_dropdown')

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
    .then(json =>makeSubjectsdropdown(json))
    

sem_no.addEventListener("click",()=>{
    
})
// charging gaya wait 2min okok baba

function myFunction(){
    var allowed_subs = document.getElementsByClassName(sem_no.value)
    for(let i=0;i<allowed_subs.length;i++){
        allowed_subs[i].style.display="block"
    }
}

function makeSubjectsdropdown(json){
    for(let i=0;i<json.length;i++){   
            var options = document.createElement("option")
            options.setAttribute("value",json[i].name)
            options.setAttribute("class",json[i].sem_no)
            options.innerHTML=json[i].name
            options.style.display="none"
            subject.append(options)
    }
}

function submit(event){
  event.preventDefault()
  fetch
}