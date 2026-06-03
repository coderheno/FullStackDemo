import streamlit as st
from google import genai
from pypdf import PdfReader

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Full Stack Development Portal",
    page_icon="🌐",
    layout="wide"
)

# =====================================
# PDF READER
# =====================================

def read_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# =====================================
# LOAD COURSE DOCUMENTS
# =====================================

@st.cache_resource
def load_course_documents():

    context = ""

    try:

        context += read_pdf(
            "Data/course_plan_doc.pdf"
        )

        context += "\n"

        context += read_pdf(
            "Data/course_plan_espro.pdf"
        )

    except Exception as e:

        context = f"PDF Loading Error: {e}"

    return context


course_context = load_course_documents()

# =====================================
# HEADER
# =====================================

st.title(
    "🌐 Full Stack Development Course Portal"
)

st.markdown("""
Learn:

✅ HTML5

✅ Tailwind CSS

✅ JavaScript

✅ React

✅ Node.js

✅ MongoDB

✅ Git & GitHub
""")

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/1055/1055687.png",
        width=100
    )

    st.title(
        "Navigation"
    )

    menu = st.radio(
        "Select Module",
        [
            "Course Overview",
            "Unit 1",
            "Lab Manual",
            "Activities",
            "MCQ Practice",
            "AI Tutor"
        ]
    )

# =====================================
# MAIN LAYOUT
# =====================================

content_col, chat_col = st.columns(
    [3,1]
)
# =====================================
# COURSE OVERVIEW
# =====================================

with content_col:

    if menu == "Course Overview":

        st.header(
            "📘 Course Overview"
        )

        st.subheader(
            "Course Outcomes"
        )

        st.markdown("""
### CO1

Apply HTML5 semantic features,
Git version control and Tailwind CSS.

### CO2

Implement JavaScript for forms,
events and browser APIs.

### CO3

Develop React applications.

### CO4

Develop Node.js applications.

### CO5

Develop Full Stack applications
using MongoDB.
""")

        st.subheader(
            "Week 1 Plan"
        )

        st.markdown("""
### Session 1

- Full Stack Introduction
- HTML5 Basics
- Semantic Elements

### Session 2

- Tailwind CSS
- Responsive Design

### Session 3

- Git
- GitHub
- Deployment
""")

        st.success(
            "Goal: Build and publish your first webpage."
        )
# =====================================
# UNIT 1
# =====================================

