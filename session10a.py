import streamlit as st

st.title("⚛️ Student Attendance Application")

st.header("🎯 Objective")

st.write("""
Develop a simple Student Attendance Application using React.
""")

st.header("📚 Concepts Used")

st.write("""
- JSX
- Functional Component
- useState()
- Event Handling
- Conditional Rendering
""")

st.header("📋 Problem Statement")

st.info("""
Create a React application that allows a faculty member
to enter a student's name, select the attendance status,
and display the attendance summary after clicking Submit.
""")

st.header("🖥 Expected Output")

st.code("""
Student Attendance

Student Name

[ Vijay ]

Attendance

○ Present

○ Absent

[ Submit ]

-------------------

Attendance Summary

Student : Vijay

Status : Present

✔ Attendance Recorded
""")

st.header("⚙ Workflow")

st.code("""
User

↓

Enter Name

↓

Select Attendance

↓

Click Submit

↓

State Updated

↓

Attendance Summary Displayed
""")

st.header("💻 React Program")

st.code("""
import React,{useState} from "react";

function App(){

const [name,setName]=useState("");
const [status,setStatus]=useState("");
const [submitted,setSubmitted]=useState(false);

return(
...
);

}

export default App;
""",language="jsx")

st.success("Next Module → Code Explanation")
import streamlit as st

st.title("⚛️ React Code Explanation")

line=st.selectbox(

"Choose a Statement",

[
"import React",
"useState()",
"function App()",
"return()",
"Input Box",
"Radio Button",
"Button",
"Conditional Rendering",
"export default App"
]

)

if line=="import React":

    st.info("""
Imports the React library.
""")

elif line=="useState()":

    st.info("""
Creates State variables.

Example

const [name,setName]=useState("");
""")

elif line=="function App()":

    st.info("""
Main React Component.
""")

elif line=="return()":

    st.info("""
Returns JSX that will be displayed.
""")

elif line=="Input Box":

    st.code("""
<input

value={name}

onChange={(e)=>setName(e.target.value)}

/>
""",language="jsx")

    st.write("""
Reads the user input and updates the State.
""")

elif line=="Radio Button":

    st.write("""
Allows the user to choose
Present or Absent.
""")

elif line=="Button":

    st.write("""
Calls the Submit function.
""")

elif line=="Conditional Rendering":

    st.code("""
{submitted && (

<div>

Summary

</div>

)}
""",language="jsx")

    st.write("""
Displays the summary
only after clicking Submit.
""")

else:

    st.info("""
Exports App Component.
""")

st.divider()

st.header("🎯 Execution Flow")

st.code("""
App Starts

↓

User Types

↓

State Changes

↓

Button Click

↓

Summary Displayed
""")

st.success("Next Module → Activities")

st.title("⚛️ Activities")

st.header("👥 Group Activity")

st.success("""

Team Member-1

Develop the Attendance App using

HTML

CSS

JavaScript

------------------------

Team Member-2

Develop the same application using

React

JSX

useState()

Event Handling

""")

st.header("📊 Compare Both")

comparison={

"Feature":[

"Lines of Code",

"DOM Manipulation",

"UI Update",

"Maintainability",

"Reusability"

],

"HTML/CSS/JS":[

"", "", "", "", ""

],

"React":[

"", "", "", "", ""

]

}

st.table(comparison)

st.header("🔄 Workflow Comparison")

col1,col2=st.columns(2)

with col1:

    st.subheader("Traditional JS")

    st.code("""

User Input

↓

DOM Update

↓

Output

""")

with col2:

    st.subheader("React")

    st.code("""

User Input

↓

State Update

↓

React Re-render

↓

Output

""")

st.header("💡 Reflection")

reflection=st.radio(

"Which approach is easier to maintain?",

[

"HTML/CSS/JavaScript",

"React"

]

)

if reflection:

    st.success("Discuss your answer with your teammates.")

st.header("🎤 Viva Questions")

questions=[

"What is JSX?",

"What is State?",

"What is useState()?",

"What is Conditional Rendering?",

"Why is React faster than traditional DOM manipulation?",

"What are the advantages of Components?"

]

for q in questions:

    st.write("•",q)

st.header("📝 Mini Assignment")

st.info("""
Extend the Attendance App by adding:

✔ Register Number

✔ Course

✔ Date

✔ Reset Button
""")

st.success("""
Congratulations!

You have completed your first React application.
""")