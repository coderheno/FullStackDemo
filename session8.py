import streamlit as st

# -----------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------

st.set_page_config(
    page_title="Modern JavaScript & Client-Server Communication",
    page_icon="🌐",
    layout="wide"
)

# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------

st.sidebar.title("📚 Module Navigation")

st.sidebar.success("Module - 2")

st.sidebar.markdown("""
### Topics Covered

- Introduction
- JavaScript Objects
- JavaScript Forms
- Events & Event Handling
- Async Programming
- Async / Await
- Navigator Object
- Cookies
- JSON
- JSON vs XML
- Fetch API
- Express.js
- Registration & Login
- Dashboard
- MCQs
- Viva Questions
- Mini Project
""")

st.sidebar.markdown("---")

st.sidebar.markdown("## 🤖 AI Tutor")

st.sidebar.markdown("""
Need help?

Click below.
""")

st.sidebar.link_button(
    "Open AI Tutor",
    "https://fscbot.streamlit.app/"
)

st.sidebar.markdown("---")

st.sidebar.info(
"""
Faculty

Dr. Vijay Arputharaj J

Department of Computer Science

CHRIST (Deemed to be University)
"""
)

# -----------------------------------------------------
# TITLE
# -----------------------------------------------------

st.title("🌐 Modern JavaScript & Client-Server Communication")

st.subheader(
"Module 2 : Interactive Web Development using JavaScript, JSON, Fetch API and Express.js"
)

st.markdown("---")

# -----------------------------------------------------
# INTRODUCTION
# -----------------------------------------------------

col1,col2=st.columns([2,1])

with col1:

    st.markdown("""
## Welcome

Welcome to **Module 2** of the Full Stack Development Course.

In this module, you will learn how JavaScript makes web pages interactive and how browsers communicate with backend servers using modern web technologies.

By the end of this module, you will be able to build a complete Registration → Login → Dashboard application using HTML, JavaScript, JSON, Fetch API and Express.js.
""")

with col2:

    st.info("""
### Module Duration

✔ 15 Hours

✔ Theory

✔ Demonstrations

✔ Lab Exercises

✔ Mini Project
""")

# -----------------------------------------------------
# LEARNING OUTCOMES
# -----------------------------------------------------

st.markdown("---")

st.header("🎯 Learning Outcomes")

st.markdown("""
After completing this module, students will be able to:

✅ Understand JavaScript Objects

✅ Develop HTML Forms

✅ Handle JavaScript Events

✅ Implement Event Handling

✅ Understand Asynchronous Programming

✅ Use Async and Await

✅ Work with Browser Navigator APIs

✅ Manage Cookies

✅ Understand JSON

✅ Compare JSON and XML

✅ Exchange Data using Fetch API

✅ Develop Express.js Applications

✅ Build Registration & Login Systems

✅ Develop Interactive Dashboards

✅ Implement Client-Server Communication
""")

# -----------------------------------------------------
# WHY THIS MODULE
# -----------------------------------------------------

st.markdown("---")

st.header("❓ Why Learn This Module?")

st.success("""
Modern websites are interactive.

Whenever you login to Gmail, Instagram, Amazon or Moodle,
JavaScript communicates with the server behind the scenes.

This module teaches exactly how that communication happens.
""")

col1,col2,col3=st.columns(3)

with col1:

    st.metric(
        "Frontend",
        "JavaScript"
    )

with col2:

    st.metric(
        "Communication",
        "Fetch API"
    )

with col3:

    st.metric(
        "Backend",
        "Express.js"
    )

# -----------------------------------------------------
# MODULE ROADMAP
# -----------------------------------------------------

st.markdown("---")

st.header("🛣 Module Roadmap")

st.code("""
JavaScript Basics
        │
        ▼
Objects
        │
        ▼
Forms
        │
        ▼
Events
        │
        ▼
Async Programming
        │
        ▼
Async / Await
        │
        ▼
Navigator
        │
        ▼
Cookies
        │
        ▼
JSON
        │
        ▼
Fetch API
        │
        ▼
Express.js
        │
        ▼
Registration
        │
        ▼
Login
        │
        ▼
Dashboard
""")

# -----------------------------------------------------
# CLIENT SERVER ARCHITECTURE
# -----------------------------------------------------

st.markdown("---")

st.header("🌍 Client - Server Architecture")

st.code("""
Browser (Client)
        │
        │ Request
        ▼
Express Server
        │
        │ Process
        ▼
JSON Response
        │
        ▼
Browser Updates UI
""")

st.info("""
Every modern web application follows this architecture.

Examples:

• Gmail

• Facebook

• Instagram

• Banking Portal

• Amazon

• Student Portal

• Hospital Management System
""")

# -----------------------------------------------------
# REAL WORLD APPLICATIONS
# -----------------------------------------------------

st.markdown("---")

st.header("🏢 Real World Applications")

apps=[
"Student Portal",
"Hospital Management System",
"Banking Application",
"CRM System",
"Library Management",
"Food Delivery",
"E-Commerce",
"Learning Management System",
"Employee Management",
"Travel Booking"
]

c1,c2=st.columns(2)

for i in range(5):
    c1.success(apps[i])

for i in range(5,10):
    c2.success(apps[i])

# -----------------------------------------------------
# TECHNOLOGIES
# -----------------------------------------------------

st.markdown("---")

st.header("🛠 Technologies Used")

col1,col2,col3,col4=st.columns(4)

with col1:

    st.info("""
HTML5

Structure
""")

with col2:

    st.info("""
Tailwind CSS

Styling
""")

with col3:

    st.info("""
JavaScript

Logic
""")

with col4:

    st.info("""
Express.js

Backend
""")

# -----------------------------------------------------
# MINI PROJECT
# -----------------------------------------------------

st.markdown("---")

st.header("💻 Module Mini Project")

st.success("""
Registration

↓

Login

↓

Dashboard

↓

Logout

using

HTML

Tailwind CSS

JavaScript

Fetch API

JSON

Express.js
""")



# -----------------------------------------------------
# REFERENCES
# -----------------------------------------------------

st.markdown("---")

st.header("📖 References")

st.markdown("""
- MDN Web Docs

- JavaScript.info

- Express.js Documentation

- W3Schools

- Node.js Documentation

- Tailwind CSS Documentation
""")

# -----------------------------------------------------
# NEXT MODULE
# -----------------------------------------------------

st.markdown("---")

st.success("""
➡️ Next Topic

Introduction to JavaScript Objects

Continue to the next page from the sidebar.
""")
import streamlit as st

# ===========================================================
# PAGE TITLE
# ===========================================================

st.title("📦 JavaScript Objects")

st.subheader("Everything in Modern JavaScript revolves around Objects")

st.markdown("---")

# ===========================================================
# LEARNING OUTCOMES
# ===========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""
After completing this topic, you will be able to

✅ Understand JavaScript Objects

✅ Create Objects

✅ Access Object Properties

✅ Modify Object Values

✅ Add New Properties

✅ Delete Properties

✅ Understand Real-world Applications of Objects

✅ Prepare for JSON and Express.js
""")

# ===========================================================
# INTRODUCTION
# ===========================================================

st.markdown("---")

st.header("❓ What is a JavaScript Object?")

st.info("""
A JavaScript Object is a collection of related information stored as **key-value pairs**.

Instead of storing individual variables, we group related data together inside a single object.
""")

st.success("""
Think of an object as a **Digital Identity Card**.

One student has

• Name

• Register Number

• Department

• Age

• Marks

Instead of creating five separate variables,
we store everything inside one object.
""")

# ===========================================================
# WHY OBJECTS
# ===========================================================

st.markdown("---")

st.header("🤔 Why Do We Need Objects?")

st.markdown("""
Imagine storing student information.
""")

st.code("""
let name = "John";

let age = 20;

let course = "BCA";

let marks = 95;
""",language="javascript")

st.error("""
Problem

❌ Too many variables

❌ Difficult to manage

❌ Difficult to send to server
""")

st.success("""
Better Solution

Store everything inside ONE Object.
""")

st.code("""
let student={

name:"John",

age:20,

course:"BCA",

marks:95

};
""",language="javascript")

# ===========================================================
# REAL WORLD
# ===========================================================

st.markdown("---")

st.header("🌍 Real-world Examples")

col1,col2=st.columns(2)

with col1:

    st.success("""
👨 Student

Name

Age

Department

Marks
""")

    st.success("""
🛒 Product

Product Name

Price

Quantity

Category
""")

    st.success("""
👨 Employee

ID

Salary

Department
""")

with col2:

    st.success("""
🏥 Patient

Patient ID

Doctor

Disease

Age
""")

    st.success("""
🏦 Bank Account

Account Number

Balance

Customer
""")

    st.success("""
🚗 Vehicle

Vehicle Number

Owner

Model
""")

# ===========================================================
# OBJECT STRUCTURE
# ===========================================================

st.markdown("---")

st.header("🏗 Structure of an Object")

st.code("""

Object

{

Key : Value,

Key : Value,

Key : Value

}

""")

st.info("""
Every Object contains

Key

↓

Value

These are called **Properties**.
""")

# ===========================================================
# FIRST OBJECT
# ===========================================================

st.markdown("---")

st.header("🚀 Creating Your First Object")

code="""
let student={

name:"John",

age:20,

department:"Computer Science",

cgpa:8.9

};

console.log(student);
"""

st.code(code,language="javascript")

st.success("""
Output

Student Object

↓

Name : John

Age : 20

Department : Computer Science

CGPA : 8.9
""")

# ===========================================================
# VISUALIZATION
# ===========================================================

st.markdown("---")

st.header("📊 Object Visualization")

st.code("""

            Student

      -------------------

      name : John

      age : 20

      department : CS

      cgpa : 8.9

      -------------------

""")

# ===========================================================
# KEY VALUE
# ===========================================================

st.markdown("---")

st.header("🔑 Understanding Key-Value Pairs")

st.table({

"Key":[

"name",

"age",

"department",

"cgpa"

],

"Value":[

"John",

20,

"Computer Science",

8.9

]

})

st.info("""
Keys act like labels.

Values store actual information.
""")

# ===========================================================
# ACCESSING PROPERTIES
# ===========================================================

st.markdown("---")

st.header("📥 Accessing Object Properties")

st.subheader("Method 1 : Dot Notation")

st.code("""

console.log(student.name);

console.log(student.age);

console.log(student.cgpa);

""",language="javascript")

st.success("""

Output

John

20

8.9

""")

st.subheader("Method 2 : Bracket Notation")

st.code("""

console.log(student["name"]);

console.log(student["age"]);

""",language="javascript")

st.success("""

Output

John

20

""")

# ===========================================================
# DOT VS BRACKET
# ===========================================================

st.markdown("---")

st.header("⚖ Dot Notation vs Bracket Notation")

st.table({

"Dot Notation":[

"student.name",

"Easy",

"Most Common"

],

"Bracket Notation":[

'student["name"]',

"Useful for Dynamic Keys",

"Supports Variables"

]

})

# ===========================================================
# MODIFY
# ===========================================================

st.markdown("---")

st.header("✏ Updating Object Values")

st.code("""

student.cgpa=9.5;

console.log(student);

""",language="javascript")

st.success("""

CGPA Updated

Old

8.9

↓

New

9.5

""")

# ===========================================================
# ADD PROPERTY
# ===========================================================

st.markdown("---")

st.header("➕ Adding New Property")

st.code("""

student.city="Bangalore";

console.log(student);

""",language="javascript")

st.success("""

New Property Added

City : Bangalore

""")

# ===========================================================
# DELETE PROPERTY
# ===========================================================

st.markdown("---")

st.header("🗑 Deleting Properties")

st.code("""

delete student.age;

console.log(student);

""",language="javascript")

st.warning("""

Age Property Deleted

""")

# ===========================================================
# CLASS ACTIVITY
# ===========================================================

st.markdown("---")

st.header("🎯 Classroom Activity")

st.info("""
Create an object based on your selected domain.

Examples

• Student

• Hospital

• Library

• CRM

• Banking

• Tourism

• Food Delivery

Include at least

✔ 5 Properties

✔ Display 3 Properties

✔ Modify 1 Property

✔ Add 1 New Property

✔ Delete 1 Property
""")

# ===========================================================
# THINK
# ===========================================================

st.markdown("---")

st.header("🧠 Think & Discuss")

st.success("""
Suppose you are developing

• Student Portal

• CRM

• Hospital System

• Banking Application

Question

Can we manage these applications using individual variables?

OR

Should we use Objects?

Discuss with your classmates.
""")

# ===========================================================
# SUMMARY
# ===========================================================

st.markdown("---")

st.success("""
Summary

✔ JavaScript Objects store related data.

✔ Objects contain Key-Value Pairs.

✔ Properties can be Accessed.

✔ Properties can be Modified.

✔ New Properties can be Added.

✔ Existing Properties can be Deleted.

Objects are the foundation for

➡ JSON

➡ Fetch API

➡ Express.js

➡ MongoDB

➡ React

➡ MERN Stack
""")
import streamlit as st

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📦 JavaScript Objects - Part 2")

st.subheader("Advanced JavaScript Objects")

st.markdown("---")

# ==========================================================
# NESTED OBJECTS
# ==========================================================

st.header("1️⃣ Nested Objects")

st.info("""
An object can contain another object.

This is called a Nested Object.
""")

st.code("""

let student={

    name:"John",

    age:20,

    address:{

        city:"Bangalore",

        state:"Karnataka",

        pincode:560029

    }

};

console.log(student.address.city);

""",language="javascript")

st.success("""
Output

Bangalore
""")

st.code("""

Student

│

├── Name

├── Age

└── Address

      ├── City

      ├── State

      └── Pincode

""")

# ==========================================================
# WHY NESTED OBJECTS
# ==========================================================

st.markdown("---")

st.header("Why Nested Objects?")

st.success("""

Real-world Applications

🏥 Patient

↓

Personal Details

↓

Address

↓

Medical Records

""")

st.success("""

🎓 Student Portal

↓

Student

↓

Course

↓

Department

↓

Marks

""")

st.success("""

🛒 E-Commerce

↓

Customer

↓

Address

↓

Order

↓

Payment

""")

# ==========================================================
# OBJECT METHODS
# ==========================================================

st.markdown("---")

st.header("2️⃣ Object Methods")

st.info("""
Objects can also contain Functions.

Functions inside Objects are called Methods.
""")

st.code("""

let student={

    name:"John",

    marks:95,

    display:function(){

        console.log("Welcome "+this.name);

    }

};

student.display();

""",language="javascript")

st.success("""

Output

Welcome John

""")

# ==========================================================
# THIS KEYWORD
# ==========================================================

st.markdown("---")

st.header("3️⃣ this Keyword")

st.info("""

this refers to the current object.

""")

st.code("""

let employee={

name:"Rahul",

salary:60000,

show:function(){

console.log(this.name);

console.log(this.salary);

}

};

employee.show();

""",language="javascript")

st.success("""

Output

Rahul

60000

""")

# ==========================================================
# OBJECT ITERATION
# ==========================================================

st.markdown("---")

st.header("4️⃣ Iterating Objects")

tab1,tab2,tab3,tab4=st.tabs([

"For...in",

"Object.keys()",

"Object.values()",

"Object.entries()"

])

with tab1:

    st.code("""

for(let key in student){

console.log(key);

}

""",language="javascript")

    st.success("""

Output

name

age

marks

""")

with tab2:

    st.code("""

console.log(

Object.keys(student)

);

""",language="javascript")

    st.success("""

['name','age','marks']

""")

with tab3:

    st.code("""

console.log(

Object.values(student)

);

""",language="javascript")

    st.success("""

['John',20,95]

""")

with tab4:

    st.code("""

console.log(

Object.entries(student)

);

""",language="javascript")

    st.success("""

[['name','John'],

['age',20],

['marks',95]]

""")

# ==========================================================
# OBJECT DESTRUCTURING
# ==========================================================

st.markdown("---")

st.header("5️⃣ Object Destructuring")

st.info("""

Instead of writing

student.name

student.age

student.course

We can extract them directly.

""")

st.code("""

let student={

name:"John",

age:20,

course:"BCA"

};

const{

name,

age,

course

}=student;

console.log(name);

console.log(course);

""",language="javascript")

st.success("""

Output

John

BCA

""")

# ==========================================================
# SPREAD OPERATOR
# ==========================================================

st.markdown("---")

st.header("6️⃣ Spread Operator (...)")

st.info("""

Spread Operator copies existing objects.

""")

st.code("""

let student={

name:"John",

age:20

};

let student2={

...student,

cgpa:9.2

};

console.log(student2);

""",language="javascript")

st.success("""

Output

{

name:"John",

age:20,

cgpa:9.2

}

""")

# ==========================================================
# REAL WORLD DEMO
# ==========================================================

st.markdown("---")

st.header("🏢 Real-world Example")

option=st.selectbox(

"Choose Domain",

[

"Student Portal",

"Hospital",

"Bank",

"Library",

"E-Commerce"

],

key="choose_domain_1"

)

if option=="Student Portal":

    st.code("""

Student

{

name

registerNumber

department

cgpa

attendance

}

""")

elif option=="Hospital":

    st.code("""

Patient

{

patientID

doctor

disease

room

bill

}

""")

elif option=="Bank":

    st.code("""

Account

{

accountNumber

customer

balance

branch

}

""")

elif option=="Library":

    st.code("""

Book

{

title

author

isbn

copies

}

""")

else:

    st.code("""

Product

{

name

price

category

stock

}

""")

# ==========================================================
# MINI DEMO
# ==========================================================

st.markdown("---")

st.header("🎮 Live Demonstration")

name=st.text_input("Student Name", key="live_demo_student_name")

age=st.number_input("Age",18,60, key="live_demo_age")

dept=st.text_input("Department", key="live_demo_department")

if st.button("Create Object", key="live_demo_create_object"):

    st.json({

        "name":name,

        "age":age,

        "department":dept

    })

# ==========================================================
# BEST PRACTICES
# ==========================================================

st.markdown("---")

st.header("💡 Best Practices")

st.success("""

✔ Use meaningful property names

✔ Group related data

✔ Avoid duplicate properties

✔ Keep object structure clean

✔ Prefer camelCase

✔ Use nested objects whenever necessary

""")

# ==========================================================
# COMMON MISTAKES
# ==========================================================

st.markdown("---")

st.header("⚠ Common Mistakes")

st.error("""

❌ Missing commas

❌ Wrong quotes

❌ Accessing undefined properties

❌ Forgetting this keyword

❌ Using = instead of :

""")

# ==========================================================
# THINK ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🧠 Think & Apply")

st.info("""

Create an Object for your selected domain.

Minimum Requirements

✔ 6 Properties

✔ 1 Nested Object

✔ 1 Method

✔ Display using Dot Notation

✔ Display using Bracket Notation

✔ Update one property

✔ Add one property

✔ Delete one property

""")

# ==========================================================
# KNOWLEDGE CHECK
# ==========================================================

st.markdown("---")

st.header("📋 Quick Knowledge Check")

q=st.radio(

"Which keyword refers to the current object?",

[

"self",

"current",

"this",

"object"

]

)

if st.button("Check Answer", key="check_answer_current_object"):

    if q=="this":

        st.success("✅ Correct!")

    else:

        st.error("❌ Incorrect. The correct answer is 'this'.")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

### Summary

✔ Nested Objects

✔ Methods

✔ this Keyword

✔ Object Iteration

✔ Object Destructuring

✔ Spread Operator

These concepts are heavily used in:

➡ JSON

➡ Fetch API

➡ Express.js

➡ MongoDB

➡ React

➡ MERN Stack

""")
import streamlit as st

st.title("📦 JavaScript Objects - Part 3")
st.subheader("Activities • Problem Solving • Viva • Interview Questions")

st.markdown("---")

# ============================================================
# WHY OBJECTS ARE IMPORTANT
# ============================================================

st.header("🚀 Why are Objects Important?")

st.success("""
Almost every modern web application uses JavaScript Objects.

Examples

✔ Student Portal

✔ Hospital Management

✔ Banking Application

✔ E-Commerce

✔ Social Media

✔ CRM

✔ Learning Management System

Objects are the foundation for

➡ JSON

➡ Fetch API

➡ Express.js

➡ React

➡ MongoDB

➡ MERN Stack
""")

# ============================================================
# PROBLEM SOLVING
# ============================================================

st.markdown("---")

st.header("💻 Problem Solving")

problem=st.selectbox(

"Choose Your Domain",

[

"Student Portal",

"Hospital",

"Library",

"Bank",

"E-Commerce",

"Tourism"

]

)

if problem=="Student Portal":

    st.info("""

Design an object for

Student Information

Minimum

• Name

• Register Number

• Department

• CGPA

• Attendance

• Address (Nested Object)

""")

elif problem=="Hospital":

    st.info("""

Design an object for

Patient Details

Minimum

• Patient ID

• Doctor

• Disease

• Age

• Address

• Contact Number

""")

elif problem=="Library":

    st.info("""

Design an object for

Book Details

Minimum

• Title

• Author

• Publisher

• Price

• Copies

• Shelf Number

""")

elif problem=="Bank":

    st.info("""

Design an object for

Customer Account

Minimum

• Account Number

• Customer Name

• Balance

• Branch

• IFSC

• Address

""")

else:

    st.info("""

Design an object based on your domain.

""")

# ============================================================
# THINK PAIR SHARE
# ============================================================

st.markdown("---")

st.header("🤝 Think - Pair - Share")

st.warning("""

Discuss with your partner

Question 1

Why are Objects better than multiple variables?

Question 2

Where have you already used Objects unknowingly?

Question 3

Can Arrays completely replace Objects?

""")

# ============================================================
# CODING CHALLENGE
# ============================================================

st.markdown("---")

st.header("🏆 Coding Challenge")

st.success("""

Create an Object

Requirements

✔ Minimum 6 Properties

✔ One Nested Object

✔ One Method

✔ Display 3 Properties

✔ Update one Property

✔ Add one Property

✔ Delete one Property

""")

# ============================================================
# DEBUGGING
# ============================================================

st.markdown("---")

st.header("🐞 Debug the Code")

st.code("""

let student={

name="John",

age=20

}

console.log(student.name)

""",language="javascript")

answer=st.checkbox("Show Solution")

if answer:

    st.code("""

let student={

name:"John",

age:20

};

console.log(student.name);

""",language="javascript")

# ============================================================
# MCQs
# ============================================================

st.markdown("---")

st.header("📝 MCQ Practice")

q1=st.radio(

"1. JavaScript Objects store data as",

[

"Arrays",

"Key-Value Pairs",

"Functions",

"Classes"

]

)

if st.button("Check MCQ 1", key="check_mcq_1"):

    if q1=="Key-Value Pairs":

        st.success("Correct ✅")

    else:

        st.error("Incorrect ❌")

st.markdown("---")

q2=st.radio(

"2. Which notation is commonly used to access object properties?",

[

"Dot Notation",

"Slash Notation",

"Hash Notation",

"Colon Notation"

]

)

if st.button("Check MCQ 2", key="check_mcq_2"):

    if q2=="Dot Notation":

        st.success("Correct ✅")

    else:

        st.error("Incorrect ❌")

st.markdown("---")

q3=st.radio(

"3. Which keyword refers to the current object?",

[

"self",

"this",

"current",

"super"

]

)

if st.button("Check MCQ 3", key="check_mcq_3"):

    if q3=="this":

        st.success("Correct ✅")

    else:

        st.error("Incorrect ❌")

# ============================================================
# VIVA
# ============================================================

st.markdown("---")

st.header("🎤 Viva Questions")

st.info("""

1. What is an Object?

2. Why do we need Objects?

3. Difference between Object and Array?

4. What are Properties?

5. What are Methods?

6. What is this keyword?

7. Explain Nested Objects.

8. What is Object Destructuring?

9. Explain Spread Operator.

10. Where are Objects used in Web Development?

""")

# ============================================================
# INTERVIEW
# ============================================================

st.markdown("---")

st.header("💼 Interview Questions")

st.success("""

✔ Why are Objects important?

✔ Difference between Object and JSON?

✔ Difference between Object and Array?

✔ Explain Dot vs Bracket Notation.

✔ Explain Object.keys().

✔ Explain Object.values().

✔ Explain Object.entries().

✔ Explain Object Destructuring.

✔ Explain Spread Operator.

""")

# ============================================================
# MINI PROJECT
# ============================================================

st.markdown("---")

st.header("🚀 Mini Project")

st.info("""

Create an Object based on your selected domain.

Possible Domains

✔ Student Portal

✔ Hospital

✔ Banking

✔ Tourism

✔ Library

✔ Food Delivery

✔ E-Commerce

✔ CRM

✔ Hotel Management

✔ Employee Management

""")

# ============================================================
# REAL WORLD
# ============================================================

st.markdown("---")

st.header("🌍 Real World Connection")

st.code("""

Registration Form

↓

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express Server

↓

Database

""")

st.success("""

Today's Object

↓

Tomorrow's JSON

↓

Next Class

Fetch API

↓

Express.js

""")

# ============================================================
# QUICK RECAP
# ============================================================

st.markdown("---")

st.header("📖 Quick Recap")

st.table({

"Concept":[

"Object",

"Property",

"Method",

"Nested Object",

"this",

"Destructuring",

"Spread Operator"

],

"Purpose":[

"Store Data",

"Store Values",

"Store Functions",

"Organize Data",

"Current Object",

"Extract Properties",

"Copy Objects"

]

})

# ============================================================
# BRIDGE
# ============================================================

st.markdown("---")

st.header("➡ Bridge to Next Topic")

st.success("""

Suppose

JavaScript Object

{

name:"John",

age:20

}

When this object is sent to the server

↓

It becomes

JSON

{

"name":"John",

"age":20

}

This transformation is the foundation of

✔ Fetch API

✔ Express.js

✔ REST API

✔ MongoDB

""")

st.info("""

Next Module

📄 JSON & JSON Objects

You will learn

✔ What is JSON?

✔ JSON Syntax

✔ JSON Objects

✔ JSON Arrays

✔ JSON Parsing

✔ JSON.stringify()

✔ JSON.parse()

""")

# ============================================================
# SUMMARY
# ============================================================

st.markdown("---")

st.success("""

🎉 Congratulations!

You have completed JavaScript Objects.

You are now ready to learn

➡ JSON

➡ Fetch API

➡ Express.js

➡ Client-Server Communication

➡ REST APIs

➡ MongoDB

""")
import streamlit as st

# ============================================================
# PAGE TITLE
# ============================================================

st.title("📝 JavaScript Forms")

st.subheader("Collecting User Information using HTML Forms and JavaScript")

st.markdown("---")

# ============================================================
# LEARNING OUTCOMES
# ============================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this chapter you will be able to

✅ Understand HTML Forms

✅ Understand Form Controls

✅ Read User Inputs

✅ Validate User Inputs

✅ Submit Forms

✅ Prevent Page Refresh

✅ Connect Forms with JavaScript

✅ Prepare Forms for Fetch API

""")

# ============================================================
# INTRODUCTION
# ============================================================

st.markdown("---")

st.header("❓ What is a Form?")

st.info("""

A Form is an HTML element used to collect information from users.

Examples

• Login

• Registration

• Student Admission

• Feedback

• Online Shopping

• Appointment Booking

""")

# ============================================================
# REAL WORLD
# ============================================================

st.markdown("---")

st.header("🌍 Where are Forms Used?")

col1,col2=st.columns(2)

with col1:

    st.success("""
🎓 Student Registration

🏥 Hospital

🏦 Banking

🛒 Shopping
""")

with col2:

    st.success("""
✈ Airline Booking

🍔 Food Ordering

📚 Library

🏨 Hotel Booking
""")

# ============================================================
# HTML FORM STRUCTURE
# ============================================================

st.markdown("---")

st.header("📄 HTML Form Structure")

st.code("""

<form>

<input>

<input>

<button>

</form>

""",language="html")

st.success("""

A Form contains

↓

Input Controls

↓

Button

↓

Submission

""")

# ============================================================
# FORM ELEMENTS
# ============================================================

st.markdown("---")

st.header("🧩 Common Form Elements")

st.table({

"Element":[

"text",

"password",

"email",

"number",

"radio",

"checkbox",

"date",

"file",

"textarea",

"select"

],

"Purpose":[

"Username",

"Password",

"Email",

"Age",

"Gender",

"Hobbies",

"DOB",

"Upload",

"Comments",

"Country"

]

})

# ============================================================
# DEMO
# ============================================================

st.markdown("---")

st.header("🎮 Interactive Form Demo")

name=st.text_input("Student Name", key="form_demo_student_name")

email=st.text_input("Email", key="form_demo_email")

age=st.number_input("Age",18,60, key="form_demo_age")

course=st.selectbox(

"Course",

["BCA","MCA","BSc","MSc"],

key="form_demo_course"

)

if st.button("Submit", key="form_demo_submit"):

    st.success("Form Submitted Successfully")

    st.json({

        "Name":name,

        "Email":email,

        "Age":age,

        "Course":course

    })

# ============================================================
# HOW FORM WORKS
# ============================================================

st.markdown("---")

st.header("⚙ Form Submission Workflow")

st.code("""

User

↓

Enter Data

↓

Click Submit

↓

JavaScript Reads Values

↓

Validation

↓

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express Server

""")

# ============================================================
# GETELEMENTBYID
# ============================================================

st.markdown("---")

st.header("📌 Reading Form Values")

st.code("""

const username=

document.getElementById("username").value;

""",language="javascript")

st.success("""

Step 1

Locate HTML Element

↓

Step 2

Read Value

↓

Store inside Variable

""")

# ============================================================
# VALUE PROPERTY
# ============================================================

st.markdown("---")

st.header("💡 value Property")

st.code("""

<input id="username">

↓

document.getElementById("username").value

""",language="javascript")

st.info("""

.value returns the value entered by the user.

""")

# ============================================================
# PREVENT DEFAULT
# ============================================================

st.markdown("---")

st.header("🚫 event.preventDefault()")

st.warning("""

Without JavaScript

↓

Submit

↓

Page Refreshes

""")

st.success("""

With preventDefault()

↓

No Refresh

↓

JavaScript Handles Submission

""")

st.code("""

event.preventDefault();

""",language="javascript")

# ============================================================
# VALIDATION
# ============================================================

st.markdown("---")

st.header("✔ Form Validation")

st.table({

"Validation":[

"Required",

"Email",

"Password",

"Age",

"Mobile"

],

"Purpose":[

"Cannot be Empty",

"Valid Email",

"Minimum Length",

"Range",

"10 Digits"

]

})

# ============================================================
# LIVE VALIDATION
# ============================================================

st.markdown("---")

st.header("🎮 Simple Validation")

user=st.text_input("Enter Username", key="validate_username")

if st.button("Validate", key="validate_button"):

    if user=="":

        st.error("Username Required")

    else:

        st.success("Valid Username")

# ============================================================
# BEST PRACTICES
# ============================================================

st.markdown("---")

st.header("⭐ Best Practices")

st.success("""

✔ Label every field

✔ Use Placeholder

✔ Validate Inputs

✔ Show Error Messages

✔ Prevent Empty Forms

✔ Use Meaningful IDs

""")

# ============================================================
# COMMON ERRORS
# ============================================================

st.markdown("---")

st.header("⚠ Common Mistakes")

st.error("""

❌ Duplicate IDs

❌ Missing Labels

❌ Empty Validation

❌ Wrong Input Types

❌ No Required Fields

""")

# ============================================================
# ACTIVITY
# ============================================================

st.markdown("---")

st.header("🎯 Classroom Activity")

st.info("""

Create a Form for your selected domain.

Minimum

✔ 6 Input Fields

✔ One Dropdown

✔ One Textarea

✔ Submit Button

✔ Validation

""")

# ============================================================
# THINK
# ============================================================

st.markdown("---")

st.header("🤔 Think")

st.success("""

Suppose

Google Login

Amazon Registration

Instagram Signup

How do they collect data?

Answer

Using HTML Forms

""")

# ============================================================
# SUMMARY
# ============================================================

st.markdown("---")

st.success("""

Today's Learning

↓

HTML Form

↓

Read Values

↓

Validation

↓

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express.js

""")

st.info("""

Next Chapter

🖱 Events and Event Handling

""")
import streamlit as st

st.title("🖱 Events & Event Handling")

st.subheader("Making Web Pages Interactive using JavaScript")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this chapter you will be able to

✅ Understand Events

✅ Understand Event Driven Programming

✅ Handle Mouse Events

✅ Handle Keyboard Events

✅ Handle Form Events

✅ Understand Event Listeners

✅ Connect Events with JavaScript

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("❓ What is an Event?")

st.info("""

An Event is an action performed by the user or browser.

Examples

✔ Mouse Click

✔ Typing

✔ Submit Form

✔ Hover Mouse

✔ Scroll

✔ Resize Window

""")

# ==========================================================
# EVENT DRIVEN PROGRAMMING
# ==========================================================

st.markdown("---")

st.header("⚡ Event Driven Programming")

st.success("""

JavaScript waits for an event.

↓

When an event occurs,

↓

JavaScript executes a function.

""")

st.code("""

User

↓

Click Button

↓

JavaScript

↓

Function Executes

""")

# ==========================================================
# REAL WORLD
# ==========================================================

st.markdown("---")

st.header("🌍 Real World Examples")

col1,col2=st.columns(2)

with col1:

    st.success("""

Login Button

↓

Click Event

""")

    st.success("""

Search Box

↓

Input Event

""")

    st.success("""

Registration Form

↓

Submit Event

""")

with col2:

    st.success("""

Shopping Cart

↓

Click Event

""")

    st.success("""

Online Quiz

↓

Change Event

""")

    st.success("""

Navigation Menu

↓

Mouse Hover

""")

# ==========================================================
# EVENT LISTENER
# ==========================================================

st.markdown("---")

st.header("🎧 Event Listener")

st.info("""

JavaScript continuously listens for user actions.

""")

st.code("""

