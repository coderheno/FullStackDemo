import streamlit as st

st.set_page_config(page_title="Full Stack Development - Unit 1",
                   page_icon="🌐",
                   layout="wide")

st.title("🌐 Full Stack Development")
st.subheader("Unit 1: Building a Modern Responsive Landing Page")

st.info("""
Learning Outcomes:
- Understand HTML5 Semantic Elements
- Understand Tailwind CSS Integration
- Learn Responsive Design Concepts
- Explore Navbar, Hero Section, Cards, and Footer
""")

# ------------------------------------
# Part 1
# ------------------------------------

with st.expander("Part 1: HTML Skeleton", expanded=True):

    st.markdown("### Basic Structure of an HTML5 Document")

    st.code("""
<!DOCTYPE html>
<html>
<head>
<title>TechLearn Academy</title>
</head>
<body>

</body>
</html>
""", language="html")

    st.markdown("""
**Explanation**

- `<!DOCTYPE html>` → Defines HTML5
- `<html>` → Root element
- `<head>` → Metadata section
- `<title>` → Browser tab title
- `<body>` → Visible webpage content
""")

# ------------------------------------
# Part 2
# ------------------------------------

with st.expander("Part 2: Meta Tags"):

    st.code("""
<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1.0">
""", language="html")

    st.markdown("""
### Why UTF-8?
Supports:
- English
- Tamil
- Hindi
- Emoji 😊

### Why Viewport?
Makes websites responsive on mobile devices.
""")

# ------------------------------------
# Part 3
# ------------------------------------

with st.expander("Part 3: Tailwind CSS CDN"):

    st.code("""
<script src="https://cdn.tailwindcss.com"></script>
""", language="html")

    st.markdown("""
Tailwind provides ready-made utility classes.

Example:
""")

    st.code("""
class="bg-blue-700 text-white p-4"
""", language="html")

    st.markdown("""
- bg-blue-700 → Blue background
- text-white → White text
- p-4 → Padding
""")

# ------------------------------------
# Part 4
# ------------------------------------

with st.expander("Part 4: HTML5 Semantic Elements"):

    st.code("""
<header>
<nav>
<main>
<section>
<article>
<footer>
""", language="html")

    semantic_data = {
        "Tag": [
            "header",
            "nav",
            "main",
            "section",
            "article",
            "footer"
        ],
        "Purpose": [
            "Top section",
            "Navigation links",
            "Main content",
            "Logical grouping",
            "Independent content",
            "Bottom information"
        ]
    }

    st.table(semantic_data)

# ------------------------------------
# Part 5
# ------------------------------------

with st.expander("Part 5: Navbar using Flexbox"):

    st.code("""
<nav class="container mx-auto flex
justify-between items-center p-4">
""", language="html")

    st.markdown("""
### Flexbox Classes

- flex → Horizontal layout
- justify-between → Space between items
- items-center → Vertical alignment
- p-4 → Padding
""")

# ------------------------------------
# Part 6
# ------------------------------------

with st.expander("Part 6: Hero Section"):

    st.code("""
<section>
<h2>Learn Full Stack Development</h2>
<p>Build modern web applications...</p>
<button>Get Started</button>
</section>
""", language="html")

    st.markdown("""
Hero Section is the first section users see.

Usually contains:
- Heading
- Description
- Call-to-action button
""")

# ------------------------------------
# Part 7
# ------------------------------------

with st.expander("Part 7: Responsive Grid (Important)"):

    st.code("""
<div class="grid
grid-cols-1
md:grid-cols-2
lg:grid-cols-3">
""", language="html")

    st.markdown("""
### Responsive Behaviour

📱 Mobile → 1 Column

💻 Tablet → 2 Columns

🖥 Desktop → 3 Columns
""")

# ------------------------------------
# Part 8
# ------------------------------------

with st.expander("Part 8: Font Awesome Icons"):

    st.code("""
<i class="fas fa-laptop-code"></i>
""", language="html")

    st.markdown("""
Font Awesome provides ready-made icons:

- Laptop
- Cloud
- Robot
- User
- Phone
- Database
""")

# ------------------------------------
# Part 9
# ------------------------------------

with st.expander("Part 9: Footer"):

    st.code("""
<footer>
© 2026 TechLearn Academy
</footer>
""", language="html")

    st.markdown("""
Footer usually contains:
- Copyright
- Contact details
- Social media links
""")

# ------------------------------------
# Summary
# ------------------------------------

st.success("""
Summary:

HTML5
├── Semantic Structure

Tailwind CSS
├── Styling
├── Layout
├── Responsive Design

Font Awesome
├── Icons

Result:
Modern Responsive Website
""")

# ------------------------------------
# Activity
# ------------------------------------

st.header("🎯 Classroom Activity")

st.markdown("""
Modify the landing page for one of the following domains:

1. Hospital Website
2. Restaurant Website
3. Travel Website
4. NGO Website
5. College Event Website

Tasks:
- Change Website Name
- Change Hero Section
- Add One More Feature Card
- Change Color Theme
""")