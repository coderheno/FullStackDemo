const express = require("express");

const app = express();

const PORT = 3000;

// Middleware
app.use(express.json());

app.use(express.static("public"));


// Home Route
app.get("/", (req, res) => {

    res.send(`
        <h1>🚀 Full Stack Development Server</h1>
        <p>Express Server is Running Successfully</p>
        <p>Try:</p>
        <ul>
            <li><a href="/status">Server Status</a></li>
        </ul>
    `);

});


// Status Route
app.get("/status", (req, res) => {

    res.json({
        success: true,
        message: "Server is Active",
        technology: "Express JS",
        port: PORT
    });

});


// Login Route
app.post("/login", (req, res) => {

    const { username, password } = req.body;

    if (
        username === "admin" &&
        password === "1234"
    ) {

        res.json({
            success: true,
            message: "Login Successful",
            user: username
        });

    } else {

        res.json({
            success: false,
            message: "Invalid Credentials"
        });

    }

});


// Start Server
app.listen(PORT, () => {

    console.log(
        `🚀 Server Running on http://localhost:${PORT}`
    );

});