button.addEventListener(

"click",

function(){

console.log("Clicked");

}

);

""",language="javascript")

# ==========================================================
# EVENT FLOW
# ==========================================================

st.markdown("---")

st.header("🔄 Event Workflow")

st.code("""

User

↓

Clicks Login

↓

Event Listener

↓

JavaScript Function

↓

Read Form

↓

Validation

↓

Fetch API

↓

Server

""")

# ==========================================================
# COMMON EVENTS
# ==========================================================

st.markdown("---")

st.header("📋 Common JavaScript Events")

events={

"Mouse Events":[

"click",

"dblclick",

"mouseover",

"mouseout",

"mousemove"

],

"Keyboard Events":[

"keydown",

"keyup",

"keypress"

],

"Form Events":[

"submit",

"change",

"input",

"focus",

"blur"

],

"Browser Events":[

"load",

"resize",

"scroll"

]

}

for key,value in events.items():

    st.subheader(key)

    st.write(value)

# ==========================================================
# CLICK EVENT
# ==========================================================

st.markdown("---")

st.header("🖱 Click Event")

st.code("""

button.addEventListener(

"click",

function(){

alert("Button Clicked");

}

);

""",language="javascript")

if st.button("Demo Click Event", key="demo_click_event"):

    st.success("Click Event Triggered")

# ==========================================================
# INPUT EVENT
# ==========================================================

st.markdown("---")

st.header("⌨ Input Event")

text=st.text_input("Type Something", key="input_event_text")

if text!="":

    st.success("Input Event Triggered")

# ==========================================================
# CHANGE EVENT
# ==========================================================

st.markdown("---")

st.header("🔄 Change Event")

course=st.selectbox(

"Select Course",

["BCA","MCA","MBA"],

key="select_course_event"

)

st.success(

f"Selected : {course}"

)

# ==========================================================
# SUBMIT EVENT
# ==========================================================

st.markdown("---")

st.header("📨 Submit Event")

name=st.text_input("Name", key="submit_event_name")

if st.button("Submit Form", key="submit_event_submit_form"):

    st.success(

f"Welcome {name}"

)

# ==========================================================
# MOUSE EVENTS
# ==========================================================

st.markdown("---")

st.header("🖱 Mouse Events")

st.table({

"Event":[

"click",

"dblclick",

"mouseover",

"mouseout",

"mousemove"

],

"Purpose":[

"Click",

"Double Click",

"Hover",

"Leave",

"Move Mouse"

]

})

# ==========================================================
# KEYBOARD EVENTS
# ==========================================================

st.markdown("---")

st.header("⌨ Keyboard Events")

st.table({

"Event":[

"keydown",

"keyup",

"keypress"

],

"Purpose":[

"Key Pressed",

"Key Released",

"Typing"

]

})

# ==========================================================
# FORM EVENTS
# ==========================================================

st.markdown("---")

st.header("📄 Form Events")

st.table({

"Event":[

"submit",

"focus",

"blur",

"change",

"input"

],

"Purpose":[

"Form Submit",

"Cursor Enter",

"Cursor Leave",

"Value Changed",

"Typing"

]

})

# ==========================================================
# ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🎯 Classroom Activity")

st.info("""

Develop a webpage for your selected domain.

Implement

✔ Click Event

✔ Input Event

✔ Change Event

✔ Submit Event

✔ Focus Event

""")

# ==========================================================
# COMMON ERRORS
# ==========================================================

st.markdown("---")

st.header("⚠ Common Mistakes")

st.error("""

❌ Wrong ID

❌ Missing Event Listener

❌ Typo in Event Name

❌ Null Object

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

Events

↓

Trigger JavaScript

↓

JavaScript Executes Functions

↓

Functions Read Forms

↓

Functions Call Fetch API

""")

st.info("""

Next

Async Programming

""")
import streamlit as st
import time

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("⚡ Asynchronous Programming & Async / Await")

st.subheader("Making JavaScript Wait Without Freezing the Browser")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this chapter you will be able to

✅ Understand Synchronous Programming

✅ Understand Asynchronous Programming

✅ Explain why Async Programming is required

✅ Understand async keyword

✅ Understand await keyword

✅ Explain Promise

✅ Use async-await with Fetch API

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("❓ Why Async Programming?")

st.info("""

Modern websites communicate with servers.

Whenever we

✔ Login

✔ Register

✔ Search

✔ Upload Images

✔ Make Payments

the browser waits for the server.

If JavaScript waits normally,

the entire webpage freezes.

""")

# ==========================================================
# RESTAURANT ANALOGY
# ==========================================================

st.markdown("---")

st.header("🍽 Restaurant Analogy")

st.success("""

Traditional (Synchronous)

Order Food

↓

Stand Near Kitchen

↓

Wait

↓

Collect Food

↓

Leave

Everyone waits.

""")

st.success("""

Modern Restaurant (Asynchronous)

Order Food

↓

Take Token

↓

Sit & Chat

↓

Food Ready

↓

Collect Food

No Time Wasted

""")

# ==========================================================
# PHONE ANALOGY
# ==========================================================

st.markdown("---")

st.header("📞 Phone Call Analogy")

col1,col2=st.columns(2)

with col1:

    st.error("""

Without Async

Call Friend

↓

Wait

↓

Wait

↓

Wait

↓

Friend Answers

""")

with col2:

    st.success("""

With Async

Call Friend

↓

Continue Working

↓

Friend Calls Back

↓

Receive Information

""")

# ==========================================================
# SYNCHRONOUS
# ==========================================================

st.markdown("---")

st.header("⛔ Synchronous Programming")

st.code("""

Step 1

↓

Finish

↓

Step 2

↓

Finish

↓

Step 3

""")

st.code("""

console.log("Start");

console.log("Middle");

console.log("End");

""",language="javascript")

st.success("""

Output

Start

Middle

End

""")

# ==========================================================
# ASYNCHRONOUS
# ==========================================================

st.markdown("---")

st.header("⚡ Asynchronous Programming")

st.code("""

Start

↓

Request Server

↓

Continue Working

↓

Server Responds

↓

Display Result

""")

# ==========================================================
# LIVE DEMO
# ==========================================================

st.markdown("---")

st.header("🎮 Simulation")

if st.button("Run Synchronous Example", key="run_sync_example"):

    st.write("Step 1")

    time.sleep(2)

    st.write("Step 2")

    time.sleep(2)

    st.write("Step 3")

if st.button("Run Async Simulation", key="run_async_simulation"):

    progress=st.progress(0)

    st.write("Sending Request...")

    for i in range(100):

        time.sleep(0.02)

        progress.progress(i+1)

    st.success("Server Responded Successfully")

# ==========================================================
# PROMISE
# ==========================================================

st.markdown("---")

st.header("📦 Promise")

st.info("""

Promise means

"I promise to give you the result later."

Promise has three states.

""")

st.table({

"State":[

"Pending",

"Resolved",

"Rejected"

],

"Meaning":[

"Waiting",

"Success",

"Failure"

]

})

# ==========================================================
# ASYNC KEYWORD
# ==========================================================

st.markdown("---")

st.header("🚀 async Keyword")

st.code("""

async function login(){

}

""",language="javascript")

st.success("""

async tells JavaScript

↓

This function performs asynchronous work.

""")

# ==========================================================
# AWAIT
# ==========================================================

st.markdown("---")

st.header("⏳ await Keyword")

st.code("""

const response=

await fetch("/login");

""",language="javascript")

st.success("""

await means

↓

Wait here

↓

Do not freeze browser

↓

Continue after response arrives

""")

# ==========================================================
# COMPLETE FLOW
# ==========================================================

st.markdown("---")

st.header("🌍 Complete Workflow")

st.code("""

User Clicks Login

↓

Event Listener

↓

async Function

↓

Fetch Request

↓

Express Server

↓

Processing

↓

JSON Response

↓

await

↓

Display Result

""")

# ==========================================================
# REAL PROJECT
# ==========================================================

st.markdown("---")

st.header("💻 Registration Example")

st.code("""

async function register(){

const response=

await fetch("/register");

const data=

await response.json();

}

""",language="javascript")

st.success("""

Exactly the same logic

used in your

Registration

Login

Dashboard Project

""")

# ==========================================================
# WHY NOT NORMAL FUNCTION
# ==========================================================

st.markdown("---")

st.header("🤔 Why Not Normal Function?")

st.error("""

Without async

↓

Cannot use await

↓

Browser waits incorrectly

""")

st.success("""

With async

↓

await works

↓

Browser remains responsive

""")

# ==========================================================
# ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🎯 Activity")

st.info("""

Identify asynchronous operations

✔ Login

✔ Registration

✔ Online Payment

✔ Upload Image

✔ Download File

✔ Google Search

""")

# ==========================================================
# MCQ
# ==========================================================

st.markdown("---")

st.header("📝 Knowledge Check")

q=st.radio(

"What does await do?",

[

"Stops JavaScript forever",

"Waits for Promise",

"Deletes Promise",

"Creates Promise"

]

)

if st.button("Check", key="check_button_promise"):

    if q=="Waits for Promise":

        st.success("Correct")

    else:

        st.error("Incorrect")

# ==========================================================
# VIVA
# ==========================================================

st.markdown("---")

st.header("🎤 Viva Questions")

st.info("""

1. What is asynchronous programming?

2. Why is async programming needed?

3. Difference between synchronous and asynchronous?

4. What is async?

5. What is await?

6. What is Promise?

7. Explain fetch with async-await.

""")

# ==========================================================
# INTERVIEW
# ==========================================================

st.markdown("---")

st.header("💼 Interview Questions")

st.success("""

✔ Why async-await over callbacks?

✔ Difference between Promise and async-await?

✔ Can await work without async?

✔ Explain browser waiting mechanism.

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

Today's Learning

Synchronous

↓

Asynchronous

↓

Promise

↓

async

↓

await

↓

Fetch API

↓

Express.js

""")

st.info("""

➡ Next Chapter

JSON & JSON Objects

""")
import streamlit as st
import json

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📄 JSON (JavaScript Object Notation)")

st.subheader("The Language used for Client-Server Communication")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this chapter students will be able to

✅ Understand JSON

✅ Explain why JSON is needed

✅ Compare Objects and JSON

✅ Convert Objects to JSON

✅ Convert JSON to Objects

✅ Understand Client-Server Communication

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("🤔 Why Do We Need JSON?")

st.info("""

Suppose a student fills a Registration Form.

JavaScript creates an Object.

Can we directly send that object to the server?

Answer

❌ No

The browser converts it into JSON.

""")

# ==========================================================
# COMPLETE FLOW
# ==========================================================

st.markdown("---")

st.header("🌍 Complete Communication")

st.code("""

Registration Form

↓

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express Server

↓

JavaScript Object

↓

Dashboard

""")

# ==========================================================
# OBJECT
# ==========================================================

st.markdown("---")

st.header("📦 JavaScript Object")

st.code("""

let student={

name:"John",

age:20,

course:"BCA"

};

""",language="javascript")

st.success("""

JavaScript understands this object.

""")

# ==========================================================
# JSON
# ==========================================================

st.markdown("---")

st.header("📄 JSON")

st.code("""

{

"name":"John",

"age":20,

"course":"BCA"

}

""",language="json")

st.success("""

Servers understand JSON.

""")

# ==========================================================
# DIFFERENCE
# ==========================================================

st.markdown("---")

st.header("⚖ JavaScript Object vs JSON")

st.table({

"JavaScript Object":[

'Keys may not require quotes',

"Can contain methods",

"Used inside JavaScript"

],

"JSON":[

'Keys must use double quotes',

"No functions allowed",

"Used for communication"

]

})

# ==========================================================
# WHY JSON
# ==========================================================

st.markdown("---")

st.header("🌍 Why JSON became Popular?")

col1,col2=st.columns(2)

with col1:

    st.success("""

✔ Lightweight

✔ Human Readable

✔ Easy to Parse

✔ Easy to Generate

""")

with col2:

    st.success("""

✔ Supported Everywhere

✔ Faster than XML

✔ API Friendly

✔ Easy to Debug

""")

# ==========================================================
# LIVE DEMO
# ==========================================================

st.markdown("---")

st.header("🎮 Object → JSON")

name=st.text_input("Name", key="object_json_3_name")

age=st.number_input("Age",18,60, key="object_json_3_age")

course=st.text_input("Course", key="object_json_3_course")

if st.button("Convert to JSON", key="object_json_3_convert"):

    student={

        "name":name,

        "age":age,

        "course":course

    }

    st.subheader("Python Dictionary / JavaScript Object")

    st.write(student)

    st.subheader("JSON")

    st.code(

        json.dumps(student,indent=4),

        language="json"

    )

# ==========================================================
# JSON RULES
# ==========================================================

st.markdown("---")

st.header("📋 JSON Rules")

st.success("""

✔ Data is Key-Value Pair

✔ Keys use Double Quotes

✔ Strings use Double Quotes

✔ No Functions

✔ No Undefined

✔ No Comments

""")

# ==========================================================
# JSON DATA TYPES
# ==========================================================

st.markdown("---")

st.header("📊 JSON Data Types")

st.table({

"Type":[

"String",

"Number",

"Boolean",

"Object",

"Array",

"null"

],

"Example":[

'"John"',

"25",

"true",

"{ }",

"[ ]",

"null"

]

})

# ==========================================================
# REAL WORLD
# ==========================================================

st.markdown("---")

st.header("🏢 Real World JSON")

choice=st.selectbox(

"Choose Example",

[

"Student",

"Hospital",

"Bank",

"E-Commerce"

],

key="choose_example_1"

)

if choice=="Student":

    st.code("""

{

"name":"John",

"department":"BCA",

"cgpa":9.2

}

""",language="json")

elif choice=="Hospital":

    st.code("""

{

"patient":"P101",

"doctor":"Dr Kumar",

"room":201

}

""",language="json")

elif choice=="Bank":

    st.code("""

{

"account":"12345",

"balance":50000

}

""",language="json")

else:

    st.code("""

{

"product":"Laptop",

"price":65000

}

""",language="json")

# ==========================================================
# THINK
# ==========================================================

st.markdown("---")

st.header("🤔 Think")

st.info("""

Google Search

↓

JSON

Instagram

↓

JSON

Amazon

↓

JSON

Hospital

↓

JSON

Almost every modern application communicates using JSON.

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express

↓

JSON

↓

JavaScript Object

""")
import streamlit as st
import json

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📄 JSON (JavaScript Object Notation)")

st.subheader("The Language used for Client-Server Communication")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this chapter students will be able to

✅ Understand JSON

✅ Explain why JSON is needed

✅ Compare Objects and JSON

✅ Convert Objects to JSON

✅ Convert JSON to Objects

✅ Understand Client-Server Communication

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("🤔 Why Do We Need JSON?")

st.info("""

Suppose a student fills a Registration Form.

JavaScript creates an Object.

Can we directly send that object to the server?

Answer

❌ No

The browser converts it into JSON.

""")

# ==========================================================
# COMPLETE FLOW
# ==========================================================

st.markdown("---")

st.header("🌍 Complete Communication")

st.code("""

Registration Form

↓

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express Server

↓

JavaScript Object

↓

Dashboard

""")

# ==========================================================
# OBJECT
# ==========================================================

st.markdown("---")

st.header("📦 JavaScript Object")

st.code("""

let student={

name:"John",

age:20,

course:"BCA"

};

""",language="javascript")

st.success("""

JavaScript understands this object.

""")

# ==========================================================
# JSON
# ==========================================================

st.markdown("---")

st.header("📄 JSON")

st.code("""

{

"name":"John",

"age":20,

"course":"BCA"

}

""",language="json")

st.success("""

Servers understand JSON.

""")

# ==========================================================
# DIFFERENCE
# ==========================================================

st.markdown("---")

st.header("⚖ JavaScript Object vs JSON")

st.table({

"JavaScript Object":[

'Keys may not require quotes',

"Can contain methods",

"Used inside JavaScript"

],

"JSON":[

'Keys must use double quotes',

"No functions allowed",

"Used for communication"

]

})

# ==========================================================
# WHY JSON
# ==========================================================

st.markdown("---")

st.header("🌍 Why JSON became Popular?")

col1,col2=st.columns(2)

with col1:

    st.success("""

✔ Lightweight

✔ Human Readable

✔ Easy to Parse

✔ Easy to Generate

""")

with col2:

    st.success("""

✔ Supported Everywhere

✔ Faster than XML

✔ API Friendly

✔ Easy to Debug

""")

# ==========================================================
# LIVE DEMO
# ==========================================================

st.markdown("---")

st.header("🎮 Object → JSON")

name=st.text_input("Name", key="object_json_4_name")

age=st.number_input("Age",18,60, key="object_json_4_age")

course=st.text_input("Course", key="object_json_4_course")

if st.button("Convert to JSON", key="object_json_4_convert"):

    student={

        "name":name,

        "age":age,

        "course":course

    }

    st.subheader("Python Dictionary / JavaScript Object")

    st.write(student)

    st.subheader("JSON")

    st.code(

        json.dumps(student,indent=4),

        language="json"

    )

# ==========================================================
# JSON RULES
# ==========================================================

st.markdown("---")

st.header("📋 JSON Rules")

st.success("""

✔ Data is Key-Value Pair

✔ Keys use Double Quotes

✔ Strings use Double Quotes

✔ No Functions

✔ No Undefined

✔ No Comments

""")

# ==========================================================
# JSON DATA TYPES
# ==========================================================

st.markdown("---")

st.header("📊 JSON Data Types")

st.table({

"Type":[

"String",

"Number",

"Boolean",

"Object",

"Array",

"null"

],

"Example":[

'"John"',

"25",

"true",

"{ }",

"[ ]",

"null"

]

})

# ==========================================================
# REAL WORLD
# ==========================================================

st.markdown("---")

st.header("🏢 Real World JSON")

choice=st.selectbox(

"Choose Example",

[

"Student",

"Hospital",

"Bank",

"E-Commerce"

],

key="choose_example_2"

)

if choice=="Student":

    st.code("""

{

"name":"John",

"department":"BCA",

"cgpa":9.2

}

""",language="json")

elif choice=="Hospital":

    st.code("""

{

"patient":"P101",

"doctor":"Dr Kumar",

"room":201

}

""",language="json")

elif choice=="Bank":

    st.code("""

{

"account":"12345",

"balance":50000

}

""",language="json")

else:

    st.code("""

{

"product":"Laptop",

"price":65000

}

""",language="json")

# ==========================================================
# THINK
# ==========================================================

st.markdown("---")

st.header("🤔 Think")

st.info("""

Google Search

↓

JSON

Instagram

↓

JSON

Amazon

↓

JSON

Hospital

↓

JSON

Almost every modern application communicates using JSON.

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express

↓

JSON

↓

JavaScript Object

""")
import streamlit as st
import json

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🔄 JSON.stringify() & JSON.parse()")

st.subheader("Converting JavaScript Objects into JSON and Back")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this lesson you will be able to

✅ Explain JSON.stringify()

✅ Explain JSON.parse()

✅ Convert Objects to JSON

✅ Convert JSON to Objects

✅ Understand Browser Communication

✅ Understand Fetch API Data Exchange

""")

# ==========================================================
# WHY STRINGIFY
# ==========================================================

st.markdown("---")

st.header("🤔 Why JSON.stringify()?")

st.info("""

JavaScript Objects cannot travel directly over the Internet.

They must first be converted into JSON.

This conversion is done using

JSON.stringify()

""")

# ==========================================================
# VISUALIZATION
# ==========================================================

st.markdown("---")

st.header("📦 Browser Communication")

st.code("""

JavaScript Object

        │

        ▼

JSON.stringify()

        │

        ▼

JSON

        │

        ▼

Internet

        │

        ▼

Express Server

""")

# ==========================================================
# OBJECT
# ==========================================================

st.markdown("---")

st.header("📦 Step 1 : JavaScript Object")

st.code("""

let student={

name:"John",

age:20,

course:"BCA"

};

""",language="javascript")

# ==========================================================
# STRINGIFY
# ==========================================================

st.markdown("---")

st.header("🔄 Step 2 : JSON.stringify()")

st.code("""

let jsonData=

JSON.stringify(student);

""",language="javascript")

st.success("""

Output

{

"name":"John",

"age":20,

"course":"BCA"

}

""")

# ==========================================================
# PARSE
# ==========================================================

st.markdown("---")

st.header("📥 Step 3 : JSON.parse()")

st.code("""

let object=

JSON.parse(jsonData);

""",language="javascript")

st.success("""

JSON

↓

Object

""")

# ==========================================================
# COMPLETE WORKFLOW
# ==========================================================

st.markdown("---")

st.header("🌍 Complete Workflow")

st.code("""

Registration Form

↓

JavaScript Object

↓

JSON.stringify()

↓

JSON

↓

Fetch API

↓

Internet

↓

Express Server

↓

JSON.parse()

↓

JavaScript Object

↓

Validation

↓

JSON Response

↓

Browser

""")

# ==========================================================
# LIVE DEMO
# ==========================================================

st.markdown("---")

st.header("🎮 Interactive Demonstration")

name=st.text_input("Name", key="interactive_demo_name")

age=st.number_input("Age",18,60, key="interactive_demo_age")

dept=st.text_input("Department", key="interactive_demo_department")

if st.button("Convert", key="convert_interactive_demo"):

    obj={

        "name":name,

        "age":age,

        "department":dept

    }

    st.subheader("Python Dictionary / JavaScript Object")

    st.write(obj)

    st.subheader("JSON")

    json_data=json.dumps(obj,indent=4)

    st.code(json_data,language="json")

    st.subheader("Back to Object")

    st.write(json.loads(json_data))

# ==========================================================
# STRINGIFY VS PARSE
# ==========================================================

st.markdown("---")

st.header("⚖ JSON.stringify() vs JSON.parse()")

st.table({

"JSON.stringify()":[

"Object ➜ JSON",

"Sending Data",

"Browser"

],

"JSON.parse()":[

"JSON ➜ Object",

"Receiving Data",

"Browser / Server"

]

})

# ==========================================================
# FETCH CONNECTION
# ==========================================================

st.markdown("---")

st.header("🔗 Connection with Fetch API")

st.code("""

fetch("/login",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

email,

password

})

})

""",language="javascript")

st.success("""

Notice

body

↓

JSON.stringify()

This is exactly what your Registration Project uses.

""")

# ==========================================================
# SERVER SIDE
# ==========================================================

st.markdown("---")

st.header("🌐 Server Side")

st.code("""

app.use(express.json())

↓

JSON

↓

JavaScript Object

↓

req.body

""",language="javascript")

st.success("""

Browser

↓

JSON

↓

Express

↓

Object

""")

# ==========================================================
# COMPLETE LOGIN
# ==========================================================

