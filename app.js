document
.getElementById("loginForm")
.addEventListener(

"submit",

async function(event){

event.preventDefault();

const username =
document.getElementById("username").value;

const password =
document.getElementById("password").value;

const response =
await fetch(

"/login",

{
method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

username,
password

})

}

);

const data =
await response.json();

const msg =
document.getElementById("message");

if(data.success){

msg.innerHTML =
data.message;

msg.className =
"text-green-600 mt-4 text-center";

}
else{

msg.innerHTML =
data.message;

msg.className =
"text-red-600 mt-4 text-center";

}

}

);