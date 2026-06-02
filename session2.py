import streamlit as st
from google import genai
from pypdf import PdfReader

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Full Stack Development - Unit 1",
    page_icon="🌐",
    layout="wide"
)

# ==========================================
# PDF FUNCTIONS
# ==========================================

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

    context = ""

    context += read_pdf(
        "Data/course_plan_doc.pdf"
    )

    context += "\n"

    context += read_pdf(
        "Data/course_plan_espro.pdf"
    )

    return context


course_context = load_course_documents()

# ==========================================
# PAGE TITLE
# ==========================================

st.title("🌐 Full Stack Development")

st.subheader(
    "Unit 1: Building a Modern Responsive Landing Page"
)

# ==========================================
# LAYOUT
# ==========================================

content_col, chat_col = st.columns([3, 1])

# ==========================================
# AI TUTOR
# ==========================================

with chat_col:

    st.markdown("## 🤖 AI Tutor")

    st.caption(
        "Ask doubts related to Unit 1, assessments, HTML, CSS, Tailwind or Full Stack concepts."
    )

    quick_question = st.selectbox(
        "Quick Questions",
        [
            "",
            "What is HTML5?",
            "Explain Semantic Tags",
            "Explain Flexbox",
            "What is Tailwind CSS?",
            "Difference between div and section",
            "Explain Responsive Design",
            "What is a Hero Section?",
            "Why use Font Awesome?"
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
You are Prof. Vijay's Full Stack Development AI Tutor.

Primary Goal:
Help students understand concepts,
prepare for assessments,
complete lab activities,
and build practical skills.

Course Documents:

{course_context}

Instructions:

1. Use course documents as the primary source.

2. Explain concepts clearly.

3. Provide:
   - Definitions
   - Historical background
   - Real-world examples
   - Code samples
   - Best practices

4. Connect answers to Full Stack Development.

5. For assessment questions,
   prioritize course document information.

6. For coding questions,
   provide examples.

7. Keep answers student-friendly.

Student Question:

{question}
"""

        try:

            with st.spinner("Thinking..."):

                client = genai.Client(
                    api_key=st.secrets["GEMINI_API_KEY"]
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.success("Response Generated")

            st.markdown(
                response.text
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

# ==========================================
# COURSE CONTENT
# ==========================================

with content_col:

    st.info("""
Learning Outcomes

• Understand HTML5 Semantic Elements

• Understand Tailwind CSS

• Understand Responsive Design

• Build Navbar, Hero Section,
  Cards and Footer
""")