st.markdown("---")

st.header("🔐 Login Workflow")

st.code("""

User

↓

Enter Email

↓

Click Login

↓

JavaScript Object

↓

JSON.stringify()

↓

Fetch

↓

Express

↓

JSON.parse()

↓

Validation

↓

JSON Response

↓

Browser

↓

Dashboard

""")

# ==========================================================
# COMMON ERRORS
# ==========================================================

st.markdown("---")

st.header("⚠ Common Mistakes")

st.error("""

❌ Forgetting JSON.stringify()

❌ Wrong Quotes

❌ Invalid JSON

❌ Missing express.json()

❌ Forgetting await response.json()

""")

# ==========================================================
# ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🎯 Classroom Activity")

st.info("""

Take your

Registration Project

Identify

✔ JavaScript Object

✔ JSON.stringify()

✔ Fetch API

✔ JSON Response

✔ response.json()

""")

# ==========================================================
# MCQ
# ==========================================================

st.markdown("---")

st.header("📝 Quick Check")

q=st.radio(

"Which function converts an Object into JSON?",

[

"JSON.parse()",

"JSON.stringify()",

"parseInt()",

"Object.parse()"

]

)

if st.button("Check Answer", key="check_answer_json_parse"):

    if q=="JSON.stringify()":

        st.success("Correct")

    else:

        st.error("Incorrect")

# ==========================================================
# VIVA
# ==========================================================

st.markdown("---")

st.header("🎤 Viva Questions")

st.info("""

1. What is JSON.stringify()?

2. Why do we use JSON.parse()?

3. Why can't JavaScript Objects travel directly?

4. Explain Browser → Server Communication.

5. Where is JSON.stringify() used in Fetch API?

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

JavaScript Object

↓

JSON.stringify()

↓

JSON

↓

Fetch API

↓

Express.js

↓

JSON.parse()

↓

JavaScript Object

↓

Response

""")

st.info("""

➡ Next Chapter

Fetch API

The most important chapter of this module.
""")
import streamlit as st
import time

# ============================================================
# PAGE TITLE
# ============================================================

st.title("🌐 Fetch API")

st.subheader("Connecting Browser and Express Server")

st.markdown("---")

# ============================================================
# LEARNING OUTCOMES
# ============================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this chapter students will be able to

✅ Explain Fetch API

✅ Understand Request and Response

✅ Explain HTTP Methods

✅ Understand Headers

✅ Understand Request Body

✅ Send Data to Express Server

✅ Receive JSON Response

""")

# ============================================================
# INTRODUCTION
# ============================================================

st.markdown("---")

st.header("❓ What is Fetch API?")

st.info("""

Fetch API is a JavaScript function used to communicate with servers.

It allows a browser to

✔ Send Data

✔ Receive Data

without refreshing the webpage.

""")

# ============================================================
# WHY FETCH
# ============================================================

st.markdown("---")

st.header("🤔 Why Fetch API?")

col1,col2=st.columns(2)

with col1:

    st.error("""

Without Fetch

↓

Submit Form

↓

Page Refresh

↓

Slow

""")

with col2:

    st.success("""

With Fetch

↓

Send Request

↓

No Refresh

↓

Fast

""")

# ============================================================
# COMPLETE WORKFLOW
# ============================================================

st.markdown("---")

st.header("🌍 Fetch API Workflow")

st.code("""

Browser

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

response.json()

↓

Browser Updates UI

""")

# ============================================================
# FETCH SYNTAX
# ============================================================

st.markdown("---")

st.header("📌 Basic Fetch Syntax")

st.code("""

fetch("/login")

""",language="javascript")

st.success("""

fetch()

↓

Creates an HTTP Request

""")

# ============================================================
# COMPLETE FETCH
# ============================================================

st.markdown("---")

st.header("💻 Complete Fetch Example")

st.code("""

const response=

await fetch("/login",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

email,

password

})

});

""",language="javascript")

# ============================================================
# BREAKDOWN
# ============================================================

st.markdown("---")

st.header("🔍 Breaking Down the Fetch Code")

tabs=st.tabs([

"fetch()",

"method",

"headers",

"body"

])

with tabs[0]:

    st.success("""

fetch()

↓

Starts communication

with the server.

""")

with tabs[1]:

    st.success("""

POST

↓

Sending Data

GET

↓

Receiving Data

""")

with tabs[2]:

    st.success("""

Content-Type

↓

application/json

Tells server

JSON is coming.

""")

with tabs[3]:

    st.success("""

body

↓

Contains the data

being sent

to server.

""")

# ============================================================
# LIVE DEMO
# ============================================================

st.markdown("---")

st.header("🎮 Request Simulation")

email=st.text_input("Email", key="request_sim_email")

password=st.text_input("Password", key="request_sim_password")

if st.button("Send Request"):

    progress=st.progress(0)

    for i in range(100):

        time.sleep(0.01)

        progress.progress(i+1)

    st.success("Request Sent Successfully")

    st.json({

        "email":email,

        "password":password

    })

# ============================================================
# REQUEST
# ============================================================

st.markdown("---")

st.header("📤 HTTP Request")

st.table({

"Part":[

"URL",

"Method",

"Headers",

"Body"

],

"Purpose":[

"Server Address",

"GET / POST",

"Information",

"Actual Data"

]

})

# ============================================================
# RESPONSE
# ============================================================

st.markdown("---")

st.header("📥 HTTP Response")

st.table({

"Server Returns":[

"Status",

"JSON",

"Message"

],

"Example":[

"200",

'{"success":true}',

"Login Successful"

]

})

# ============================================================
# FETCH FLOW
# ============================================================

st.markdown("---")

st.header("🌍 Complete Login Flow")

st.code("""

User

↓

Click Login

↓

Event

↓

async Function

↓

fetch()

↓

Express Server

↓

Validate

↓

JSON

↓

Browser

↓

Dashboard

""")

# ============================================================
# HTTP METHODS
# ============================================================

st.markdown("---")

st.header("📚 HTTP Methods")

st.table({

"Method":[

"GET",

"POST",

"PUT",

"DELETE"

],

"Purpose":[

"Read",

"Create",

"Update",

"Delete"

]

})

# ============================================================
# GET vs POST
# ============================================================

st.markdown("---")

st.header("⚖ GET vs POST")

st.table({

"GET":[

"Retrieve Data",

"No Request Body",

"Visible URL"

],

"POST":[

"Send Data",

"Request Body",

"Secure"

]

})

# ============================================================
# FETCH + EXPRESS
# ============================================================

st.markdown("---")

st.header("🔗 Fetch + Express")

st.code("""

Browser

↓

fetch()

↓

POST

↓

Express

↓

app.post()

↓

Response

↓

Browser

""")

# ============================================================
# COMMON ERRORS
# ============================================================

st.markdown("---")

st.header("⚠ Common Errors")

st.error("""

❌ Wrong Route

❌ Missing await

❌ Missing JSON.stringify()

❌ Missing response.json()

❌ Wrong Content-Type

""")

# ============================================================
# ACTIVITY
# ============================================================

st.markdown("---")

st.header("🎯 Activity")

st.info("""

Take your Registration Project.

Identify

✔ URL

✔ Method

✔ Headers

✔ Body

✔ Response

✔ JSON

""")

# ============================================================
# SUMMARY
# ============================================================

st.markdown("---")

st.success("""

HTML Form

↓

Object

↓

JSON

↓

Fetch

↓

Express

↓

JSON

↓

Browser

""")
import streamlit as st
import time

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🌐 Fetch API - Request & Response Lifecycle")

st.subheader("Understanding how Browser communicates with Express Server")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this lesson students will be able to

✅ Explain complete Fetch Workflow

✅ Understand HTTP Request

✅ Understand HTTP Response

✅ Explain Status Codes

✅ Handle Errors

✅ Understand try...catch

✅ Debug Fetch Applications

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("❓ What happens after clicking Login?")

st.code("""

User

↓

Clicks Login

↓

JavaScript

↓

Fetch API

↓

Internet

↓

Express Server

↓

Validation

↓

JSON Response

↓

Browser Updates UI

""")

# ==========================================================
# INTERACTIVE SIMULATION
# ==========================================================

st.markdown("---")

st.header("🎮 Browser Communication Simulation")

if st.button("Start Simulation", key="start_communication_simulation"):

    progress=st.progress(0)

    status=st.empty()

    steps=[

        "📄 Reading Form Data",

        "📦 Creating JavaScript Object",

        "🔄 JSON.stringify()",

        "🌐 Sending HTTP Request",

        "🚀 Request travelling to Server",

        "🖥 Express Server Processing",

        "✔ Credentials Validated",

        "📤 Creating JSON Response",

        "🌐 Sending Response",

        "📥 Browser Receiving Response",

        "🎉 Dashboard Updated"

    ]

    for i,step in enumerate(steps):

        progress.progress((i+1)*9)

        status.success(step)

        time.sleep(0.8)

    st.balloons()

# ==========================================================
# HTTP REQUEST
# ==========================================================

st.markdown("---")

st.header("📤 HTTP Request")

st.code("""

POST /login HTTP/1.1

Host: localhost:3000

Content-Type: application/json

{

"email":"john@gmail.com",

"password":"123"

}

""")

st.success("""

Request contains

✔ URL

✔ Method

✔ Headers

✔ Body

""")

# ==========================================================
# REQUEST BREAKDOWN
# ==========================================================

st.markdown("---")

st.header("🔍 Request Breakdown")

tabs=st.tabs([

"URL",

"Method",

"Headers",

"Body"

])

with tabs[0]:

    st.info("""

Server Address

Example

/login

/register

/dashboard

""")

with tabs[1]:

    st.info("""

GET

Read

POST

Create

PUT

Update

DELETE

Delete

""")

with tabs[2]:

    st.info("""

Content-Type

application/json

Authorization

Accept

""")

with tabs[3]:

    st.info("""

Actual Data

Email

Password

Age

Course

""")

# ==========================================================
# RESPONSE
# ==========================================================

st.markdown("---")

st.header("📥 HTTP Response")

st.code("""

HTTP/1.1 200 OK

Content-Type: application/json

{

"success":true,

"message":"Login Successful"

}

""")

# ==========================================================
# STATUS CODES
# ==========================================================

st.markdown("---")

st.header("📊 HTTP Status Codes")

st.table({

"Status":[

"200",

"201",

"400",

"401",

"403",

"404",

"500"

],

"Meaning":[

"Success",

"Created",

"Bad Request",

"Unauthorized",

"Forbidden",

"Not Found",

"Internal Server Error"

]

})

# ==========================================================
# TRY CATCH
# ==========================================================

st.markdown("---")

st.header("🛡 Error Handling using try...catch")

st.code("""

try{

const response=

await fetch("/login");

}

catch(error){

console.log(error);

}

""",language="javascript")

st.success("""

If server fails,

application should not crash.

""")

# ==========================================================
# WHY TRY CATCH
# ==========================================================

st.markdown("---")

st.header("🤔 Why try...catch?")

col1,col2=st.columns(2)

with col1:

    st.error("""

Without try...catch

↓

Application Stops

↓

Poor User Experience

""")

with col2:

    st.success("""

With try...catch

↓

Display Error Message

↓

Continue Running

""")

# ==========================================================
# FETCH TEMPLATE
# ==========================================================

st.markdown("---")

st.header("💻 Standard Fetch Template")

st.code("""

async function login(){

try{

const response=

await fetch("/login",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

email,

password

})

});

const data=

await response.json();

