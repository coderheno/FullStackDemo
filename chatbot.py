import google.generativeai as genai
import streamlit as st
from pypdf import PdfReader
import os
import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

st.set_page_config(
    page_title="Full Stack AI Assistant",
    page_icon="🤖",
    layout="wide"
)

from pypdf import PdfReader

def read_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


@st.cache_resource
def load_course_documents():

    text = ""

    text += read_pdf(
        "Data/course_plan_doc.pdf"
    )

    text += "\n"

    text += read_pdf(
        "Data/course_plan_espro.pdf"
    )

    return text


course_context = load_course_documents()
 

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

for m in genai.list_models():
    print(m.name)
import streamlit as st
import google.generativeai as genai

# ----------------------------------
# Configure Gemini
# ----------------------------------

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# ----------------------------------
# Page Config
# ----------------------------------


st.title("🤖 Full Stack AI Assistant")

st.info("""
Ask questions about:

• HTML5
• CSS & Tailwind CSS
• JavaScript
• React
• Node.js
• MongoDB
• Next.js
• Git & GitHub
• Assessments
• Course Outcomes
""")

# ----------------------------------
# Sidebar
# ----------------------------------

st.sidebar.header("Sample Questions")

st.sidebar.write("""
• What is HTML5 Semantic Tag?

• Explain Flexbox

• Difference between React and Next.js

• What is JSON?

• Explain Git Merge Conflict

• What is CO2?

• Explain CIA II Assessment
""")

# ----------------------------------
# Session State
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------------
# Course Context
# ----------------------------------

course_context = """
You are an MCA Full Stack Development Course Assistant.

Course Outcomes:

CO1:
Apply HTML5 semantic features, Git and Tailwind CSS.

CO2:
Implement JavaScript forms, events,
browser features and JSON APIs.

CO3:
Develop React applications using
components, hooks and routing.

CO4:
Develop server-side applications using
Node.js, Express.js and MongoDB.

CO5:
Develop applications using Next.js.

Assessments:

CIA I:
MCQ Assessment

CIA II:
Problem Solving + Prototyping + Documentation

CIA III:
Lab Test

CIA IV:
Regular Lab Exercises

Lab End Examination:
Comprehensive Full Stack Development Lab Exam

Always answer as a course assistant.
Keep answers clear and student friendly.
"""

# ----------------------------------
# User Input
# ----------------------------------

question = st.chat_input(
    "Ask your Full Stack question..."
)

# ----------------------------------
# Chat Processing
# ----------------------------------

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    prompt = f"""
You are an AI Full Stack Development Teaching Assistant.

Primary Responsibility:
Help students learn the Full Stack Development course.

Course Documents:

{course_context}

Instructions:

1. Use the course documents as the PRIMARY source of truth for:
   - Course Outcomes (COs)
   - Units and Topics
   - Assessments
   - Lab Exercises
   - Rubrics
   - Evaluation Schemes
   - Course Policies

2. When students ask conceptual questions,
   provide educational explanations that support learning.

3. You may provide:
   - Definitions
   - Historical background
   - Real-world examples
   - Code examples
   - Best practices
   - Industry insights
   - Interview tips
   - Project ideas

4. Keep answers aligned with the syllabus whenever possible.

5. If a topic is outside the syllabus,
   answer briefly and explain its relevance to Full Stack Development.

6. For programming questions:
   - Explain the concept first.
   - Then provide code examples.
   - Mention common mistakes.
   - Suggest practical applications.

7. For assessment-related questions:
   prioritize information from the course documents.

8. Use student-friendly language.

Student Question:

{question}
"""


    try:

        with st.spinner("Thinking..."):

            response = model.generate_content(
                prompt
            )

        answer = response.text

    except Exception as e:

        answer = f"Error: {e}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ----------------------------------
# Display Chat
# ----------------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])

# ----------------------------------
# Clear Chat
# ----------------------------------

if st.sidebar.button("Clear Chat"):

    st.session_state.messages = []

    st.rerun()