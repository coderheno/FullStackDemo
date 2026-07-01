// ======================================================
// Import Express Framework
// ======================================================
console.log("***** MY NEW SERVER.JS IS RUNNING *****");
const express = require("express");

// Create Express Application

const app = express();

// Server Port

const PORT = 3000;

// ======================================================
// Middleware
// ======================================================

// Convert Incoming JSON into JavaScript Object

app.use(express.json());

// Serve Static Files from "public" Folder

app.use(express.static("public"));

// ======================================================
// Temporary User Storage (No Database)
// ======================================================

let registeredUser = {

    email: "",

    password: ""

};

// ======================================================
// Registration Route
// ======================================================

app.post("/register", (req, res) => {

    // Read Registration Details

    const { email, password } = req.body;

    // Check Empty Fields

    if (!email || !password) {

        return res.json({

            success: false,

            message: "Please enter both Email and Password."

        });

    }

    // Store Credentials Temporarily

    registeredUser.email = email;

    registeredUser.password = password;

    console.log("------------------------------------");
    console.log("New User Registered");
    console.log("Email :", registeredUser.email);
    console.log("Password :", registeredUser.password);
    console.log("------------------------------------");

    // Send Response

    res.json({

        success: true,

        message: "✅ Registration Successful!\n\nYour credentials have been stored temporarily in the Express Server Memory.\n\nYou can now login using the same Email and Password."

    });

});

// ======================================================
// Login Route
// ======================================================

app.post("/login", (req, res) => {

    // Read Login Details

    const { email, password } = req.body;

    // Check Credentials

    if (

        email === registeredUser.email &&

        password === registeredUser.password

    ) {

        console.log("------------------------------------");
        console.log("Login Successful");
        console.log("Email :", email);
        console.log("------------------------------------");

        res.json({

            success: true,

            message: "Login Successful."

        });

    }

    else {

        console.log("------------------------------------");
        console.log("Invalid Login Attempt");
        console.log("------------------------------------");

        res.json({

            success: false,

            message: "Invalid Email or Password."

        });

    }

});

// ======================================================
// Dashboard Route
// ======================================================

app.get("/dashboard", (req, res) => {

    res.sendFile(__dirname + "/public/dashboard.html");

});

// ======================================================
// Home Route
// ======================================================

app.get("/", (req, res) => {

    res.sendFile(__dirname + "/public/index.html");

});

// ======================================================
// Start Server
// ======================================================
const listEndpoints = require("express-list-endpoints");

console.log(listEndpoints(app));
app.listen(PORT, () => {

    console.log("=========================================");
    console.log("Express Server Started Successfully");
    console.log("Server Running at:");
    console.log("http://localhost:3000");
    console.log("=========================================");

});