console.log(data);

}

catch(error){

console.log(error);

}

}

""",language="javascript")

# ==========================================================
# DEBUGGING
# ==========================================================

st.markdown("---")

st.header("🐞 Debugging Fetch Applications")

st.warning("""

Always Check

✔ Browser Console

✔ Network Tab

✔ Server Terminal

✔ Response Status

✔ Route Name

✔ JSON Format

""")

# ==========================================================
# DEVELOPER TOOLS
# ==========================================================

st.markdown("---")

st.header("🛠 Browser Developer Tools")

st.success("""

Press

F12

↓

Network

↓

Click Login

↓

Observe

POST Request

Status Code

Headers

Response

""")

# ==========================================================
# COMMON ERRORS
# ==========================================================

st.markdown("---")

st.header("⚠ Common Errors")

st.table({

"Problem":[

"404",

"500",

"Missing await",

"Wrong Route",

"No JSON",

"CORS"

],

"Reason":[

"Route Missing",

"Server Error",

"Forgot await",

"Typo",

"Wrong Data",

"Different Origin"

]

})

# ==========================================================
# REAL LIFE APPLICATIONS
# ==========================================================

st.markdown("---")

st.header("🌍 Applications using Fetch API")

apps=[

"Google Search",

"Gmail",

"Instagram",

"Facebook",

"Amazon",

"Netflix",

"YouTube",

"WhatsApp Web",

"Student Portal",

"Online Banking"

]

for app in apps:

    st.success(app)

# ==========================================================
# THINK ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🧠 Think & Discuss")

st.info("""

Imagine Internet becomes slow.

What happens?

↓

Fetch waits.

↓

Browser remains responsive.

↓

User sees Loading Indicator.

Why?

Because of

Async Await.

""")

# ==========================================================
# LAB ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🎯 Lab Exercise")

st.success("""

Take your Registration Project.

Observe

✔ Browser Request

✔ Browser Response

✔ Network Tab

✔ JSON Payload

✔ Express Terminal

✔ Status Code

""")

# ==========================================================
# MCQ
# ==========================================================

st.markdown("---")

st.header("📝 Knowledge Check")

answer=st.radio(

"Which tab in Browser helps us monitor Fetch requests?",

[

"Elements",

"Console",

"Network",

"Sources"

]

)

if st.button("Check Answer", key="check_answer_network"):

    if answer=="Network":

        st.success("Correct!")

    else:

        st.error("Incorrect!")

# ==========================================================
# VIVA
# ==========================================================

st.markdown("---")

st.header("🎤 Viva Questions")

st.info("""

1. What is Fetch API?

2. Difference between Request and Response?

3. Explain HTTP Status Codes.

4. Why do we use try...catch?

5. What is response.json()?

6. Explain Browser Developer Tools.

7. What happens when Login button is clicked?

""")

# ==========================================================
# INTERVIEW
# ==========================================================

st.markdown("---")

st.header("💼 Interview Questions")

st.success("""

✔ Explain Fetch API.

✔ Difference between GET and POST.

✔ Difference between Request and Response.

✔ Explain HTTP Status Codes.

✔ Why use Async Await with Fetch?

✔ Explain JSON.stringify().

✔ Explain response.json().

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

Browser

↓

Fetch API

↓

Request

↓

Express

↓

Response

↓

Dashboard

""")

st.info("""

➡ Next Chapter

Navigator API & Browser Features

""")
import streamlit as st

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🌍 JavaScript Navigator API")

st.subheader("Accessing Browser Information")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this chapter students will be able to

✅ Explain Navigator Object

✅ Retrieve Browser Information

✅ Detect Online Status

✅ Understand Geolocation

✅ Understand Clipboard API

✅ Explain Browser Features

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("❓ What is Navigator Object?")

st.info("""

Navigator is a built-in JavaScript Object.

It provides information about

✔ Browser

✔ Operating System

✔ Internet Connection

✔ Language

✔ Platform

✔ Location

""")

# ==========================================================
# WHY NAVIGATOR
# ==========================================================

st.markdown("---")

st.header("🤔 Why Navigator API?")

st.success("""

Applications use Navigator to

✔ Detect Device

✔ Detect Browser

✔ Detect Language

✔ Detect Internet Connectivity

✔ Access Geolocation

✔ Improve User Experience

""")

# ==========================================================
# VISUALIZATION
# ==========================================================

st.markdown("---")

st.header("🌐 Navigator Object")

st.code("""

Browser

↓

Navigator

↓

userAgent

platform

language

onLine

geolocation

clipboard

""")

# ==========================================================
# COMMON PROPERTIES
# ==========================================================

st.markdown("---")

st.header("📋 Common Navigator Properties")

st.table({

"Property":[

"userAgent",

"platform",

"language",

"onLine",

"geolocation",

"clipboard"

],

"Purpose":[

"Browser Details",

"Operating System",

"Browser Language",

"Internet Status",

"Current Location",

"Copy/Paste"

]

})

# ==========================================================
# USER AGENT
# ==========================================================

st.markdown("---")

st.header("🖥 navigator.userAgent")

st.code("""

console.log(

navigator.userAgent

);

""",language="javascript")

st.success("""

Returns Browser Information

Chrome

Firefox

Edge

Safari

""")

# ==========================================================
# PLATFORM
# ==========================================================

st.markdown("---")

st.header("💻 navigator.platform")

st.code("""

console.log(

navigator.platform

);

""",language="javascript")

st.success("""

Examples

MacIntel

Win32

Linux x86_64

""")

# ==========================================================
# LANGUAGE
# ==========================================================

st.markdown("---")

st.header("🌎 navigator.language")

st.code("""

console.log(

navigator.language

);

""",language="javascript")

st.success("""

Examples

en-US

en-IN

ta-IN

hi-IN

""")

# ==========================================================
# ONLINE
# ==========================================================

st.markdown("---")

st.header("📶 navigator.onLine")

st.code("""

if(navigator.onLine){

console.log("Connected");

}

""",language="javascript")

st.success("""

Useful for

Banking

Payment

Online Exams

LMS

""")

# ==========================================================
# GEOLOCATION
# ==========================================================

st.markdown("---")

st.header("📍 Geolocation")

st.code("""

navigator.geolocation.getCurrentPosition(

function(position){

console.log(position);

}

);

""",language="javascript")

st.info("""

Permission Required

↓

Browser asks

Allow Location?

""")

# ==========================================================
# CLIPBOARD
# ==========================================================

st.markdown("---")

st.header("📋 Clipboard API")

st.code("""

navigator.clipboard.writeText(

"Hello"

);

""",language="javascript")

st.success("""

Copies text

to Clipboard

""")

# ==========================================================
# REAL WORLD
# ==========================================================

st.markdown("---")

st.header("🌍 Real-world Applications")

apps=[

"Google Maps",

"Uber",

"Swiggy",

"Zomato",

"Amazon",

"Online Banking",

"Weather Apps",

"Hospital Apps",

"Food Delivery",

"Tourism"

]

for app in apps:

    st.success(app)

# ==========================================================
# MINI DEMO
# ==========================================================

st.markdown("---")

st.header("🎮 Interactive Browser Information")

browser=st.selectbox(

"Browser",

[

"Chrome",

"Firefox",

"Edge",

"Safari"

],

key="browser_select"

)

platform=st.selectbox(

"Platform",

[

"Windows",

"Mac",

"Linux",

"Android",

"iOS"

],

key="platform_select"

)

online=st.radio(

"Internet Status",

["Online","Offline"]

)

if st.button("Show Browser Information", key="show_browser_info"):

    st.json({

        "Browser":browser,

        "Platform":platform,

        "Status":online

    })

# ==========================================================
# SECURITY
# ==========================================================

st.markdown("---")

st.header("🔒 Browser Security")

st.warning("""

Navigator APIs

like

Geolocation

Camera

Microphone

Clipboard

require user permission.

""")

# ==========================================================
# BEST PRACTICES
# ==========================================================

st.markdown("---")

st.header("⭐ Best Practices")

st.success("""

✔ Ask permission

✔ Respect Privacy

✔ Handle Offline Users

✔ Provide Fallback

✔ Do not misuse Location

""")

# ==========================================================
# COMMON ERRORS
# ==========================================================

st.markdown("---")

st.header("⚠ Common Errors")

st.error("""

❌ Permission Denied

❌ Offline Internet

❌ Browser Compatibility

❌ HTTPS Required

""")

# ==========================================================
# ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🎯 Classroom Activity")

st.info("""

Develop a webpage for your selected domain.

Use any TWO Navigator properties.

Example

✔ Detect Browser

✔ Detect Language

✔ Detect Internet

✔ Detect Platform

Display the information.

""")

# ==========================================================
# KNOWLEDGE CHECK
# ==========================================================

st.markdown("---")

st.header("📝 MCQ")

answer=st.radio(

"Which property detects Internet connectivity?",

[

"userAgent",

"platform",

"onLine",

"language"

]

)

if st.button("Check", key="check_button_online"):

    if answer=="onLine":

        st.success("Correct!")

    else:

        st.error("Incorrect!")

# ==========================================================
# VIVA
# ==========================================================

st.markdown("---")

st.header("🎤 Viva Questions")

st.info("""

1. What is Navigator?

2. Explain navigator.userAgent.

3. Explain navigator.platform.

4. Explain navigator.language.

5. Explain navigator.onLine.

6. Explain Geolocation.

7. Explain Clipboard API.

""")

# ==========================================================
# INTERVIEW
# ==========================================================

st.markdown("---")

st.header("💼 Interview Questions")

st.success("""

✔ Why use Navigator API?

✔ Which APIs require permission?

✔ Difference between userAgent and platform?

✔ Explain navigator.onLine.

✔ Explain Browser Security.

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

Navigator

↓

Browser Information

↓

Device

↓

Location

↓

Internet

↓

Clipboard

""")

st.info("""

➡ Next Chapter

🍪 Cookies & Browser Storage

""")
import streamlit as st

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🍪 Cookies & Browser Storage")

st.subheader("Remembering Users using Cookies, Local Storage and Session Storage")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this lesson students will be able to

✅ Understand Cookies

✅ Explain Browser Storage

✅ Create Cookies

✅ Read Cookies

✅ Delete Cookies

✅ Compare Cookies and Local Storage

✅ Explain Session Storage

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("❓ Why do websites remember us?")

st.info("""

Have you noticed?

✔ Gmail remembers your Email

✔ Amazon remembers your Cart

✔ Netflix remembers your Profile

✔ Facebook remembers Login

How?

Using Browser Storage.

""")

# ==========================================================
# VISUALIZATION
# ==========================================================

st.markdown("---")

st.header("🌍 Browser Storage")

st.code("""

Browser

↓

Cookies

↓

Local Storage

↓

Session Storage

""")

# ==========================================================
# WHAT IS COOKIE
# ==========================================================

st.markdown("---")

st.header("🍪 What is a Cookie?")

st.success("""

A Cookie is a small text file

stored inside the browser.

It stores

✔ Username

✔ Session ID

✔ Preferences

✔ Authentication

""")

# ==========================================================
# COOKIE FEATURES
# ==========================================================

st.markdown("---")

st.header("⭐ Cookie Features")

st.table({

"Feature":[

"Stored in Browser",

"Small Size",

"Expiry",

"Sent to Server",

"Supports Authentication"

],

"Value":[

"Yes",

"4 KB",

"Yes",

"Yes",

"Yes"

]

})

# ==========================================================
# CREATE COOKIE
# ==========================================================

st.markdown("---")

st.header("📝 Creating Cookie")

st.code("""

