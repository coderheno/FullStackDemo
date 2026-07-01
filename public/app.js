// ======================================================
// Registration Form
// ======================================================

document
.getElementById("registerForm")
.addEventListener("submit", async function(event){

    // Prevent Page Refresh

    event.preventDefault();

    // Read Registration Details

    const email =
    document.getElementById("regEmail").value;

    const password =
    document.getElementById("regPassword").value;

    // Send Data to Express Server

    const response = await fetch("/register",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            email:email,
            password:password

        })

    });

    // Read JSON Response

    const data = await response.json();

    // Display Registration Message

    const registerMessage =
    document.getElementById("registerMessage");

    if(data.success){

        registerMessage.innerHTML = data.message;

        registerMessage.className =
        "mt-4 text-center font-bold text-green-600";

        // Popup Message

        alert(
            "Registration Successful!\n\n" +
            "Your credentials have been stored temporarily in the Express Server Memory.\n\n" +
            "Please login using the same Email and Password."
        );

        // Clear Registration Form

        document.getElementById("registerForm").reset();

        // Move Cursor to Login Email

        document.getElementById("loginEmail").focus();

    }

    else{

        registerMessage.innerHTML = data.message;

        registerMessage.className =
        "mt-4 text-center font-bold text-red-600";

    }

});


// ======================================================
// Login Form
// ======================================================

document
.getElementById("loginForm")
.addEventListener("submit", async function(event){

    // Prevent Page Refresh

    event.preventDefault();

    // Read Login Details

    const email =
    document.getElementById("loginEmail").value;

    const password =
    document.getElementById("loginPassword").value;

    // Send Login Request

    const response = await fetch("/login",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            email:email,
            password:password

        })

    });

    // Read Server Response

    const data = await response.json();

    // Display Login Message

    const loginMessage =
    document.getElementById("loginMessage");

    if(data.success){

        loginMessage.innerHTML = data.message;

        loginMessage.className =
        "mt-4 text-center font-bold text-green-600";

        alert(
            "Login Successful!\n\n" +
            "Welcome to Express.js Dashboard."
        );

        // Wait for 1 Second

        setTimeout(function(){

            window.location.href="/dashboard";

        },1000);

    }

    else{

        loginMessage.innerHTML = data.message;

        loginMessage.className =
        "mt-4 text-center font-bold text-red-600";

        alert(
            "Login Failed!\n\n" +
            "Invalid Email or Password."
        );

    }

});