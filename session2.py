import streamlit as st
from google import genai
from pypdf import PdfReader

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Full Stack Development Portal",
    page_icon="🌐",
    layout="wide"
)

# ==========================================
# PDF READER
# ==========================================

def read_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

# ==========================================
# LOAD COURSE DOCUMENTS
# ==========================================

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

# ==========================================
# PAGE HEADER
# ==========================================

st.title("🌐 Full Stack Development")

st.markdown(
    """
Learn:

- HTML5
- Tailwind CSS
- JavaScript
- React
- Node.js
- MongoDB
- Git & GitHub
"""
)

# ==========================================
# TWO COLUMN LAYOUT
# ==========================================

content_col, chat_col = st.columns(
    [3,1]
)

# ==========================================
# LEFT COLUMN
# ==========================================

with content_col:

    st.header(
        "📚 Course Content"
    )

    st.info(
        """
This portal contains:
• Demo Programs
• Lab Exercises
• Course Outcomes
• AI Tutor
"""
    )
    # ======================================
    # TABS
    # ======================================

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📖 Notes",
            "💻 Demo",
            "📝 Activity",
            "🎯 Outcomes"
        ]
    )

    # ======================================
    # NOTES TAB
    # ======================================

    with tab1:

        st.subheader(
            "HTML5, CSS AND GITHUB"
        )

        st.code("HTML5 New Elements – HTML5 Semantics –Canvas – HTML Media –Git-commit –rollback – remote repository – GitHub – merge conflict – CSS specificity rule – Pseudo selectors – media queries – flexbox – responsive  web design – transition –Tailwind responsive grid – Components (Navbar, tables, heroes, carousel, modal etc.,) – font awesome icons. Introduction to Core JavaScript - Use JavaScript to interact with some of the new HTML5 apis")

    # ======================================
    # DEMO TAB
    # ======================================

    with tab2:

        st.subheader(
            "Landing Page Demonstration"
        )

        st.markdown("""
Students will create:

- Header
- Navigation Bar
- Hero Section
- Feature Cards
- Footer
""")
        st.code(
"""
<header class="bg-blue-700 text-white">
    <nav>
        <h1>TechLearn</h1>
    </nav>
</header>

<section>
    <h2>Learn Full Stack Development</h2>
</section>

<footer>
    Copyright 2026
</footer>
""",
            language="html"
        )

    # ======================================
    # ACTIVITY TAB
    # ======================================

    with tab3:

        st.subheader(
            "Exercise 1"
        )

        st.markdown("""
### Responsive Landing Page

Build a landing page using:

- HTML5 Semantic Tags
- Tailwind CSS
- Font Awesome Icons

Requirements:

✔ Header

✔ Navigation Bar

✔ Hero Section

✔ Feature Cards

✔ Footer

Bonus:

✔ Mobile Responsive Design
""")

        st.success(
            "Submission: Push source code to GitHub Repository."
        )

    # ======================================
    # COURSE OUTCOMES TAB
    # ======================================

    with tab4:

        st.subheader(
            "Course Outcomes"
        )

        st.markdown("""
### CO1

Apply HTML5 semantic features,
Git version control and Tailwind CSS
to develop structured websites.

### CO2

Implement client-side scripting using
JavaScript for forms, events,
browser APIs and JSON.

### CO3

Develop dynamic single-page
applications using React.js.

### CO4

Design and optimize applications
using Node.js.

### CO5

Develop Full Stack applications
integrated with MongoDB.
""")

# ==========================================
# RIGHT COLUMN - AI TUTOR
# ==========================================

with chat_col:

    st.header(
        "🤖 AI Tutor"
    )

    st.caption(
        "Ask doubts related to syllabus, assessments, HTML, CSS, JavaScript, React, Git and Full Stack Development."
    )

    quick_question = st.selectbox(
        "Quick Questions",
        [
            "",
            "What is HTML5?",
            "Explain Semantic Tags",
            "Explain Tailwind CSS",
            "Explain Flexbox",
            "What is Git?",
            "What is Exercise 1?",
            "What are the Course Outcomes?"
        ]
    )

    question = st.text_area(
        "Ask Your Question",
        value=quick_question,
        height=120
    )
if st.button(
    "🚀 Ask AI",
    use_container_width=True
):

    prompt = f"""
Course Documents:

{course_context}

Student Question:

{question}

Answer clearly and help students understand concepts.
"""

    try:

        with st.spinner(
            "Thinking..."
        ):

            client = genai.Client(
                api_key=st.secrets["GEMINI_API_KEY"]
            )

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.success(
            "Response Generated"
        )

        st.markdown(
            response.text
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )