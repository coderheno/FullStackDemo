import streamlit as st

st.set_page_config(
    page_title="React.js Essentials",
    page_icon="⚛️",
    layout="wide"
)

# ==========================================================
# TITLE
# ==========================================================

st.title("⚛️ React.js Essentials for Beginners")
st.markdown("### Module 1 : Introduction to React")
st.divider()

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.success("""
After completing this module, you will be able to:

✅ Explain why React was introduced.

✅ Describe the advantages of React over traditional JavaScript.

✅ Understand the architecture of a React application.

✅ Explain the structure of a React program.

✅ Identify the purpose of important project folders.

✅ Build your first React application.
""")

# ==========================================================
# WHY REACT
# ==========================================================

st.header("1️⃣ Why React?")

st.write("""
Modern web applications are highly interactive.
Applications such as Facebook, Instagram, Netflix and
WhatsApp continuously update information without
refreshing the entire webpage.

Developing such applications using only HTML,
CSS and JavaScript becomes increasingly difficult
as the application grows.

React was introduced to simplify the development
of dynamic and interactive user interfaces.
""")

# ==========================================================
# TRADITIONAL APPROACH
# ==========================================================

st.subheader("Traditional HTML + JavaScript")

col1,col2=st.columns(2)

with col1:

    st.code("""

<input id="name">

<button>

Submit

</button>

<h2 id="output"></h2>

""",language="html")

with col2:

    st.code("""

let name=

document.getElementById("name").value;

document.getElementById("output")

.innerHTML=name;

""",language="javascript")

st.warning("""
Every time data changes, JavaScript must manually
find HTML elements and update the page.
""")

# ==========================================================
# REACT APPROACH
# ==========================================================

st.subheader("React Approach")

st.markdown("""

```text
User Input

        ↓

State Changes

        ↓

React Updates UI Automatically

```

""")

st.success("""
React developers focus on changing the DATA.

React automatically updates the User Interface.
""")

# ==========================================================
# COMPARISON
# ==========================================================

st.header("2️⃣ HTML + JavaScript vs React")

comparison={

"Traditional JavaScript":[

"Manual DOM Manipulation",

"Large JavaScript Files",

"Repeated DOM Updates",

"Hard to Maintain",

"Suitable for Small Projects"

],

"React":[

"Automatic UI Updates",

"Component-Based",

"State Management",

"Reusable Code",

"Suitable for Large Projects"

]

}

st.table(comparison)

# ==========================================================
# WHAT IS REACT
# ==========================================================

st.header("3️⃣ What is React?")

st.info("""
React is an Open-Source JavaScript Library
used for building fast, dynamic and reusable
User Interfaces (UI).
""")

st.write("React is maintained by Meta (Facebook).")

# ==========================================================
# FEATURES
# ==========================================================

st.header("4️⃣ Features of React")

features=[

"Component-Based Architecture",

"Reusable Components",

"Virtual DOM",

"JSX",

"One-Way Data Flow",

"State Management",

"Fast Rendering",

"Easy to Maintain"

]

for f in features:

    st.write("✅",f)

# ==========================================================
# REAL WORLD
# ==========================================================

st.header("5️⃣ Applications Developed Using React")

apps={

"Application":[

"Facebook",

"Instagram",

"Netflix",

"WhatsApp Web",

"Airbnb",

"Uber Eats"

],

"Purpose":[

"Social Media",

"Photo Sharing",

"Video Streaming",

"Messaging",

"Travel Booking",

"Food Delivery"

]

}

st.table(apps)

# ==========================================================
# REACT ARCHITECTURE
# ==========================================================

st.header("6️⃣ Component-Based Architecture")

st.markdown("""

```text
Website

│

├── Header

├── Navigation

├── Content

├── Sidebar

└── Footer

```

""")

st.success("""
Each section is called a Component.

Components are independent,
reusable building blocks.
""")

# ==========================================================
# PROGRAM STRUCTURE
# ==========================================================

st.header("7️⃣ General Structure of a React Program")

st.markdown("""

```text
Import Libraries

        ↓

Create Component

        ↓

Declare State

        ↓

Write Functions

        ↓

Return JSX

        ↓

Export Component

```

""")

