console.log("hello");
console.log("Hello")
var cate = document.getElementById("subjects")
var uploads = document.getElementById("subjectnotes");

function subjects(json){
    for(let i=0;i<json.length;i++){
        // var header = document.createElement("h1")
        // header.setAttribute("id",i)
        // header.setAttribute("onclick","clicked(this)")
        // header.innerHTML = json[i].name
        // cate.appendChild(header)
    }
} 
// div class ="Soham" 
// div class = "SOham" 

function drawuploads(json){
    for(let i=0;i<json.length;i++){
        var header = document.createElement("a")
       
        // header.setAttribute("style","display:none")
        header.setAttribute("onclick","clicked(this)")
        header.setAttribute("class","w3-text-brown uploads")
        header.setAttribute("href","/reader?name="+json[i].uploads)
        // header.innerHTML = json[i].content_posts
        // console.log(json[i].content_posts)
        header.innerText = json[i].uploads
        uploads.appendChild(header)
        var linebreak = document.createElement("br")
        uploads.append(linebreak)
    }
}

function clicked(element){
    // Let us focus
    // <h1 onclick="clicked(this)"id="XYZ" class="ABC">
    console.log(parseInt(element.id))
    // console.log(posts.children[0].getAttribute("class"))
    // go to browae and relo
    for(let i=0;i<posts.children.length;i++){

        if (parseInt(posts.children[i].getAttribute("class")) == (parseInt(element.id))){
            posts.children[i].style.display = "block"
            console.log(posts.children[i].style.display)
        }else{
            posts.children[i].style.display = "none"
        }
    }
}
var fil = window.location.search
var hil = fil.slice(fil.indexOf("=")+1,fil.length)
console.log(hil)
var cred = {
        subject_id:hil
}

fetch(window.location.origin + "/getuploads", {
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
    .then(json =>drawuploads(json))