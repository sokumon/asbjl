console.log("Hello")
var cate = document.getElementById("categories")
var posts= document.getElementById("posts")
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
    .then(json =>makeCate(json))
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
		.then(json =>makePosts(json))
	fetch(window.location.origin + "/thread", {

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
			.then(json =>console.log(json))
function makeCate(json){
for(let i =0;i<json.length;i++){
	var link = document.createElement("p")
	link.setAttribute("onclick","clicked(this)")
	link.innerHTML=json[i].name
	cate.append(link)
}
}
function makePosts(json){
	var para= document.createElement("p")
	para.setAttribute("class",json[0].subject_posts)
	para.innerHTML= json[0].content_posts +"<br>"+ json[0].student_id
	posts.append(para)
	
}

function clicked(element){
	var classnames = document.getElementsByClassName(element.innerHTML)
	for(let i =0;i<classnames.length;i++){
		classnames[i].style.display = 'block'
	}
}
