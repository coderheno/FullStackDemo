import streamlit as st
from pathlib import Path

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Express.js Registration & Login",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# CUSTOM CSS
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -----------------------------------------
# HEADER
# -----------------------------------------

st.markdown("""
<div class="header">

<h1>CHRIST (Deemed to be University)</h1>

<h3>
Express.js Registration, Login & Dashboard
</h3>

<p>
Interactive Learning Presentation
</p>

</div>
""",unsafe_allow_html=True)

# -----------------------------------------
# TWO COLUMN LAYOUT
# -----------------------------------------

left,right=st.columns([3,2])

with left:

    st.markdown("## 🎯 Learning Objectives")

    st.markdown("""

- Understand Registration

- Understand Login

- Understand Dashboard

- Learn Client Server Communication

- Build Full Stack Application

""")

    st.markdown("---")

    st.markdown("## 📚 Modules Covered")

    st.success("1. Program Flow")

    st.success("2. Project Structure")

    st.success("3. Registration Demonstration")

    st.success("4. Login Demonstration")

    st.success("5. Dashboard")

    st.success("6. server.js")

    st.success("7. index.html")

    st.success("8. app.js")

    st.success("9. Complete Workflow")

with right:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/1055/1055687.png",
        width=250
    )

    st.info("""

Registration

↓

Login

↓

Dashboard

""")

# -----------------------------------------
# WORKFLOW
# -----------------------------------------

st.markdown("---")

st.markdown("# 🌍 Complete Workflow")

st.code("""

Student

↓

Registration

↓

Login

↓

Dashboard

""")

# -----------------------------------------
# SIDEBAR
# -----------------------------------------

st.sidebar.title("📖 Navigation")

option=st.sidebar.radio(

"Select Topic",

(

"🏠 Home",

"📘 Program Flow",

"📂 Project Structure",

"📝 Registration",

"🔐 Login",

"🖥 Dashboard",

"⚙ server.js",

"🌐 index.html",

"⚡ app.js",

"🔄 Complete Workflow"

)

)

st.sidebar.markdown("---")

st.sidebar.success("Developed for Classroom Demonstration")

# -----------------------------------------
# NEXT BUTTON
# -----------------------------------------

st.markdown("---")

col1,col2,col3=st.columns([2,3,2])

with col2:

    if st.button("Next ➜"):

        st.switch_page("pages/01_Program_Flow.py")
import streamlit as st
from pathlib import Path

# --------------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------------

st.set_page_config(
    page_title="Program Flow",
    page_icon="📘",
    layout="wide"
)

# --------------------------------------------------------
# LOAD CSS
# --------------------------------------------------------

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------------------------------------------
# HEADER
# --------------------------------------------------------

st.markdown("""
<div class="header">

<h1>Program Flow</h1>

<h3>Registration → Login → Dashboard</h3>

</div>
""",unsafe_allow_html=True)

# --------------------------------------------------------
# INTRODUCTION
# --------------------------------------------------------

st.info("""
This application follows the Client–Server Architecture.

The browser communicates with the Express.js server
using Fetch API and JSON.
""")

st.markdown("---")

# --------------------------------------------------------
# STEP 1
# --------------------------------------------------------

col1,col2=st.columns([1,3])

with col1:

    st.success("STEP 1")

with col2:

    st.subheader("📝 HTML Registration Form")

    st.code("""

User enters

• Email

• Password

↓

Click Register

""")

# --------------------------------------------------------

st.markdown("⬇")

# --------------------------------------------------------
# STEP 2
# --------------------------------------------------------

col1,col2=st.columns([1,3])

with col1:

    st.success("STEP 2")

with col2:

    st.subheader("⚡ JavaScript Fetch API")

    st.code("""

JavaScript

↓

Reads Form Values

↓

Creates Object

↓

Converts to JSON

↓

fetch()

""")

# --------------------------------------------------------

st.markdown("⬇")

# --------------------------------------------------------
# STEP 3
# --------------------------------------------------------

col1,col2=st.columns([1,3])

with col1:

    st.success("STEP 3")

with col2:

    st.subheader("🌐 Express Server")

    st.code("""

POST /register

↓

Receives JSON

↓

Stores Credentials

""")

# --------------------------------------------------------

st.markdown("⬇")

# --------------------------------------------------------
# STEP 4
# --------------------------------------------------------

col1,col2=st.columns([1,3])

with col1:

    st.success("STEP 4")

with col2:

    st.subheader("📦 JSON Response")

    st.code("""

{

success:true,

message:

"Registration Successful"

}

""",language="json")

# --------------------------------------------------------

st.markdown("⬇")

# --------------------------------------------------------
# STEP 5
# --------------------------------------------------------

col1,col2=st.columns([1,3])

with col1:

    st.success("STEP 5")

with col2:

    st.subheader("🔐 Login")

    st.code("""

Email

↓

Password

↓

Click Login

""")

# --------------------------------------------------------

st.markdown("⬇")

# --------------------------------------------------------
# STEP 6
# --------------------------------------------------------

col1,col2=st.columns([1,3])

with col1:

    st.success("STEP 6")

with col2:

    st.subheader("🖥 Dashboard")

    st.code("""

Login Successful

↓

Dashboard Opens

↓

Welcome User

""")

# --------------------------------------------------------
# COMPLETE FLOW
# --------------------------------------------------------