with content_col:

    if menu == "Unit 1":

        st.header(
            "📚 Unit 1 : HTML5, Tailwind CSS and Git"
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "HTML5",
                "Semantic Tags",
                "Canvas & Media"
            ]
        )

        # ============================
        # TAB 1
        # ============================

        with tab1:

            st.subheader(
                "Introduction to HTML5"
            )

            st.markdown("""
### What is HTML?

HTML stands for:

**Hyper Text Markup Language**

HTML is used to structure web pages.

HTML is not a programming language.

It is a markup language that tells the browser how content should be displayed.

---

### Why HTML5?

HTML5 introduced:

- Semantic Elements
- Audio Support
- Video Support
- Canvas
- Geolocation APIs
- Local Storage APIs
- Better Accessibility

---

### Basic HTML Structure
""")

            st.code(
"""
<!DOCTYPE html>
<html>

<head>
    <title>My First Page</title>
</head>

<body>

    <h1>Hello World</h1>

</body>

</html>
""",
                language="html"
            )

            st.success(
                "Every webpage begins with the <!DOCTYPE html> declaration."
            )

            st.info(
                "Think of HTML as the skeleton of a website."
            )

        # ============================
        # TAB 2
        # ============================

        with tab2:

            st.subheader(
                "HTML5 Semantic Elements"
            )

            st.markdown("""
### What are Semantic Tags?

Semantic tags describe the meaning
of content rather than its appearance.

They make webpages:

- Easier to read
- Easier to maintain
- Better for SEO
- Better for Accessibility
""")

            st.code(
"""
<header>
<nav>
<main>
<section>
<article>
<footer>
""",
                language="html"
            )

            st.markdown("""
### Common Semantic Elements

#### header

Contains:

- Logo
- Website Name
- Navigation

#### nav

Contains:

- Menu Links
- Navigation Options

#### main

Main content of webpage.

#### section

Logical grouping of content.

#### article

Independent content block.

#### footer

Copyright information,
contact details and links.
""")

            st.success(
                "Search engines understand semantic tags better than generic div tags."
            )
        # ============================
        # TAB 3
        # ============================

        with tab3:

            st.subheader(
                "HTML5 Canvas and Media Elements"
            )

            st.markdown("""
### Canvas Element

The Canvas element provides a
drawing area for graphics.

Applications:

- Games
- Charts
- Drawing Applications
- Animations

Syntax:
""")

            st.code(
"""
<canvas
    id="myCanvas"
    width="300"
    height="200">
</canvas>
""",
                language="html"
            )

            st.markdown("""
### Audio Element

HTML5 allows embedding audio directly
without external plugins.
""")

            st.code(
"""
<audio controls>

<source
src="music.mp3"
type="audio/mpeg">

</audio>
""",
                language="html"
            )

            st.markdown("""
### Video Element

HTML5 supports video playback
without Flash Player.
""")

            st.code(
"""
<video
width="500"
controls>

<source
src="movie.mp4"
type="video/mp4">

</video>
""",
                language="html"
            )

            st.success(
                "HTML5 eliminated the dependency on external multimedia plugins."
            )

        # =================================
        # SEMANTIC LAYOUT VISUALIZATION
        # =================================

        st.divider()

        st.subheader(
            "HTML5 Semantic Page Layout"
        )

        st.code(
"""
----------------------------------
|            HEADER              |
----------------------------------
|              NAV               |
----------------------------------
|             MAIN               |
|                                |
|  SECTION 1                     |
|  ARTICLE                       |
|                                |
|  SECTION 2                     |
|                                |
----------------------------------
|            FOOTER              |
----------------------------------
"""
        )

        st.info(
            "This is the recommended structure for most modern webpages."
        )

        st.subheader(
            "Real World Example"
        )

        st.markdown("""
### Online Learning Website

#### Header

Logo + Website Name

#### Navigation

Home | Courses | Contact

#### Main

Course Content

#### Section

Python Programming

#### Article

Lesson Details

#### Footer

Copyright Information
""")

        st.success(
            "Students should map semantic tags to real-world webpages."
        )

        st.divider()
with content_col:

    if menu == "Lab Manual":
        st.header(
            "🧪 Lab Exercise 1"
        )

        st.markdown("""
### Exercise 1

Create a webpage for any of the domain:

- Restaurant
- Travel Agency
- NGO
- College Club
- Fitness Center
- Startup Company

Requirements:

✔ Header

✔ Navigation Bar

✔ Main Section

✔ Two Content Sections

✔ Footer

✔ At least one Semantic Element

✔ Proper Page Title
""")
        
        st.markdown("""
## Experiment No: 1

### Title

Design a Semantic HTML5 Webpage

### Objective

To develop a structured webpage
using HTML5 semantic elements.

### Software Required

- VS Code
- Chrome Browser
- Git
- GitHub Account

### Outcome

Students will be able to:

- Create HTML5 webpages
- Apply semantic tags
- Structure webpage content
- Understand webpage hierarchy
""")

        st.divider()

        st.subheader(
            "Procedure"
        )

        st.markdown("""
### Step 1

Open VS Code.

### Step 2

Create:

index.html

### Step 3

Add HTML5 document structure.

### Step 4

Insert:

- Header
- Navigation
- Main Content
- Footer

### Step 5

Save the file.

### Step 6

Run in Browser.

### Step 7

Verify webpage output.
""")

        st.divider()

        st.subheader(
            "Sample Solution"
        )

        st.code(
"""
<!DOCTYPE html>

<html>

<head>

<title>My Website</title>

</head>

<body>

<header>

<h1>My Website</h1>

</header>

<nav>

<a href="#">Home</a>

<a href="#">About</a>

</nav>

<main>

<section>

<h2>Welcome</h2>

<p>Hello World</p>

</section>

</main>

<footer>

Copyright 2026

</footer>

</body>

</html>
""",
            language="html"
        )

        st.success(
            "Students may enhance the design using Tailwind CSS."
        )

        st.divider()

        st.header(
            "🔧 Git Introduction"
        )

        st.markdown("""
Git is a Version Control System.

Git helps developers:

- Track Changes
- Collaborate
- Restore Previous Versions
- Manage Software Projects

Git was developed by:

Linus Torvalds
""")

        st.info(
            "Think of Git as an Undo System for Software Projects."
        )
        st.divider()

        st.header(
            "🚀 Git Workflow"
        )

        st.markdown("""
### Typical Git Workflow

1. Create Project

2. Initialize Git Repository

3. Add Files

4. Commit Changes

5. Push to GitHub

6. Continue Development
""")

        st.code(
"""
Project Folder

↓

git init

↓

git add .

↓

git commit -m "Initial Commit"

↓

git push

↓

GitHub Repository
"""
        )

        st.success(
            "Every professional software project follows a version control workflow."
        )

        st.divider()

        st.subheader(
            "Essential Git Commands"
        )

        st.code(
"""
git init

git status

git add .

git commit -m "First Commit"

git log

git push
""",
            language="bash"
        )

        st.info(
            "Students should practice each command at least once during Week 1."
        )

        st.divider()

        st.header(
            "🌐 GitHub Introduction"
        )

        st.markdown("""
GitHub is a cloud-based platform
used to host Git repositories.

Benefits:

✔ Backup Source Code

✔ Team Collaboration

✔ Portfolio Development

✔ Open Source Contributions

✔ Project Sharing
""")

        st.success(
            "Every student should create a GitHub account during Week 1."
        )

        st.divider()