# ==========================================================
# SIMPLE PROGRAM
# ==========================================================

st.subheader("Example")

st.code("""

import React from "react";

function App(){

    return(

        <h1>

        Hello React

        </h1>

    );

}

export default App;

""",language="jsx")

st.info("""
Every React program follows
this basic structure.
""")

# ==========================================================
# PROJECT STRUCTURE
# ==========================================================

st.header("8️⃣ React Project Structure")

st.code("""

attendance-app/

│

├── node_modules/

├── public/

│      └── index.html

│

├── src/

│      ├── App.js

│      ├── App.css

│      └── index.js

│

├── package.json

└── package-lock.json

""")

# ==========================================================
# FOLDER EXPLANATION
# ==========================================================

st.subheader("Purpose of Important Files")

folders={

"Folder / File":[

"node_modules",

"public",

"src",

"App.js",

"App.css",

"index.js",

"package.json"

],

"Purpose":[

"Stores installed packages",

"Contains static files",

"Contains application source code",

"Main React Component",

"Application Styling",

"Entry Point",

"Project configuration"

]

}

st.table(folders)

# ==========================================================
# EXECUTION FLOW
# ==========================================================

st.header("9️⃣ How React Executes")

st.markdown("""

```text
npm start

        ↓

Development Server Starts

        ↓

index.js

        ↓

App.js

        ↓

Browser

        ↓

http://localhost:3000

```

""")

# ==========================================================
# REACT ROADMAP
# ==========================================================

st.header("🔟 React Learning Roadmap")

roadmap="""
React Introduction
        ↓
Project Structure
        ↓
JSX
        ↓
Components
        ↓
useState()
        ↓
Event Handling
        ↓
Conditional Rendering
        ↓
Attendance Application
        ↓
React Router
        ↓
API Integration
"""

st.code(roadmap)

# ==========================================================
# CLASS ACTIVITY
# ==========================================================

st.header("🎯 Individual Activity")

st.write("""
Answer the following questions:

1. Why was React introduced?

2. List four advantages of React.

3. Explain the role of Components.

4. What is the purpose of App.js?

5. Differentiate React and Traditional JavaScript.

6. Draw the React Program Structure.
""")

# ==========================================================
# THINK
# ==========================================================

st.header("💡 Think Before Next Class")

st.warning("""
Suppose you are developing an Attendance Application.

Would you prefer:

• Updating HTML manually every time a student is marked Present?

OR

• Updating only the data and allowing React
to automatically update the screen?

This question will be answered in the next module
when we learn JSX and State Management.
""")

# ==========================================================
# SUMMARY
# ==========================================================

st.success("""
✔ Why React?

✔ Features of React

✔ React Architecture

✔ Project Structure

✔ React Program Structure

✔ Execution Flow

Next Module →

JSX, Components and useState()
""")
 
st.title("⚛️ React.js Essentials")
st.subheader("Module 2A : JSX (JavaScript XML)")

st.divider()

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.success("""
After completing this module, you will be able to:

✅ Define JSX

✅ Differentiate HTML and JSX

✅ Identify JSX syntax rules

✅ Embed JavaScript expressions inside JSX

✅ Create simple JSX elements

✅ Identify common JSX errors
""")

# ==========================================================
# WHAT IS JSX
# ==========================================================

st.header("1️⃣ What is JSX?")

st.write("""
JSX stands for **JavaScript XML**.

It is a syntax extension for JavaScript that allows developers
to write HTML-like code inside JavaScript.

React uses JSX to describe the User Interface (UI).
""")

st.info("""
JSX looks like HTML,
but it is NOT HTML.

React converts JSX into JavaScript before displaying it in the browser.
""")

# ==========================================================
# WHY JSX
# ==========================================================

st.header("2️⃣ Why JSX?")

st.write("""
Without JSX, creating HTML elements in JavaScript becomes lengthy
and difficult to read.

JSX makes UI development simple, readable and maintainable.
""")

col1,col2=st.columns(2)

with col1:

    st.subheader("Without JSX")

    st.code("""

React.createElement(

"h1",

null,

"Hello React"

);

""",language="javascript")

with col2:

    st.subheader("With JSX")

    st.code("""

<h1>

Hello React

</h1>

""",language="jsx")

st.success("""
JSX makes the code easier to read and write.
""")

# ==========================================================
# HTML VS JSX
# ==========================================================

st.header("3️⃣ HTML vs JSX")

comparison={

"HTML":[

"class",

"for",

"onclick",

'style=""'

],

"JSX":[

"className",

"htmlFor",

"onClick",

"style={{ }}"

]

}

st.table(comparison)

# ==========================================================
# JSX RULES
# ==========================================================

st.header("4️⃣ Important JSX Rules")

rules=[

"Return only one parent element.",

"Close every HTML tag.",

"Use className instead of class.",

"Use htmlFor instead of for.",

"Use camelCase event names (onClick).",

"Write JavaScript inside { }."

]

for r in rules:

    st.write("✅",r)

# ==========================================================
# SINGLE ROOT ELEMENT
# ==========================================================

st.header("5️⃣ Rule : One Parent Element")

st.write("❌ Incorrect")

st.code("""

<h1>Hello</h1>

<p>Welcome</p>

""",language="jsx")

st.error("""
React Components must return only ONE parent element.
""")

st.write("✅ Correct")

st.code("""

<div>

<h1>Hello</h1>

<p>Welcome</p>

</div>

""",language="jsx")

# ==========================================================
# SELF CLOSING
# ==========================================================

st.header("6️⃣ Self Closing Tags")

st.code("""

<input />

<br />

<img />

""",language="jsx")

st.warning("""
Unlike HTML,

every tag must be properly closed.
""")

# ==========================================================
# JAVASCRIPT INSIDE JSX
# ==========================================================

st.header("7️⃣ Embedding JavaScript in JSX")

st.write("""
JavaScript expressions can be written inside curly braces { }.
""")

st.code("""

const name="Vijay";

return(

<h2>

{name}

</h2>

);

""",language="jsx")

st.success("""
Output

Vijay
""")

# ==========================================================
# LIVE DEMO
# ==========================================================

st.header("8️⃣ Interactive Demo")

name=st.text_input("Enter Your Name", key="module2a_name")

if name:

    st.success(f"Hello {name}")

st.info("""
In React,

{name}

would automatically display the entered value.
""")

# ==========================================================
# EXPRESSIONS
# ==========================================================

st.header("9️⃣ Expressions in JSX")

st.code("""

const a=10;

const b=20;

return(

<h2>

{a+b}

</h2>

);

""",language="jsx")

st.success("""
Output

30
""")

# ==========================================================
# VARIABLES
# ==========================================================

st.header("🔟 Variables")

st.code("""

const course="MCA";

return(

<p>

{course}

</p>

);

""",language="jsx")

# ==========================================================
# COMMENTS
# ==========================================================

st.header("1️⃣1️⃣ Comments in JSX")

st.code("""

{/* This is JSX Comment */}

""",language="jsx")

# ==========================================================
# INLINE STYLE
# ==========================================================

st.header("1️⃣2️⃣ Inline Styling")

st.code("""

<h1

style={{

color:"blue",

fontSize:"40px"

}}

>

Hello

</h1>

""",language="jsx")

st.warning("""
Notice

style={{ }}

Outer { }

↓

JavaScript

Inner { }

↓

Object
""")

# ==========================================================
# COMMON ERRORS
# ==========================================================

st.header("1️⃣3️⃣ Common JSX Errors")

errors={

"Error":[

"Using class",

"Using for",

"Multiple root elements",

"Unclosed tags",

"Using onclick"

],

"Correct":[

"className",

"htmlFor",

"Single Parent",

"Close Tags",

"onClick"

]

}

st.table(errors)

# ==========================================================
# THINK
# ==========================================================

st.header("🤔 Think")

st.write("""
Predict the output.
""")

st.code("""

const student="John";

return(

<h2>

Welcome {student}

</h2>

);

""",language="jsx")

answer=st.text_input("Your Prediction", key="prediction")

if answer:

    st.success("Discuss your answer with your classmates.")

# ==========================================================
# ACTIVITY
# ==========================================================

st.header("🎯 Activity")

st.write("""
Convert the following HTML into JSX.

1.

<button class="btn">

Save

</button>

2.

<label for="name">

Name

</label>

3.

<img src="logo.png">
""")

# ==========================================================
# MINI QUIZ
# ==========================================================

st.header("📝 Quick Quiz")

q=st.radio(

"Which attribute replaces 'class' in JSX?",

[

"class",

"className",

"cssClass",

"style"

]

)

if q=="className":

    st.success("✅ Correct")

# ==========================================================
# VIVA
# ==========================================================

st.header("🎤 Viva Questions")

questions=[

"What is JSX?",

"Is JSX HTML?",

"Why do we use JSX?",

"What are the rules of JSX?",

"What is the purpose of className?",

"What is htmlFor?",

"How do you write JavaScript inside JSX?",

"Why should JSX return only one parent element?"

]

for q in questions:

    st.write("•",q)

# ==========================================================
# SUMMARY
# ==========================================================

st.success("""
✔ What is JSX?

✔ Why JSX?

✔ HTML vs JSX

✔ JSX Rules

✔ Expressions

✔ Variables

✔ Comments

✔ Inline Styles

✔ Common Errors

Next Module →

Functional Components
""")
 
st.title("⚛️ React.js Essentials")
st.subheader("Module 2B : Components & React Program Structure")

st.divider()

# =====================================================
# LEARNING OUTCOMES
# =====================================================

st.header("🎯 Learning Outcomes")

st.success("""
After completing this module, students will be able to:

✅ Explain what a Component is

✅ Differentiate Web Pages and Components

✅ Understand Functional Components

✅ Explain the purpose of App()

✅ Explain return()

✅ Understand Component Hierarchy

✅ Explain React Rendering
""")

# =====================================================
# COMPONENT
# =====================================================

st.header("1️⃣ What is a Component?")

st.write("""
A Component is an independent and reusable piece of
the User Interface.

Instead of building one large webpage,
React divides the application into
small reusable blocks called Components.
""")

st.info("""
Think of Components like LEGO blocks.

Small blocks combine together
to build one complete application.
""")

# =====================================================
# REAL WORLD
# =====================================================

st.header("2️⃣ Real World Example")

st.code("""

Student Attendance System

│

├── Header

├── Attendance Form

├── Attendance Summary

└── Footer

""")

st.success("""
Each section is an independent Component.
""")

# =====================================================
# WHY COMPONENTS
# =====================================================

st.header("3️⃣ Why Components?")

comparison={

"Without Components":[

"Large HTML File",

"Difficult to Maintain",

"Code Duplication",

"Low Reusability"

],

"With Components":[

"Small Independent Files",

"Easy Maintenance",

"Reusable Code",

"Scalable Projects"

]

}

st.table(comparison)

# =====================================================
# TYPES
# =====================================================

st.header("4️⃣ Types of Components")

st.table({

"Type":[

"Functional Component",

"Class Component"

],

"Description":[

"Uses JavaScript Functions (Recommended)",

"Uses JavaScript Classes (Older Method)"

]

})

st.success("""
Modern React primarily uses Functional Components.
""")

# =====================================================
# FUNCTIONAL COMPONENT
# =====================================================

st.header("5️⃣ Functional Component")

st.code("""

function Welcome(){

    return(

        <h1>

        Welcome Students

        </h1>

    );

}

""",language="jsx")

st.write("""
A Functional Component is simply
a JavaScript function
that returns JSX.
""")

# =====================================================
# APP
# =====================================================

st.header("6️⃣ Why App()?")

st.code("""

function App(){

}

""",language="jsx")

st.write("""
App is the root (main) component.

React starts executing
from the App Component.
""")

st.markdown("""

```text

Browser

↓

index.js

↓

<App/>

↓

App()

↓

Screen
""")


st.header("7️⃣ Understanding return()")

st.write("""
Every Component must return JSX.

Whatever is written inside return()
is displayed on the browser.
""")

st.code("""

function App(){

return(

<h1>

Hello React

</h1>

);

}

""",language="jsx")

st.success("""
Output

Hello React
""")

st.header("8️⃣ Why return only ONE Parent Element?")

st.code("""

return(

<div> <h1>Hello</h1> <p>Welcome</p> </div>

)

""",language="jsx")

st.info("""
React Components
must return
one parent element.

Usually we use

<div>

or

<>

(Fragment)
""")

st.header("9️⃣ General Structure of Every React Component")

st.code("""

Import Libraries

↓

Create Component

↓

Write Logic

↓

Return JSX

↓

Export Component

""")


st.header("🔟 Complete React Program")

st.code("""

import React from "react";

function App(){

return(

    <h1>

    Hello React

    </h1>

);

}

export default App;

""",language="jsx")


st.header("1️⃣1️⃣ Line by Line Explanation")

explain=st.selectbox(

    "Choose a Line",

    [

        "import React",

        "function App()",

        "return()",

        "<h1>",

        "export default App"

    ]

)

if explain=="import React":
    st.info("Imports the React Library.")

elif explain=="function App()":
    st.info("Creates the Main React Component.")

elif explain=="return()":
    st.info("Returns JSX that will be displayed.")

elif explain=="<h1>":
    st.info("JSX Element displayed on the browser.")

elif explain=="export default App":
    st.info("Allows other files to use this Component.")

st.header("1️⃣2️⃣ Component Hierarchy")

st.code("""

App

│

├── Header

├── Menu

├── Content

└── Footer

""")

st.success("""
Components can contain
other Components.
""")

st.header("1️⃣3️⃣ Rendering")

st.write("""
Rendering means

Displaying Components
on the screen.
""")

st.markdown("""


React Starts

↓

App()

↓

return()

↓

JSX

↓

Browser


""")


st.header("1️⃣4️⃣ Mini Demo")

name=st.text_input("Enter Your Name", key="module2b_name")

if name:
    st.markdown(f"# Welcome {name}")

st.info("""
Imagine this is returned by

return()

inside App().
""")


st.header("🤔 Think")

st.write("""
Suppose we have

Header

Menu

Footer

Should we write

everything inside one file

OR

create separate Components?

Discuss with your classmates.
""")


st.header("🎯 Activity")

st.write("""

Design Components for

Hospital Management System

Food Delivery App

Movie Booking App

Library Management System

""")


st.header("📝 Quick Quiz")

q=st.radio(

"Which Component starts first?",

[

"Header",

"Footer",

"App",

"Menu"

]

)

if q=="App":
    st.success("Correct")
# =====================================================
# VIVA
# =====================================================

st.header("🎤 Viva Questions")

questions=[

"What is a Component?",

"What is a Functional Component?",

"Why do we use Components?",

"What is App()?",

"What is return()?",

"What happens if return() has two parent elements?",

"What is Rendering?",

"Why is React called Component-Based?"

]

for i in questions:
    st.write("•",i)

st.header("👥 Classroom Activity")

st.success("""

Activity:

Create the following applications
only by identifying Components.

Team-1

Attendance System

Team-2

Hospital System

Team-3

Food Delivery App

Team-4

Movie Ticket Booking

Draw the Component Hierarchy.

No coding required.

""")

st.success("""

✔ Components

✔ Functional Components

✔ App()

✔ return()

✔ Rendering

✔ Component Hierarchy

Next Module →

State (useState)

""")
 
st.title("⚛️ React.js Essentials")
st.subheader("Module 3 : State, useState() & Event Handling")

st.divider()

# =====================================================
# LEARNING OUTCOMES
# =====================================================

st.header("🎯 Learning Outcomes")

st.success("""
After completing this module, students will be able to

✅ Explain State

✅ Explain why React uses State

✅ Understand useState()

✅ Update State

✅ Explain Event Handling

✅ Explain Controlled Components

✅ Predict React Rendering
""")

# =====================================================
# INTRODUCTION
# =====================================================

st.header("1️⃣ Why Do We Need State?")

st.write("""
Suppose we display a student's name on the screen.

Initially

Name = Vijay

Later

Name = John

Question:

How will the webpage know that the name has changed?

Traditional JavaScript requires manually updating the DOM.

React automatically updates the UI using State.
""")