st.markdown("---")

st.subheader("📊 Complete Client–Server Workflow")

st.code("""

Registration Form

↓

JavaScript

↓

JSON

↓

Fetch API

↓

Express Server

↓

Validation

↓

JSON Response

↓

Browser

↓

Dashboard

""")

# --------------------------------------------------------
# KEY POINTS
# --------------------------------------------------------

st.markdown("---")

st.subheader("📌 Key Points")

st.success("""
✔ User enters credentials.
""")

st.success("""
✔ JavaScript sends data using Fetch API.
""")

st.success("""
✔ Express.js validates the request.
""")

st.success("""
✔ JSON response is returned.
""")

st.success("""
✔ Browser updates the interface.
""")

# --------------------------------------------------------
# NAVIGATION
# --------------------------------------------------------

st.markdown("---")

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Home"):

        st.switch_page("app.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/02_Project_Structure.py")

import streamlit as st
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Project Structure",
    page_icon="📂",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="header">

<h1>Project Structure</h1>

<h3>Express.js Login Application</h3>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# STEP 1
# --------------------------------------------------

st.subheader("📌 Step 1 : Create Project Folder")

st.success("""
Create a new folder

Example

ExpressLoginDemo
""")

st.code("""
ExpressLoginDemo/
""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# STEP 2
# --------------------------------------------------

st.subheader("📌 Step 2 : Open VS Code")

st.success("""
Open VS Code

↓

File

↓

Open Folder

↓

Select ExpressLoginDemo
""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# STEP 3
# --------------------------------------------------

st.subheader("📌 Step 3 : Open Terminal")

st.code("""
Terminal

↓

New Terminal
""")

st.info("""
All commands will be executed from the VS Code terminal.
""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# STEP 4
# --------------------------------------------------

st.subheader("📌 Step 4 : Initialize Node Project")

st.code("""
npm init -y
""", language="bash")

st.success("""
Creates

package.json
""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# STEP 5
# --------------------------------------------------

st.subheader("📌 Step 5 : Install Express")

st.code("""
npm install express
""", language="bash")

st.success("""
Creates

node_modules/

package-lock.json
""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# STEP 6
# --------------------------------------------------

st.subheader("📌 Step 6 : Create Folder Structure")

st.code("""

ExpressLoginDemo/

│

├── server.js

│

├── package.json

│

├── node_modules/

│

└── public/

      │

      ├── index.html

      ├── app.js

      └── dashboard.html

""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# FILE PURPOSE
# --------------------------------------------------

st.subheader("📁 Purpose of Each File")

col1,col2=st.columns(2)

with col1:

    st.info("""
📄 server.js

Express Server

API Routes

Business Logic
""")

    st.info("""
📄 package.json

Project Information

Dependencies
""")

with col2:

    st.info("""
📄 index.html

Registration

Login UI
""")

    st.info("""
📄 app.js

Fetch API

JavaScript Logic
""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# PROJECT FLOW
# --------------------------------------------------

st.subheader("📊 Project Flow")

st.code("""

Project Folder

↓

server.js

↓

public/

↓

index.html

↓

app.js

↓

Dashboard

""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# WHAT WE WILL BUILD
# --------------------------------------------------

st.subheader("🚀 What We Are Going to Build")

st.success("""
✔ Registration Page

✔ Login Page

✔ Dashboard

✔ Client–Server Communication

✔ Fetch API

✔ Express.js Server
""")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# QUICK CHECK
# --------------------------------------------------

st.subheader("📝 Quick Check")

answer = st.radio(

"Which file starts the Express Server?",

[
"index.html",
"server.js",
"app.js",
"package.json"
]

)

if st.button("Check Answer"):

    if answer=="server.js":

        st.success("✅ Correct!")

    else:

        st.error("❌ Incorrect!")

# --------------------------------------------------

st.markdown("---")

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/01_Program_Flow.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/03_Registration_Demo.py")

import streamlit as st
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Registration Demonstration",
    page_icon="📝",
    layout="wide"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="header">

<h1>Registration Demonstration</h1>

<h3>Create a New User Account</h3>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# OBJECTIVE
# --------------------------------------------------

st.info("""
🎯 Objective

Create a new account by entering an Email and Password.
The credentials will be sent to the Express.js server.
""")

st.markdown("---")

# --------------------------------------------------
# REGISTRATION FORM
# --------------------------------------------------

left, right = st.columns([1,1])

with left:

    st.subheader("📝 Registration Form")

    email = st.text_input("Email Address")

    password = st.text_input(
        "Password",
        type="password"
    )

    register = st.button("Register")

with right:

    st.subheader("📋 Registration Workflow")

    st.code("""

Enter Email

↓

Enter Password

↓

Click Register

↓

JavaScript Reads Values

↓

Creates Object

↓

JSON

↓

Fetch API

↓

Express Server

↓

Registration Successful

""")

# --------------------------------------------------
# DEMO OUTPUT
# --------------------------------------------------

if register:

    st.success("✅ Registration Successful!")

    st.balloons()

    st.code("""

{

"success":true,

"message":"Registration Successful"

}

""", language="json")

st.markdown("---")

# --------------------------------------------------
# STEP-BY-STEP PROCEDURE
# --------------------------------------------------

st.subheader("📌 Step-by-Step Procedure")

steps = [

"Open Registration Page",

"Enter Email Address",

"Enter Password",

"Click Register Button",

"JavaScript Reads Form Values",

"JavaScript Creates an Object",

"Object is Converted to JSON",

"Fetch API Sends Data",

"Express Server Receives Request",

"Credentials Stored in Server",

"Registration Successful Message Displayed"

]

for i, step in enumerate(steps, start=1):

    st.success(f"Step {i} : {step}")

# --------------------------------------------------
# FLOW
# --------------------------------------------------

st.markdown("---")

st.subheader("🌍 Complete Registration Flow")

st.code("""

Registration Form

↓

JavaScript

↓

Object

↓

JSON

↓

Fetch API

↓

Express Server

↓

Store Credentials

↓

JSON Response

↓

Registration Successful

""")

# --------------------------------------------------
# KEY FILES
# --------------------------------------------------

st.markdown("---")

st.subheader("📂 Files Used")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("""
📄 index.html

Registration Form
""")

with c2:

    st.info("""
📄 app.js

Reads Values

Calls Fetch API
""")

with c3:

    st.info("""
📄 server.js

Stores Credentials

Returns Response
""")

# --------------------------------------------------
# WHAT'S NEXT
# --------------------------------------------------

st.markdown("---")

st.warning("""
Next:

We will implement the Registration feature by creating
the Express Server (server.js).
""")

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------

st.markdown("---")

c1, c2, c3 = st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/02_Project_Structure.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/04_Server_JS.py")
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="server.js",
    page_icon="⚙",
    layout="wide"
)

# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown("""
<div class="header">

<h1>Step 1 : Create server.js</h1>

<h3>Express Server Configuration</h3>

</div>
""",unsafe_allow_html=True)

# ---------------------------------------------------------
# OBJECTIVE
# ---------------------------------------------------------

st.info("""

🎯 Objective

Create an Express Server that can receive
Registration and Login requests.

""")

st.markdown("---")

# ---------------------------------------------------------
# STEP 1
# ---------------------------------------------------------

st.subheader("Step 1 : Import Express")

left,right=st.columns([1,1])

with left:

    st.code("""

const express=require("express");

""",language="javascript")

with right:

    st.success("""

✔ Import Express Library

✔ Enables Web Server

""")

st.markdown("---")

# ---------------------------------------------------------
# STEP 2
# ---------------------------------------------------------

st.subheader("Step 2 : Create Express Application")

left,right=st.columns([1,1])

with left:

    st.code("""

const app=express();

""",language="javascript")

with right:

    st.success("""

Creates

↓

Express Application

""")

st.markdown("---")

# ---------------------------------------------------------
# STEP 3
# ---------------------------------------------------------

st.subheader("Step 3 : Server Port")

left,right=st.columns([1,1])

with left:

    st.code("""

const PORT=3000;

""",language="javascript")

with right:

    st.success("""

Application Runs

↓

http://localhost:3000

""")

st.markdown("---")

# ---------------------------------------------------------
# STEP 4
# ---------------------------------------------------------

st.subheader("Step 4 : JSON Middleware")

left,right=st.columns([1,1])

with left:

    st.code("""

app.use(express.json());

""",language="javascript")

with right:

    st.success("""

Reads

↓

Incoming JSON

↓

req.body

""")

st.markdown("---")

# ---------------------------------------------------------
# STEP 5
# ---------------------------------------------------------

st.subheader("Step 5 : Static Folder")

left,right=st.columns([1,1])

with left:

    st.code("""

app.use(

express.static("public")

);

""",language="javascript")

with right:

    st.success("""

Serves

↓

index.html

↓

app.js

↓

dashboard.html

""")

st.markdown("---")

# ---------------------------------------------------------
# VISUAL
# ---------------------------------------------------------

st.subheader("How Browser Finds HTML")

st.code("""

Browser

↓

localhost:3000

↓

public/

↓

index.html

""")

st.markdown("---")

# ---------------------------------------------------------
# FILE STRUCTURE
# ---------------------------------------------------------

st.subheader("Current Project Structure")

st.code("""

ExpressLogin/

│

├── server.js

│

├── package.json

│

└── public/

      │

      ├── index.html

      ├── app.js

      └── dashboard.html

""")

st.markdown("---")

# ---------------------------------------------------------
# QUICK RECAP
# ---------------------------------------------------------

st.subheader("Today's Progress")

st.success("✔ Express Imported")

st.success("✔ App Created")

st.success("✔ Port Configured")

st.success("✔ JSON Middleware Added")

st.success("✔ Static Folder Configured")

st.markdown("---")

# ---------------------------------------------------------
# NEXT CLASS
# ---------------------------------------------------------

st.warning("""

Next

↓

Create Registration Route

app.post("/register")

""")

# ---------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/03_Registration_Demo.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/05_Register_Route.py")
import streamlit as st
from pathlib import Path

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Registration Route",
    page_icon="📝",
    layout="wide"
)

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
<div class="header">

<h1>Step 2 : Registration Route</h1>

<h3>Create POST /register API</h3>

</div>
""",unsafe_allow_html=True)

# -------------------------------------------------------
# OBJECTIVE
# -------------------------------------------------------

st.info("""

🎯 Objective

Create a Registration API to receive

Email

Password

from the browser.

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 1
# -------------------------------------------------------

st.subheader("Step 1 : Create POST Route")

left,right=st.columns([1,1])

with left:

    st.code("""

app.post(

"/register",

(req,res)=>{

});

""",language="javascript")

with right:

    st.success("""

POST Route Created

↓

/register

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 2
# -------------------------------------------------------

st.subheader("Step 2 : Read User Inputs")

left,right=st.columns([1,1])

with left:

    st.code("""

const{

email,

password

}=req.body;

""",language="javascript")

with right:

    st.success("""

Reads

↓

Email

↓

Password

from Browser

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 3
# -------------------------------------------------------

st.subheader("Step 3 : Validate Input")

left,right=st.columns([1,1])

with left:

    st.code("""

if(

!email ||

!password

){

return res.json({

success:false

});

}

""",language="javascript")

with right:

    st.success("""

Check

↓

Empty Fields

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 4
# -------------------------------------------------------

st.subheader("Step 4 : Store Credentials")

left,right=st.columns([1,1])

with left:

    st.code("""

registeredUser.email

=

email;

registeredUser.password

=

password;

""",language="javascript")

with right:

    st.success("""

Temporary Storage

↓

Server Memory

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 5
# -------------------------------------------------------

st.subheader("Step 5 : Send JSON Response")

left,right=st.columns([1,1])

with left:

    st.code("""

res.json({

success:true,

message:

"Registration Successful"

});

""",language="javascript")

with right:

    st.success("""

Browser Receives

↓

Success Message

""")

st.markdown("---")

# -------------------------------------------------------
# REGISTRATION FLOW
# -------------------------------------------------------

st.subheader("Registration Workflow")

st.code("""

Registration Form

↓

Click Register

↓

POST /register

↓

Express Server

↓

Read Email

↓

Read Password

↓

Store in Memory

↓

JSON Response

↓

Registration Successful

""")

st.markdown("---")

# -------------------------------------------------------
# VISUAL
# -------------------------------------------------------

st.subheader("Browser Communication")

st.code("""

Browser

↓

POST /register

↓

Express

↓

Memory

↓

JSON

↓

Browser

""")

st.markdown("---")

# -------------------------------------------------------
# FILES INVOLVED
# -------------------------------------------------------

st.subheader("Files Used")

c1,c2,c3=st.columns(3)

with c1:

    st.info("""

index.html

↓

Registration Form

""")

with c2:

    st.info("""

app.js

↓

Fetch API

""")

with c3:

    st.info("""

server.js

↓

Registration Route

""")

st.markdown("---")

# -------------------------------------------------------
# TODAY'S PROGRESS
# -------------------------------------------------------

st.subheader("Today's Progress")

st.success("✔ Registration Route Created")

st.success("✔ Read Email")

st.success("✔ Read Password")

st.success("✔ Stored Credentials")

st.success("✔ JSON Response Sent")

st.markdown("---")

# -------------------------------------------------------
# NEXT
# -------------------------------------------------------

st.warning("""

Next

↓

Create Login Route

POST /login

""")

# -------------------------------------------------------
# NAVIGATION
# -------------------------------------------------------

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/04_Server_JS.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/06_Login_Route.py")

import streamlit as st
from pathlib import Path

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Login Route",
    page_icon="🔐",
    layout="wide"
)

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
<div class="header">

<h1>Step 3 : Login Route</h1>

<h3>Create POST /login API</h3>

</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# OBJECTIVE
# -------------------------------------------------------

st.info("""

🎯 Objective

Validate the Email and Password entered by the user.

If credentials are correct,

allow access to Dashboard.

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 1
# -------------------------------------------------------

st.subheader("Step 1 : Create Login Route")

left,right=st.columns(2)

with left:

    st.code("""

app.post(

"/login",

(req,res)=>{

});

""",language="javascript")

with right:

    st.success("""

POST Route

↓

/login

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 2
# -------------------------------------------------------

st.subheader("Step 2 : Read Login Credentials")

left,right=st.columns(2)

with left:

    st.code("""

const{

email,

password

}=req.body;

""",language="javascript")

with right:

    st.success("""

Read

↓

Email

↓

Password

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 3
# -------------------------------------------------------

st.subheader("Step 3 : Compare Credentials")

left,right=st.columns(2)

with left:

    st.code("""

if(

email===registeredUser.email &&

password===registeredUser.password

)

""",language="javascript")

with right:

    st.success("""

Compare

↓

Stored User

↓

Login User

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 4
# -------------------------------------------------------

st.subheader("Step 4 : Login Success")

left,right=st.columns(2)

with left:

    st.code("""

res.json({

success:true,

message:

"Login Successful"

});

""",language="javascript")

with right:

    st.success("""

Send Success

↓

Browser

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 5
# -------------------------------------------------------

st.subheader("Step 5 : Invalid Login")

left,right=st.columns(2)

with left:

    st.code("""

res.json({

success:false,

message:

"Invalid Email or Password"

});

""",language="javascript")

with right:

    st.error("""

Wrong Credentials

↓

Display Error

""")

st.markdown("---")

# -------------------------------------------------------
# LOGIN WORKFLOW
# -------------------------------------------------------

st.subheader("🔄 Login Workflow")

st.code("""

Login Form

↓

Enter Email

↓

Enter Password

↓

POST /login

↓

Express Server

↓

Compare Credentials

↓

Success / Failure

↓

JSON Response

↓

Dashboard

""")

st.markdown("---")

# -------------------------------------------------------
# BROWSER COMMUNICATION
# -------------------------------------------------------

st.subheader("🌐 Client - Server Communication")

st.code("""

Browser

↓

POST /login

↓

Express Server

↓

Validate

↓

JSON Response

↓

Browser

""")

st.markdown("---")

# -------------------------------------------------------
# FILES USED
# -------------------------------------------------------

st.subheader("📂 Files Used")

c1,c2,c3=st.columns(3)

with c1:

    st.info("""

index.html

↓

Login Form

""")

with c2:

    st.info("""

app.js

↓

Fetch API

""")

with c3:

    st.info("""

server.js

↓

Login Route

""")

st.markdown("---")

# -------------------------------------------------------
# TODAY'S PROGRESS
# -------------------------------------------------------

st.subheader("✅ Today's Progress")

st.success("✔ Login Route Created")

st.success("✔ Read Email")

st.success("✔ Read Password")

st.success("✔ Compared Credentials")

st.success("✔ Returned JSON Response")

st.markdown("---")

# -------------------------------------------------------
# WHAT HAPPENS AFTER SUCCESS?
# -------------------------------------------------------

st.warning("""

Next

↓

Redirect User

↓

Dashboard

""")

# -------------------------------------------------------
# NAVIGATION
# -------------------------------------------------------

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/05_Register_Route.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/07_Dashboard.py")

import streamlit as st
from pathlib import Path

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="🖥",
    layout="wide"
)

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
<div class="header">

<h1>Step 4 : Dashboard</h1>

<h3>Landing Page after Successful Login</h3>

</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# OBJECTIVE
# -------------------------------------------------------

st.info("""

🎯 Objective

Display the Dashboard only after
successful authentication.

""")

st.markdown("---")

# -------------------------------------------------------
# DASHBOARD PREVIEW
# -------------------------------------------------------

st.subheader("🖥 Dashboard Preview")

st.success("""

Welcome to Dashboard

""")

col1,col2,col3=st.columns(3)

with col1:

    st.metric("User","student@christuniversity.in")

with col2:

    st.metric("Status","Logged In")

with col3:

    st.metric("Server","Connected")

st.button("Logout")

st.markdown("---")

# -------------------------------------------------------
# STEP 1
# -------------------------------------------------------

st.subheader("Step 1 : Login Successful")

left,right=st.columns(2)

with left:

    st.code("""

if(data.success){

}

""",language="javascript")

with right:

    st.success("""

Server Returns

↓

success : true

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 2
# -------------------------------------------------------

st.subheader("Step 2 : Redirect User")

left,right=st.columns(2)

with left:

    st.code("""

window.location.href=

"/dashboard";

""",language="javascript")

with right:

    st.success("""

Redirect Browser

↓

Dashboard

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 3
# -------------------------------------------------------

st.subheader("Step 3 : Display Dashboard")

left,right=st.columns(2)

with left:

    st.code("""

app.get(

"/dashboard",

...

);

""",language="javascript")

with right:

    st.success("""

Express

↓

dashboard.html

""")

st.markdown("---")

# -------------------------------------------------------
# DASHBOARD WORKFLOW
# -------------------------------------------------------

st.subheader("Dashboard Workflow")

st.code("""

Login Successful

↓

JSON Response

↓

Redirect

↓

GET /dashboard

↓

Express Server

↓

dashboard.html

↓

Dashboard Displayed

""")

st.markdown("---")

# -------------------------------------------------------
# PROJECT FLOW
# -------------------------------------------------------

st.subheader("Complete Application Flow")

st.code("""

Registration

↓

Store Credentials

↓

Login

↓

Validate User

↓

Dashboard

↓

Logout

""")

st.markdown("---")

# -------------------------------------------------------
# FILES USED
# -------------------------------------------------------

st.subheader("Files Used")

c1,c2,c3=st.columns(3)

with c1:

    st.info("""

dashboard.html

↓

User Interface

""")

with c2:

    st.info("""

app.js

↓

Redirect

""")

with c3:

    st.info("""

server.js

↓

Serve Dashboard

""")

st.markdown("---")

# -------------------------------------------------------
# EXPECTED OUTPUT
# -------------------------------------------------------

st.subheader("Expected Output")

st.success("✔ Registration Successful")

st.success("✔ Login Successful")

st.success("✔ Dashboard Opens")

st.success("✔ Logout Available")

st.markdown("---")

# -------------------------------------------------------
# TODAY'S PROGRESS
# -------------------------------------------------------

st.subheader("Today's Progress")

st.success("✔ Registration Completed")

st.success("✔ Login Completed")

st.success("✔ Dashboard Created")

st.success("✔ Full Workflow Completed")

st.markdown("---")

# -------------------------------------------------------
# NEXT
# -------------------------------------------------------

st.warning("""

Next

↓

Complete Project Workflow

Registration

↓

Login

↓

Dashboard

""")

# -------------------------------------------------------
# NAVIGATION
# -------------------------------------------------------

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/06_Login_Route.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/08_Complete_Workflow.py")
import streamlit as st
from pathlib import Path

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Complete Workflow",
    page_icon="🔄",
    layout="wide"
)

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("""
<div class="header">

<h1>Complete Project Workflow</h1>

<h3>Registration → Login → Dashboard</h3>

</div>
""",unsafe_allow_html=True)

# ---------------------------------------------------
# INTRODUCTION
# ---------------------------------------------------

st.info("""

This slide summarizes the complete working
of our Express.js Application.

""")

st.markdown("---")

# ---------------------------------------------------
# COMPLETE FLOW
# ---------------------------------------------------

st.subheader("Overall Workflow")

st.code("""

Start

↓

Open Browser

↓

Registration Page

↓

Enter Email

↓

Enter Password

↓

Click Register

↓

POST /register

↓

Express Server

↓

Store Credentials

↓

Registration Successful

↓

Login Page

↓

Enter Email

↓

Enter Password

↓

POST /login

↓

Validate Credentials

↓

Login Successful

↓

GET /dashboard

↓

Dashboard

↓

Logout

↓

End

""")

st.markdown("---")

# ---------------------------------------------------
# FILE COMMUNICATION
# ---------------------------------------------------

st.subheader("Files Involved")

st.code("""

Browser

↓

index.html

↓

app.js

↓

Fetch API

↓

server.js

↓

Dashboard

""")

st.markdown("---")

# ---------------------------------------------------
# REQUEST RESPONSE
# ---------------------------------------------------

left,right=st.columns(2)

with left:

    st.subheader("Browser Sends")

    st.success("""

Email

Password

JSON

POST Request

""")

with right:

    st.subheader("Server Returns")

    st.success("""

Success

Message

JSON

Dashboard

""")

st.markdown("---")

# ---------------------------------------------------
# PROJECT FILES
# ---------------------------------------------------

st.subheader("Project Files")

st.code("""

ExpressLogin/

│

├── server.js

├── package.json

└── public/

      │

      ├── index.html

      ├── app.js

      └── dashboard.html

""")

st.markdown("---")

# ---------------------------------------------------
# EXECUTION FLOW
# ---------------------------------------------------

st.subheader("Execution Flow")

st.code("""

User

↓

HTML Form

↓

JavaScript

↓

Fetch()

↓

Express

↓

Memory

↓

JSON Response

↓

Dashboard

""")

st.markdown("---")

# ---------------------------------------------------
# EXPECTED OUTPUT
# ---------------------------------------------------

st.subheader("Expected Output")

st.success("✔ User Registered")

st.success("✔ Login Successful")

st.success("✔ Dashboard Loaded")

st.success("✔ Logout Successful")

st.markdown("---")

# ---------------------------------------------------
# LAB ACTIVITY
# ---------------------------------------------------

st.subheader("Mini Exercise")

st.info("""

Modify the project.

Add

✔ Mobile Number

✔ Confirm Password

✔ Welcome Message

""")

st.markdown("---")

# ---------------------------------------------------
# SUMMARY
# ---------------------------------------------------

st.subheader("Summary")

st.table({

"Concept":[

"HTML",

"JavaScript",

"Fetch API",

"Express",

"Registration",

"Login",

"Dashboard"

],

"Status":[

"✔",

"✔",

"✔",

"✔",

"✔",

"✔",

"✔"

]

})

st.markdown("---")

# ---------------------------------------------------
# NAVIGATION
# ---------------------------------------------------

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/07_Dashboard.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/09_Index_HTML.py")
import streamlit as st
from pathlib import Path

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="index.html",
    page_icon="🌐",
    layout="wide"
)

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown("""
<div class="header">

<h1>index.html</h1>

<h3>Registration & Login User Interface</h3>

</div>

""",unsafe_allow_html=True)

# ---------------------------------------------------------
# INTRODUCTION
# ---------------------------------------------------------

st.info("""

Purpose

Create the User Interface

• Registration Form

• Login Form

• Buttons

• Messages

""")

st.markdown("---")

# =========================================================
# PART 1
# =========================================================

st.subheader("Step 1 : HTML Boilerplate")

left,right=st.columns([1,1])

with left:

    st.code("""

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"

content="width=device-width,

initial-scale=1.0">

<title>

Registration & Login

</title>

</head>

""",language="html")

with right:

    st.success("""

Creates

↓

Basic HTML Page

""")

st.markdown("---")

# =========================================================
# PART 2
# =========================================================

st.subheader("Step 2 : Tailwind CSS")

left,right=st.columns([1,1])

with left:

    st.code("""

<script src=

"https://cdn.tailwindcss.com">

</script>

""",language="html")

with right:

    st.success("""

Loads

↓

Tailwind CSS

""")

st.markdown("---")

# =========================================================
# PART 3
# =========================================================

st.subheader("Step 3 : Registration Form")

left,right=st.columns([1,1])

with left:

    st.code("""

<form id="registerForm">

<input>

<input>

<button>

Register

</button>

</form>

""",language="html")

with right:

    st.success("""

Registration Form

↓

Email

↓

Password

↓

Register

""")

st.markdown("---")

# =========================================================
# PART 4
# =========================================================

st.subheader("Step 4 : Login Form")

left,right=st.columns([1,1])

with left:

    st.code("""

<form id="loginForm">

<input>

<input>

<button>

Login

</button>

</form>

""",language="html")

with right:

    st.success("""

Login Form

↓

Email

↓

Password

↓

Login

""")

st.markdown("---")

# =========================================================
# PART 5
# =========================================================

st.subheader("Step 5 : Connect JavaScript")

left,right=st.columns([1,1])

with left:

    st.code("""

<script

src="app.js">

</script>

""",language="html")

with right:

    st.success("""

Loads

↓

JavaScript File

""")

st.markdown("---")

# =========================================================
# COMPLETE STRUCTURE
# =========================================================

st.subheader("Complete Structure")

st.code("""

HTML

↓

Head

↓

Tailwind

↓

Registration Form

↓

Login Form

↓

app.js

""")

st.markdown("---")

# =========================================================
# EXPECTED OUTPUT
# =========================================================

st.subheader("Expected Output")

st.success("✔ Registration Form")

st.success("✔ Login Form")

st.success("✔ Responsive UI")

st.success("✔ Connected with app.js")

st.markdown("---")

# =========================================================
# FILE RELATIONSHIP
# =========================================================

st.subheader("Relationship")

st.code("""

index.html

↓

User Interface

↓

app.js

↓

Fetch API

↓

server.js

""")

st.markdown("---")

# =========================================================
# NAVIGATION
# =========================================================

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/08_Complete_Workflow.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/10_App_JS.py")
import streamlit as st
from pathlib import Path

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="app.js",
    page_icon="⚡",
    layout="wide"
)

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown("""
<div class="header">

<h1>app.js</h1>

<h3>Client Side JavaScript</h3>

</div>
""",unsafe_allow_html=True)

# ---------------------------------------------------------
# OBJECTIVE
# ---------------------------------------------------------

st.info("""

🎯 Objective

Read user input

↓

Send request to Express

↓

Receive response

↓

Redirect to Dashboard

""")

st.markdown("---")

# =========================================================
# STEP 1
# =========================================================

st.subheader("Step 1 : Add Event Listener")

left,right=st.columns([1,1])

with left:

    st.code("""

document

.getElementById(

"registerForm"

)

.addEventListener(

"submit",

registerUser

);

""",language="javascript")

with right:

    st.success("""

Detects

↓

Register Button Click

""")

st.markdown("---")

# =========================================================
# STEP 2
# =========================================================

st.subheader("Step 2 : Prevent Page Refresh")

left,right=st.columns([1,1])

with left:

    st.code("""

event

.preventDefault();

""",language="javascript")

with right:

    st.success("""

Stops

↓

Page Refresh

""")

st.markdown("---")

# =========================================================
# STEP 3
# =========================================================

st.subheader("Step 3 : Read Form Values")

left,right=st.columns([1,1])

with left:

    st.code("""

const email=

document

.getElementById(

"regEmail"

).value;

const password=

document

.getElementById(

"regPassword"

).value;

""",language="javascript")

with right:

    st.success("""

Reads

↓

Email

↓

Password

""")

st.markdown("---")

# =========================================================
# STEP 4
# =========================================================

st.subheader("Step 4 : Create JavaScript Object")

left,right=st.columns([1,1])

with left:

    st.code("""

{

email,

password

}

""",language="javascript")

with right:

    st.success("""

Create

↓

JavaScript Object

""")

st.markdown("---")

# =========================================================
# STEP 5
# =========================================================

st.subheader("Step 5 : Convert Object to JSON")

left,right=st.columns([1,1])

with left:

    st.code("""

JSON.stringify({

email,

password

})

""",language="javascript")

with right:

    st.success("""

Object

↓

JSON

""")

st.markdown("---")

# =========================================================
# STEP 6
# =========================================================

st.subheader("Step 6 : Send Request")

left,right=st.columns([1,1])

with left:

    st.code("""

await fetch(

"/register",

{

method:"POST",

headers:{

"Content-Type":

"application/json"

},

body:

JSON.stringify({

email,

password

})

}

);

""",language="javascript")

with right:

    st.success("""

Browser

↓

Express

""")

st.markdown("---")

# =========================================================
# STEP 7
# =========================================================

st.subheader("Step 7 : Read Response")

left,right=st.columns([1,1])

with left:

    st.code("""

const data=

await response

.json();

""",language="javascript")

with right:

    st.success("""

Reads

↓

JSON Response

""")

st.markdown("---")

# =========================================================
# STEP 8
# =========================================================

st.subheader("Step 8 : Redirect")

left,right=st.columns([1,1])

with left:

    st.code("""

window.location.href=

"/dashboard";

""",language="javascript")

with right:

    st.success("""

Login Success

↓

Dashboard

""")

st.markdown("---")

# =========================================================
# COMPLETE FLOW
# =========================================================

st.subheader("Complete app.js Flow")

st.code("""

Click Register

↓

Event Listener

↓

preventDefault()

↓

Read Values

↓

JavaScript Object

↓

JSON.stringify()

↓

Fetch API

↓

Express Server

↓

JSON Response

↓

Dashboard

""")

st.markdown("---")

# =========================================================
# FILE RELATIONSHIP
# =========================================================

st.subheader("How app.js Communicates")

st.code("""

index.html

↓

app.js

↓

Fetch API

↓

server.js

↓

Dashboard

""")

st.markdown("---")

# =========================================================
# SUMMARY
# =========================================================

st.subheader("Summary")

st.success("✔ Event Listener")

st.success("✔ Read Form Values")

st.success("✔ JavaScript Object")

st.success("✔ JSON.stringify()")

st.success("✔ Fetch API")

st.success("✔ JSON Response")

st.success("✔ Dashboard Redirect")

st.markdown("---")

# =========================================================
# NAVIGATION
# =========================================================

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/09_Index_HTML.py")

with c3:

    if st.button("Next ➜"):

        st.switch_page("pages/11_Server_JS_Complete.py")
import streamlit as st
from pathlib import Path

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Run the Project",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------------------------------
# LOAD CSS
# -------------------------------------------------------

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.markdown("""
<div class="header">

<h1>Run the Express Application</h1>

<h3>Registration → Login → Dashboard</h3>

</div>
""",unsafe_allow_html=True)

# -------------------------------------------------------
# STEP 1
# -------------------------------------------------------

st.subheader("Step 1 : Open Terminal")

st.code("""

Terminal

↓

New Terminal

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 2
# -------------------------------------------------------

st.subheader("Step 2 : Install Express")

st.code("""

npm install express

""",language="bash")

st.markdown("---")

# -------------------------------------------------------
# STEP 3
# -------------------------------------------------------

st.subheader("Step 3 : Start Server")

st.code("""

npm start

""",language="bash")

st.success("""

Server Started Successfully

http://localhost:3000

""")

st.markdown("---")

# -------------------------------------------------------
# STEP 4
# -------------------------------------------------------

st.subheader("Step 4 : Open Browser")

st.code("""

http://localhost:3000

""")

st.success("""

Registration Page Opens

""")

st.markdown("---")

# -------------------------------------------------------
# DEMO FLOW
# -------------------------------------------------------

st.subheader("Live Demonstration")

st.code("""

Registration

↓

Registration Successful

↓

Login

↓

Login Successful

↓

Dashboard

↓

Logout

""")

st.markdown("---")

# -------------------------------------------------------
# EXPECTED TERMINAL
# -------------------------------------------------------

st.subheader("Expected Terminal Output")

st.code("""

====================================

Express Server Started Successfully

Server Running at:

http://localhost:3000

====================================

New User Registered

Email : student@gmail.com

Password : ******

------------------------------------

Login Successful

Email : student@gmail.com

------------------------------------

""")

st.markdown("---")

# -------------------------------------------------------
# PROJECT STRUCTURE
# -------------------------------------------------------

st.subheader("Project Structure")

st.code("""

ExpressLogin/

│

├── server.js

├── package.json

└── public/

      │

      ├── index.html

      ├── app.js

      └── dashboard.html

""")

st.markdown("---")

# -------------------------------------------------------
# COMPLETE EXECUTION FLOW
# -------------------------------------------------------

st.subheader("Execution Flow")

st.code("""

Open Browser

↓

Registration

↓

Express Server

↓

Store Credentials

↓

Login

↓

Validate Credentials

↓

Dashboard

↓

Logout

""")

st.markdown("---")

# -------------------------------------------------------
# CHECKLIST
# -------------------------------------------------------

st.subheader("Checklist")

st.checkbox("Project Folder Created")

st.checkbox("Express Installed")

st.checkbox("Server Running")

st.checkbox("Registration Working")

st.checkbox("Login Working")

st.checkbox("Dashboard Working")

st.checkbox("Logout Working")

st.markdown("---")

# -------------------------------------------------------
# QUICK TROUBLESHOOTING
# -------------------------------------------------------

st.subheader("Common Issues")

st.table({

"Issue":[

"Cannot GET /",

"Fetch Failed",

"Port Busy",

"Page Not Found",

"Invalid Login"

],

"Solution":[

"Check index.html",

"Check app.js",

"Restart Server",

"Check Route",

"Register First"

]

})

st.markdown("---")

# -------------------------------------------------------
# FINAL SUMMARY
# -------------------------------------------------------

st.subheader("Project Completed")

st.success("✔ Registration")

st.success("✔ Login")

st.success("✔ Dashboard")

st.success("✔ Express Server")

st.success("✔ Fetch API")

st.success("✔ Client-Server Communication")

st.markdown("---")

# -------------------------------------------------------
# NAVIGATION
# -------------------------------------------------------

c1,c2,c3=st.columns([2,3,2])

with c1:

    if st.button("⬅ Previous"):

        st.switch_page("pages/10_App_JS.py")

with c3:

    if st.button("Finish ✅"):

        st.balloons()

        st.success("Congratulations! Express.js Project Completed.")
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Expected Output",
    page_icon="✅",
    layout="wide"
)

with open(BASE_DIR / "styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<div class="header">

<h1>Expected Output</h1>

<h3>Registration → Login → Dashboard</h3>

</div>
""",unsafe_allow_html=True)

st.success("After completing the project, the following output should be observed.")

st.markdown("---")

st.subheader("Output 1 : Registration")

st.code("""

Enter Email

↓

Enter Password

↓

Click Register

↓

Registration Successful

""")

st.markdown("---")

st.subheader("Output 2 : Login")

st.code("""

Enter Registered Email

↓

Enter Password

↓

Click Login

↓

Login Successful

""")

st.markdown("---")

st.subheader("Output 3 : Dashboard")

st.code("""

Welcome User

↓

Dashboard Opens

↓

Logout Button

""")

st.markdown("---")

st.subheader("Application Flow")

st.code("""

Registration

↓

Login

↓

Dashboard

↓

Logout

""")

st.markdown("---")

c1,c2,c3=st.columns([2,3,2])

with c1:
    if st.button("⬅ Previous"):
        st.switch_page("pages/11_Run_Project.py")

with c3:
    if st.button("Next ➜"):
        st.switch_page("pages/13_Project_Activity.py")