document.cookie=

"username=John";

""",language="javascript")

st.success("""

Cookie Created

""")

# ==========================================================
# READ COOKIE
# ==========================================================

st.markdown("---")

st.header("📖 Reading Cookie")

st.code("""

console.log(

document.cookie

);

""",language="javascript")

# ==========================================================
# DELETE COOKIE
# ==========================================================

st.markdown("---")

st.header("🗑 Deleting Cookie")

st.code("""

document.cookie=

"username=;

expires=Thu, 01 Jan 1970";

""",language="javascript")

# ==========================================================
# COOKIE EXAMPLE
# ==========================================================

st.markdown("---")

st.header("🎮 Remember Me Example")

remember=st.checkbox("Remember Me")

if remember:

    st.success("""

Cookie will store

User Information

until expiry.

""")

else:

    st.warning("""

User information

will not be remembered.

""")

# ==========================================================
# LOCAL STORAGE
# ==========================================================

st.markdown("---")

st.header("💾 Local Storage")

st.code("""

localStorage.setItem(

"user",

"John"

);

""",language="javascript")

st.success("""

Stored Permanently

until user deletes it.

""")

# ==========================================================
# READ LOCAL STORAGE
# ==========================================================

st.markdown("---")

st.header("📥 Reading Local Storage")

st.code("""

localStorage.getItem(

"user"

);

""",language="javascript")

# ==========================================================
# REMOVE LOCAL STORAGE
# ==========================================================

st.markdown("---")

st.header("🗑 Removing Local Storage")

st.code("""

localStorage.removeItem(

"user"

);

""",language="javascript")

# ==========================================================
# SESSION STORAGE
# ==========================================================

st.markdown("---")

st.header("🗂 Session Storage")

st.code("""

sessionStorage.setItem(

"user",

"John"

);

""",language="javascript")

st.success("""

Stored

until browser tab closes.

""")

# ==========================================================
# COMPARISON
# ==========================================================

st.markdown("---")

st.header("⚖ Cookies vs Local Storage vs Session Storage")

st.table({

"Cookies":[

"4 KB",

"Expiry",

"Yes",

"Authentication"

],

"Local Storage":[

"5-10 MB",

"Permanent",

"No",

"Preferences"

],

"Session Storage":[

"5 MB",

"Until Tab Closes",

"No",

"Temporary Data"

]

})

# ==========================================================
# REAL WORLD
# ==========================================================

st.markdown("---")

st.header("🌍 Real World Examples")

examples=[

"Gmail Login",

"Amazon Cart",

"Netflix Profile",

"Dark Mode",

"Language Preference",

"Student Portal",

"Banking",

"E-Commerce"

]

for i in examples:

    st.success(i)

# ==========================================================
# LOGIN FLOW
# ==========================================================

st.markdown("---")

st.header("🔐 Login Workflow")

st.code("""

Login

↓

Validate

↓

Cookie Created

↓

Dashboard

↓

Browser remembers user

""")

# ==========================================================
# SECURITY
# ==========================================================

st.markdown("---")

st.header("🔒 Security")

st.warning("""

Never store

Passwords

Credit Card

OTP

inside Cookies.

""")

# ==========================================================
# BEST PRACTICES
# ==========================================================

st.markdown("---")

st.header("⭐ Best Practices")

st.success("""

✔ Store Session ID

✔ Store Theme

✔ Store Language

✔ Use Expiry

✔ Delete after Logout

""")

# ==========================================================
# COMMON ERRORS
# ==========================================================

st.markdown("---")

st.header("⚠ Common Mistakes")

st.error("""

❌ Storing Password

❌ Large Data

❌ No Expiry

❌ Forget Logout

""")

# ==========================================================
# ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🎯 Classroom Activity")

st.info("""

Enhance your Login Application.

Implement

✔ Remember Me

✔ Cookie

OR

✔ Local Storage

Display Username

after Login.

""")

# ==========================================================
# MCQ
# ==========================================================

st.markdown("---")

st.header("📝 MCQ")

answer=st.radio(

"Which storage is automatically sent to the server?",

[

"Cookie",

"Local Storage",

"Session Storage",

"IndexedDB"

]

)

if st.button("Check Answer", key="check_answer_cookie"):

    if answer=="Cookie":

        st.success("Correct!")

    else:

        st.error("Incorrect!")

# ==========================================================
# VIVA
# ==========================================================

st.markdown("---")

st.header("🎤 Viva Questions")

st.info("""

1. What is Cookie?

2. Why Cookies?

3. Difference between Cookies and Local Storage?

4. Explain Session Storage.

5. Why shouldn't passwords be stored?

6. Explain Remember Me.

""")

# ==========================================================
# INTERVIEW
# ==========================================================

st.markdown("---")

st.header("💼 Interview Questions")

st.success("""

✔ Cookie vs Local Storage?

✔ Cookie vs Session?

✔ Which is faster?

✔ Which supports authentication?

✔ Why use Cookies?

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

Browser

↓

Cookie

↓

Remember User

↓

Login

↓

Dashboard

""")

st.info("""

➡ Next Chapter

JSON vs XML

""")
import streamlit as st

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📊 JSON vs XML")

st.subheader("Understanding Modern Data Exchange Formats")

st.markdown("---")

# ==========================================================
# LEARNING OUTCOMES
# ==========================================================

st.header("🎯 Learning Outcomes")

st.markdown("""

After completing this lesson students will be able to

✅ Explain XML

✅ Explain JSON

✅ Compare XML and JSON

✅ Identify advantages of JSON

✅ Explain why modern APIs prefer JSON

""")

# ==========================================================
# INTRODUCTION
# ==========================================================

st.markdown("---")

st.header("❓ Why Do We Need Data Exchange?")

st.info("""

Suppose

Browser wants to send data

↓

Server receives data

↓

Server sends response

A common format is required.

Earlier

XML

Today

JSON

""")

# ==========================================================
# XML
# ==========================================================

st.markdown("---")

st.header("📄 XML")

st.code("""

<Student>

    <Name>John</Name>

    <Age>20</Age>

    <Department>BCA</Department>

</Student>

""",language="xml")

st.success("""

XML uses Tags

Similar to HTML

""")

# ==========================================================
# JSON
# ==========================================================

st.markdown("---")

st.header("📦 JSON")

st.code("""

{

"name":"John",

"age":20,

"department":"BCA"

}

""",language="json")

st.success("""

JSON uses

Key : Value

Pairs

""")

# ==========================================================
# VISUAL COMPARISON
# ==========================================================

st.markdown("---")

st.header("⚖ Side-by-Side Comparison")

col1,col2=st.columns(2)

with col1:

    st.subheader("XML")

    st.code("""

<Student>

<Name>

John

</Name>

</Student>

""")

with col2:

    st.subheader("JSON")

    st.code("""

{

"name":"John"

}

""")

# ==========================================================
# DIFFERENCE TABLE
# ==========================================================

st.markdown("---")

st.header("📋 JSON vs XML")

st.table({

"Feature":[

"Readability",

"File Size",

"Parsing",

"Speed",

"Supports Arrays",

"Functions",

"Used in APIs"

],

"JSON":[

"Easy",

"Small",

"Fast",

"Fast",

"Yes",

"No",

"Yes"

],

"XML":[

"Complex",

"Large",

"Slower",

"Slower",

"Limited",

"No",

"Rare Today"

]

})

# ==========================================================
# WHY JSON WON
# ==========================================================

st.markdown("---")

st.header("🏆 Why JSON Became Popular")

st.success("""

✔ Less Code

✔ Lightweight

✔ Faster

✔ Easy to Parse

✔ JavaScript Friendly

✔ API Friendly

✔ Human Readable

""")

# ==========================================================
# WHERE XML IS USED
# ==========================================================

st.markdown("---")

st.header("🌍 Where XML is Still Used")

st.info("""

XML is still used in

✔ Configuration Files

✔ RSS Feeds

✔ Office Documents

✔ Android Layout Files

✔ SOAP Web Services

""")

# ==========================================================
# WHERE JSON IS USED
# ==========================================================

st.markdown("---")

st.header("🌍 Where JSON is Used")

applications=[

"Google Maps",

"Instagram",

"Facebook",

"Amazon",

"Netflix",

"WhatsApp",

"Online Banking",

"Student Portal",

"Hospital Management",

"Weather APIs"

]

for app in applications:

    st.success(app)

# ==========================================================
# DEMONSTRATION
# ==========================================================

st.markdown("---")

st.header("🎮 Which One is Easier?")

choice=st.radio(

"Which format is easier to read?",

["JSON","XML"]

)

if st.button("Show Result", key="show_result"):

    if choice=="JSON":

        st.success("Correct! JSON is simpler and easier to read.")

    else:

        st.info("XML is readable, but JSON is generally simpler.")

# ==========================================================
# REAL PROJECT CONNECTION
# ==========================================================

st.markdown("---")

st.header("💻 Registration Project")

st.code("""

Registration Form

↓

JavaScript Object

↓

JSON

↓

Fetch API

↓

Express Server

↓

JSON

↓

Dashboard

""")

st.warning("""

Notice

Our Registration Project

never used XML.

Modern JavaScript Applications

mostly communicate

using JSON.

""")

# ==========================================================
# BEST PRACTICES
# ==========================================================

st.markdown("---")

st.header("⭐ Best Practices")

st.success("""

✔ Use JSON for APIs

✔ Keep JSON Small

✔ Validate Data

✔ Use Meaningful Keys

✔ Avoid Unnecessary Nesting

""")

# ==========================================================
# COMMON ERRORS
# ==========================================================

st.markdown("---")

st.header("⚠ Common Mistakes")

st.error("""

❌ Missing Quotes

❌ Trailing Commas

❌ Invalid JSON Format

❌ Confusing JSON with JavaScript Objects

""")

# ==========================================================
# ACTIVITY
# ==========================================================

st.markdown("---")

st.header("🎯 Classroom Activity")

st.info("""

Convert your

Student Object

into

✔ JSON

and

✔ XML

Compare

• Readability

• Length

• Ease of Understanding

""")

# ==========================================================
# MCQ
# ==========================================================

st.markdown("---")

st.header("📝 Knowledge Check")

answer=st.radio(

"Which format is preferred by most modern REST APIs?",

["XML","JSON"]

)

if st.button("Check Answer", key="check_answer_json"):

    if answer=="JSON":

        st.success("Correct!")

    else:

        st.error("Incorrect!")

# ==========================================================
# VIVA
# ==========================================================

st.markdown("---")

st.header("🎤 Viva Questions")

st.info("""

1. What is XML?

2. What is JSON?

3. Difference between JSON and XML?

4. Why is JSON more popular?

5. Can XML still be used today?

6. Which format is used in Fetch API?

""")

# ==========================================================
# INTERVIEW
# ==========================================================

st.markdown("---")

st.header("💼 Interview Questions")

st.success("""

✔ Why did JSON replace XML?

✔ Difference between JSON and XML?

✔ Which is faster?

✔ Which format is easier to parse?

✔ Which format is used in REST APIs?

""")

# ==========================================================
# SUMMARY
# ==========================================================

st.markdown("---")

st.success("""

XML

↓

Older Technology

↓

JSON

↓

Modern APIs

↓

Fetch API

↓

Express.js

""")

st.info("""

➡ Next Chapter

🚀 Express.js

Building Registration → Login → Dashboard

""")