st.warning("""
React follows the principle

Change the DATA

↓

React updates the UI automatically.
""")

# =====================================================
# VARIABLE VS STATE
# =====================================================

st.header("2️⃣ Variable vs State")

comparison={

"JavaScript Variable":[

"Stores data",

"UI does NOT update automatically",

"Used in normal JavaScript"

],

"React State":[

"Stores data",

"UI updates automatically",

"Used in React"

]

}

st.table(comparison)

# =====================================================
# WHAT IS STATE
# =====================================================

st.header("3️⃣ What is State?")

st.info("""
State is a variable whose value can change during
the execution of the program.

Whenever State changes,

React automatically re-renders
the User Interface.
""")

# =====================================================
# EXAMPLES
# =====================================================

st.header("4️⃣ Examples of State")

states=[

"Student Name",

"Attendance Status",

"Shopping Cart",

"Login Status",

"Counter",

"Course Name",

"Age"

]

for s in states:

    st.write("✅",s)

# =====================================================
# USESTATE
# =====================================================

st.header("5️⃣ Understanding useState()")

st.code("""

const [name,setName]=

useState("");

""",language="javascript")

st.write("""
This single line creates a State Variable.
""")

# =====================================================
# BREAKDOWN
# =====================================================

st.header("6️⃣ Breaking Down useState()")

choice=st.selectbox(

"Select",

[

"name",

"setName",

'useState("")'

]

)

if choice=="name":

    st.success("""

Current Value

Example

name="Vijay"

""")

elif choice=="setName":

    st.success("""

Function used to update State

Example

setName("John")

""")

else:

    st.success("""

Initial Value

Initially Empty

""")

# =====================================================
# WORKFLOW
# =====================================================

st.header("7️⃣ State Workflow")

st.code("""

User Types

↓

onChange Event

↓

setName()

↓

State Updated

↓

React Re-renders

↓

Updated Screen

""")

# =====================================================
# DEMO
# =====================================================

st.header("8️⃣ Interactive Demo")

name=st.text_input("Enter Student Name", key="student_name")

if name:

    st.success(f"State Value : {name}")

    st.markdown(f"# Welcome {name}")

st.info("""
Imagine this value is stored
inside React State.
""")

# =====================================================
# EVENT HANDLING
# =====================================================

st.header("9️⃣ Event Handling")

events={

"Event":[

"onClick",

"onChange",

"onSubmit",

"onFocus",

"onBlur"

],

"Purpose":[

"Button Click",

"Typing",

"Form Submit",

"Input Active",

"Input Leaves"

]

}

st.table(events)

# =====================================================
# ONCHANGE
# =====================================================

st.header("🔟 onChange Event")

st.code("""

<input

value={name}

onChange={(e)=>

setName(e.target.value)

}

/>

""",language="jsx")

st.success("""
Every key press updates the State.
""")

# =====================================================
# ONCLICK
# =====================================================

st.header("1️⃣1️⃣ onClick Event")

count=st.session_state.get("count",0)

if st.button("Increase Counter"):

    count+=1

    st.session_state.count=count

st.metric("Counter",st.session_state.get("count",0))

st.write("""
React performs similar updates
using useState().
""")

# =====================================================
# CONTROLLED COMPONENT
# =====================================================

st.header("1️⃣2️⃣ Controlled Components")

st.write("""
React controls the value of every input.

Input

↓

State

↓

UI

Everything remains synchronized.
""")

st.code("""

<input

value={name}

onChange={(e)=>

setName(e.target.value)

}

/>

""",language="jsx")

# =====================================================
# RENDERING
# =====================================================

st.header("1️⃣3️⃣ React Rendering")

st.code("""

State Changes

↓

React Detects Change

↓

Component Re-renders

↓

Updated Screen

""")

# =====================================================
# THINK
# =====================================================

st.header("🤔 Think")

st.write("""
Suppose

name="John"

changes to

name="Peter"

Will React

update the screen automatically?

Why?
""")

# =====================================================
# ACTIVITY
# =====================================================

