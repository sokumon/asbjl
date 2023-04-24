// var name = document.getElementById("login").innerText(firstname)




fetch(window.location.origin + "/getmynotes", {
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
    .then(json =>drawmynotes(json))
var uploads = document.getElementById("mynotes")
function drawmynotes(json){
    for(let i=0;i<json.length;i++){
        var header = document.createElement("a")
       
        // header.setAttribute("style","display:none")
        header.setAttribute("onclick","clicked(this)")
        header.setAttribute("class","w3-text-brown uploads")
        header.setAttribute("href","/reader?name="+json[i].FILENAME)
        // header.innerHTML = json[i].content_posts
        // console.log(json[i].content_posts)
        header.innerText = json[i].FILENAME
        uploads.appendChild(header)
        var linebreak = document.createElement("br")
        uploads.append(linebreak)
    }
}