with content_col:

    if menu == "Activities":
        st.header(
            "🤝 Share-Pair-Build Activity"
        )

        st.markdown("""
### Activity Theme

Build Your First Modern Webpage

### Team Formation

Pair:

✔ One student with prior HTML knowledge

✔ One student with limited HTML knowledge

### Goal

Learn through collaboration.

Strong students become mentors.
New students gain confidence.
""")

        st.markdown("""
### Domain Choices

Choose any one:

- Restaurant
- NGO
- Travel Agency
- Startup
- Fitness Center
- College Club
- Online Learning Platform
- Smart Farming
""")
        st.subheader(
            "Activity Requirements"
        )

        st.markdown("""
### Mandatory Requirements

Your webpage must include:

✔ HTML5 Semantic Elements

✔ Header

✔ Navigation Bar

✔ Hero Section

✔ Two Content Sections

✔ Footer

✔ Meaningful Content

✔ Proper Title

✔ Git Repository

✔ GitHub Upload
""")

        st.divider()

        st.header(
            "🤖 Responsible AI Guidelines"
        )

        st.warning(
            "AI is a learning assistant, not a replacement for understanding."
        )

        st.markdown("""
### AI Usage Policy

Students may use:

- ChatGPT
- Gemini
- GitHub Copilot

for:

✔ Idea Generation

✔ Code Suggestions

✔ Debugging

✔ Learning Concepts

Students should NOT:

❌ Submit code they cannot explain

❌ Blindly copy AI-generated solutions

❌ Depend entirely on AI

### Rule

50% AI Assistance

50% Human Understanding
""")

        st.success(
            "If AI generates code, students must explain the purpose of each section."
        )

        st.divider()

        st.header(
            "📝 Reflection Sheet"
        )

        st.markdown("""
Each team must answer:

### Question 1

What domain did you choose?

### Question 2

What semantic elements did you use?

### Question 3

What Git commands did you use?

### Question 4

What prompts were given to AI?

### Question 5

What did you personally learn?

### Question 6

What improvements would you make in Version 2?
""")

        st.divider()

        st.header(
            "📊 Assessment Rubric"
        )

        rubric_data = {
            "Criteria": [
                "HTML5 Structure",
                "Semantic Elements",
                "Creativity",
                "Git & GitHub Usage",
                "Explanation & Reflection"
            ],
            "Marks": [
                2,
                2,
                2,
                2,
                2
            ]
        }

        st.table(rubric_data)

        st.success(
            "Total Marks = 10"
        )

        st.divider()

        st.header(
            "🏆 Awards for Participants"
        )

        st.markdown("""
### Award Categories

🏆 Best Design

🏆 Best Teamwork

🏆 Best Beginner Mentor

🏆 Best AI Prompt

🏆 Most Creative Domain

🏆 Best GitHub Repository
""")

        st.info(
            "The goal is learning, collaboration and creativity."
        )
# =====================================
# MCQ PRACTICE MODULE
# =====================================