st.header("🎯 Activity")

st.success("""

Predict the output

State="Present"

↓

Click Button

↓

State="Absent"

What will happen on the screen?

""")

# =====================================================
# GROUP ACTIVITY
# =====================================================

st.header("👥 Group Activity")

st.info("""
Create a Counter Application.

Requirements

Team-1

Design using HTML + JavaScript

Team-2

Design using React

Compare

✔ Code Length

✔ Readability

✔ UI Update

✔ Maintainability

Present your findings.
""")

# =====================================================
# MCQ
# =====================================================

st.header("📝 Quick Quiz")

q=st.radio(

"What updates the UI in React?",

[

"Variables",

"State",

"Functions",

"CSS"

]

)

if q=="State":

    st.success("Correct!")

# =====================================================
# VIVA
# =====================================================

st.header("🎤 Viva Questions")

questions=[

"What is State?",

"Why do we use State?",

"What is useState()?",

"What is setName()?",

"What is the difference between Variable and State?",

"What is onChange?",

"What is Controlled Component?",

"What is Re-rendering?"

]

for i in questions:

    st.write("•",i)

# =====================================================
# SUMMARY
# =====================================================

st.success("""

✔ State

✔ useState()

✔ onChange

✔ onClick

✔ Controlled Components

✔ React Rendering

Next →

Student Attendance Application

""")
 
st.title("⚛️ React.js Essentials")
st.subheader("Module 4A : First React Application - Greeting App")

st.divider()

# -------------------------------------------------
# LEARNING OUTCOMES
# -------------------------------------------------

st.header("🎯 Learning Outcomes")

st.success("""
Students will learn

✅ useState()

✅ onChange Event

✅ Controlled Components

✅ Dynamic Rendering

✅ React Execution Flow
""")

# -------------------------------------------------
# INTRODUCTION
# -------------------------------------------------

st.header("1️⃣ Problem Statement")

st.write("""
Suppose we want to display

Hello Vijay

immediately when the user types

Vijay.

Can we achieve this without manually updating HTML?

Yes.

React does this automatically using State.
""")

# -------------------------------------------------
# OUTPUT
# -------------------------------------------------

st.header("2️⃣ Expected Output")

st.code("""

Student Name

[ Vijay ]

----------------------

Hello Vijay

""")

# -------------------------------------------------
# REACT CODE
# -------------------------------------------------

st.header("3️⃣ React Program")

st.code("""

import React,{useState} from "react";

function App(){

const [name,setName]=useState("");

return(

<div>

<input

type="text"

value={name}

onChange={(e)=>setName(e.target.value)}

/>

<h2>

Hello {name}

</h2>

</div>

);

}

export default App;

""",language="jsx")

# -------------------------------------------------
# WORKFLOW
# -------------------------------------------------

st.header("4️⃣ Execution Workflow")

st.code("""

User Types

↓

onChange Event

↓

setName()

↓

State Updated

↓

React Re-renders

↓

Hello Vijay

""")

# -------------------------------------------------
# EXPLANATION
# -------------------------------------------------

st.header("5️⃣ Line by Line Explanation")

topic=st.selectbox(

"Choose",

[

"useState",

"value",

"onChange",

"setName",

"{name}"

]

)

if topic=="useState":

    st.info("Creates State.")

elif topic=="value":

    st.info("Displays current State.")

elif topic=="onChange":

    st.info("Triggered whenever user types.")

elif topic=="setName":

    st.info("Updates the State.")

else:

    st.info("Displays the current State.")

# -------------------------------------------------
# LIVE DEMO
# -------------------------------------------------

st.header("6️⃣ Interactive Demo")

name=st.text_input("Enter Name", key="greeting_name")

if name:

    st.success(f"Hello {name}")

# -------------------------------------------------
# THINK
# -------------------------------------------------

st.header("🤔 Think")

st.write("""

Question

What happens if we remove

value={name} ?

Discuss with your friends.

""")

# -------------------------------------------------
# SUMMARY
# -------------------------------------------------

st.success("""

✔ useState()

✔ onChange()

✔ Rendering

✔ State Update

""")
