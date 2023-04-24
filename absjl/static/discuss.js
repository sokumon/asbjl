console.log("hello");
console.log("Hello")
var cate = document.getElementById("categories")
var posts= document.getElementById("posts")
var content = document.getElementById("content")
var threadid = document.getElementById("threadid")
var makePost = document.getElementById("makePost")
var plussign = document.getElementById("plussign")


function putCategory(json){
    for(let i=0;i<json.length;i++){
        var header = document.createElement("div")
        header.setAttribute("id",i)
        header.setAttribute("onclick","clicked(this)")
        header.innerHTML = json[i].name
        cate.appendChild(header)
    }
} 
// div class ="Soham" 
// div class = "SOham" 

function drawposts(json){
    for(let i=0;i<json.length;i++){
        var header = document.createElement("div")
        header.setAttribute("class",json[i].thread_id)
        header.setAttribute("style","display:none")
        header.setAttribute("onclick","clickedposts(this)")
        
        header.innerHTML = json[i].content_posts
        console.log(json[i].content_posts)
        posts.appendChild(header)
    }
}
// function createposts(json){
//     for(let i=0;i<json.length;i++){
//         var header = document.createElement("h1")
//         header.setAttribute("id",i)
//         header.setAttribute("onclick","clicked(this)")
//         header.innerHTML = json[i].name
//         cate.appendChild(header)
//     }
// } 

// function putCategory(json){
//     for(let i=0;i<json.length;i++){
//         var header = document.createElement("h1")
//         header.setAttribute("id",i)
//         header.setAttribute("onclick","clicked(this)")
//         header.innerHTML = json[i].name
//         cate.appendChild(header)
//     }
// } 
// tereko aur tin fucntion likhne padhenege 
// to shpw threads cetorgies 
// clicked style.display
function clicked(element){
    // Let us focus
    // <h1 onclick="clicked(this)"id="XYZ" class="ABC">
    if(plussign.classList.contains("w3-hide")){
        plussign.classList.remove("w3-hide")
        plussign.classList.add("w3-show")
    }else{
        plussign.classList.add("w3-hide")
        plussign.classList.remove("w3-show")
    }
    console.log(parseInt(element.id) + 1)
    threadid.value = parseInt(element.id) + 1
    // console.log(posts.children[0].getAttribute("class"))
    // go to browae and relo
    for(let i=0;i<posts.children.length;i++){

        if (parseInt(posts.children[i].getAttribute("class")) == (parseInt(element.id) + 1)){
            posts.children[i].style.display = "block"
            console.log(posts.children[i].style.display)
        }else{
            posts.children[i].style.display = "none"
        }
    }
}

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
    .then(json =>putCategory(json))
// tu hai kya????
fetch(window.location.origin + "/getposts", {

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
    .then(json =>drawposts(json))    

////////////////////////////////////////////////////////////////////////////////////////////////////
////////////***create new posts */    
document.getElementById("add-comment").addEventListener("click", function (event) {
    event.preventDefault()
  
    var content = document.getElementById("comment").value
    var thread = document.getElementById("thread").value
//     var firstname = document.getElementById("firstname").value
//     var lastname = document.getElementById("lastname").value
//     localStorage.setItem("firstname", firstname);
//     submitsignin(email_id, password, firstname, lastname)
   });
  function n_post(content) {
  
     cred = {
      content: content,
      student_id:localStorage.getItem("firstname"),
      thread_id:thread
//       password: password,
//       firstname: firstname,
//       lastname: lastname
    }
    console.log(cred)
}
//     fetch(window.location.origin + "/signup", {
  
//       // Adding method type
//       method: "POST",
  
//       // Adding body or contents to send
//       body: JSON.stringify(cred),
  
//       // Adding headers to the request
//       headers: {
//         "Content-type": "application/json; charset=UTF-8"
//       }
//     })
//       // Converting to JSON
//       .then(response => response.json())
  
//       // Displaying results to console
//       // .then(json => console.log(json))
//       .then(json => validateRegister(json))
//   }
//    function validateRegister(json){
     
//      if(json.message){
//        alert(json.message)
//      }
//      if(json.error){
//       alert(json.error)
//     }
//   }


// thoda theory time
// <input> tag
// input tag has a special type called as hidden 
// hidden can also have a value 
// clicked do
// hidden u cannot see in the UI but u can still document.getElementById
// cliceked function ko use karo


function plussignsubmit(){
    if(makePost.classList.contains("w3-hide")){
        makePost.classList.remove("w3-hide")
        makePost.classList.add("w3-show")
    }else{
        makePost.classList.add("w3-hide")
        makePost.classList.remove("w3-show")
    }
}

function createPost(){
    var cred ={
        content:content.value,
        thread_id:threadid.value,
        firstname:localStorage.getItem("firstname")
    }
    console.log(cred)
    fetch(window.location.origin + "/posts", {
  
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
      .then(json => console.log(json))

  }