with content_col:

    if menu == "MCQ Practice":

        st.header(
            "🎯 CO1 MCQ Practice"
        )

        st.info(
            "Attempt the quiz and check your understanding of HTML5, Semantic Elements, Git and Tailwind CSS."
        )

        score = 0

        # ==================================
        # QUESTION 1
        # ==================================

        q1 = st.radio(
            "1. Which HTML5 tag represents the main content of a webpage?",
            [
                "header",
                "main",
                "footer",
                "nav"
            ],
            key="q1"
        )

        if q1 == "main":
            score += 1

        # ==================================
        # QUESTION 2
        # ==================================

        q2 = st.radio(
            "2. Which semantic tag is primarily used for navigation links?",
            [
                "section",
                "article",
                "nav",
                "footer"
            ],
            key="q2"
        )

        if q2 == "nav":
            score += 1

        # ==================================
        # QUESTION 3
        # ==================================

        q3 = st.radio(
            "3. Which Git command initializes a repository?",
            [
                "git add",
                "git commit",
                "git init",
                "git push"
            ],
            key="q3"
        )

        if q3 == "git init":
            score += 1

        # ==================================
        # QUESTION 4
        # ==================================

        q4 = st.radio(
            "4. Tailwind CSS is a ______ framework.",
            [
                "Database",
                "Utility First",
                "Backend",
                "Version Control"
            ],
            key="q4"
        )

        if q4 == "Utility First":
            score += 1

        # ==================================
        # QUESTION 5
        # ==================================

        q5 = st.radio(
            "5. Which HTML5 element is used for independent content?",
            [
                "article",
                "nav",
                "footer",
                "header"
            ],
            key="q5"
        )

        if q5 == "article":
            score += 1

        st.divider()

        st.markdown(
            "### Click Submit after answering all questions"
        )
        # ==================================
        # QUESTION 6
        # ==================================

        q6 = st.radio(
            "6. Which HTML5 element usually contains copyright information?",
            [
                "main",
                "footer",
                "article",
                "section"
            ],
            key="q6"
        )

        if q6 == "footer":
            score += 1

        # ==================================
        # QUESTION 7
        # ==================================

        q7 = st.radio(
            "7. Which command stages all modified files?",
            [
                "git commit",
                "git status",
                "git add .",
                "git push"
            ],
            key="q7"
        )

        if q7 == "git add .":
            score += 1

        # ==================================
        # QUESTION 8
        # ==================================

        q8 = st.radio(
            "8. Which Tailwind class applies padding?",
            [
                "bg-blue-500",
                "p-4",
                "text-white",
                "rounded"
            ],
            key="q8"
        )

        if q8 == "p-4":
            score += 1

        # ==================================
        # QUESTION 9
        # ==================================

        q9 = st.radio(
            "9. Which HTML5 feature is used to draw graphics?",
            [
                "audio",
                "canvas",
                "video",
                "section"
            ],
            key="q9"
        )

        if q9 == "canvas":
            score += 1

        # ==================================
        # QUESTION 10
        # ==================================

        q10 = st.radio(
            "10. Why are semantic tags preferred over generic div tags?",
            [
                "Reduce internet usage",
                "Improve readability and SEO",
                "Increase file size",
                "Replace CSS"
            ],
            key="q10"
        )

        if q10 == "Improve readability and SEO":
            score += 1

        st.divider()

        # ==================================
        # SUBMIT BUTTON
        # ==================================

        if st.button(
            "📊 Submit Quiz"
        ):

            st.subheader(
                "Quiz Result"
            )

            st.metric(
                "Score",
                f"{score}/10"
            )

            progress = score / 10

            st.progress(
                progress
            )

            # =============================
            # FEEDBACK
            # =============================

            if score >= 9:

                st.success(
                    "Excellent! You have a strong understanding of Unit 1 concepts."
                )

            elif score >= 7:

                st.success(
                    "Good Job! Revise Git and Semantic Elements for better mastery."
                )

            elif score >= 5:

                st.warning(
                    "Fair Performance. Review HTML5, Git and Tailwind CSS concepts."
                )

            else:

                st.error(
                    "Needs Improvement. Revisit the notes and lab exercises."
                )

            st.balloons()

            st.info(
                "Tip: Use the AI Tutor to clarify concepts before attempting the quiz again."
            )