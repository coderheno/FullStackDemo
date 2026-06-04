import streamlit as st

st.set_page_config(
    page_title="Tailwind CSS Tutorial",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Tailwind CSS Interactive Tutorial")

st.sidebar.title("Topics")

topic = st.sidebar.radio(
    "Select Topic",
    [
        "Introduction",
        "Utility Classes",
        "Flexbox",
        "Grid",
        "Positioning",
        "Responsive Classes",
        "Responsive Web Design",
        "Responsive Images",
        "State Variants",
        "Arbitrary Values",
        "Tailwind Attributes",
        "Reading Tailwind Classes",
        "Card Component Example",
        "Tailwind Cheat Sheet"
    ]
)

# ==================================================
# INTRODUCTION
# ==================================================

if topic == "Introduction":

    st.header("Introduction")

    st.write("""
Tailwind CSS is a utility-first CSS framework.

Instead of writing custom CSS rules, you build designs
by adding predefined utility classes directly to HTML elements.
""")

    st.subheader("Traditional CSS")

    st.code("""
.card {
    background-color: blue;
    padding: 16px;
    border-radius: 8px;
}
""", language="css")

    st.subheader("Tailwind CSS")

    st.code("""
<div class="bg-blue-500 p-4 rounded-lg">
    Card Content
</div>
""", language="html")

# ==================================================
# UTILITY CLASSES
# ==================================================
elif topic == "Flexbox":

    st.header("Flexbox")

    st.write("""
Flexbox is used to align and distribute items
within a container.
""")

    st.code("""
<div class="flex">
    <div>Item 1</div>
    <div>Item 2</div>
</div>
""", language="html")

    st.subheader("Direction")

    st.code("""
flex-row
flex-col
""")

    st.subheader("Horizontal Alignment")

    st.code("""
justify-start
justify-center
justify-between
justify-around
justify-evenly
""")

    st.subheader("Vertical Alignment")

    st.code("""
items-start
items-center
items-end
""")

    st.subheader("Example")

    st.code("""
<div class="flex justify-center items-center h-screen">
    Centered Content
</div>
""", language="html")
elif topic == "Grid":

    st.header("CSS Grid")

    st.code("""
<div class="grid grid-cols-3 gap-4">
    <div>1</div>
    <div>2</div>
    <div>3</div>
</div>
""", language="html")

    st.subheader("Common Grid Classes")

    st.code("""
grid
grid-cols-1
grid-cols-2
grid-cols-3
grid-cols-4

gap-2
gap-4
gap-8
""")

    st.success("""
Grid is perfect for dashboards,
card layouts and galleries.
""")
elif topic == "Positioning":

    st.header("Positioning")

    st.code("""
relative
absolute
fixed
sticky
""")

    st.subheader("Position Helpers")

    st.code("""
top-0
bottom-0
left-0
right-0
""")

    st.subheader("Example")

    st.code("""
<div class="relative">

    <div class="absolute top-0 right-0">
        Badge
    </div>

</div>
""", language="html")
elif topic == "Responsive Web Design":

    st.header("Responsive Design Fundamentals")

    st.subheader("Viewport Meta Tag")

    st.code("""
<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0">
""", language="html")

    st.info("""
Without the viewport tag,
mobile browsers may render pages as desktop layouts.
""")

    st.subheader("Responsive Principles")

    st.markdown("""
- Use flexible widths
- Use Grid and Flexbox
- Avoid fixed pixel layouts
- Use responsive breakpoints
- Make images responsive
""")
elif topic == "Responsive Images":

    st.header("Responsive Images")

    st.subheader("Tailwind Method")

    st.code("""
<img
    src="photo.jpg"
    class="w-full h-auto">
""", language="html")

    st.subheader("Picture Element")

    st.code("""
<picture>
    <source
        media="(min-width:800px)"
        srcset="desktop.jpg">

    <img
        src="mobile.jpg"
        alt="Image">
</picture>
""", language="html")

    st.success("""
w-full ensures the image never exceeds
its container width.
""")
elif topic == "Reading Tailwind Classes":

    st.header("Reading Tailwind Class Strings")

    st.code("""
class="
flex
items-center
justify-between
p-4
bg-white
shadow-lg
rounded-xl
"
""")

    st.table({
        "Class":[
            "flex",
            "items-center",
            "justify-between",
            "p-4",
            "bg-white",
            "shadow-lg",
            "rounded-xl"
        ],
        "Meaning":[
            "Flex Layout",
            "Vertical Center",
            "Space Between Items",
            "Padding",
            "White Background",
            "Large Shadow",
            "Rounded Corners"
        ]
    })
elif topic == "Tailwind Cheat Sheet":

    st.header("Tailwind Cheat Sheet")

    st.markdown("""
### Layout
- flex
- grid
- block
- hidden

### Spacing
- p-4
- px-4
- py-4
- m-4
- mx-auto

### Colors
- bg-blue-500
- text-red-500
- border-green-500

### Typography
- text-xl
- font-bold
- text-center

### Borders
- border
- rounded-lg
- rounded-full

### Flexbox
- justify-center
- justify-between
- items-center

### Grid
- grid-cols-2
- grid-cols-3
- gap-4

### Responsive
- sm:
- md:
- lg:
- xl:
- 2xl:

### States
- hover:
- focus:
- active:
- dark:
""")

    st.success("""
If you understand Layout, Spacing, Colors,
Flexbox, Grid, Responsive Classes and State Variants,
you already know about 80% of Tailwind used in real projects.
""")

elif topic == "Utility Classes":

    st.header("Common Utility Classes")

    st.subheader("Class Structure")

    st.code("""
property-value
""")

    st.table({
        "Class":[
            "text-center",
            "bg-red-500",
            "p-4",
            "m-2",
            "font-bold",
            "rounded-lg"
        ],
        "Meaning":[
            "Center Text",
            "Red Background",
            "Padding",
            "Margin",
            "Bold Text",
            "Large Border Radius"
        ]
    })

    st.subheader("Colors")

    st.code("""
<p class="text-red-500">Red Text</p>
<p class="text-blue-700">Blue Text</p>

<div class="bg-green-500">
    Content
</div>
""", language="html")

    st.info("""
Color Scale:

50
100
200
300
400
500
600
700
800
900
950
""")

    st.subheader("Spacing")

    st.code("""
p-4

pt-4
pb-4
pl-4
pr-4

px-4
py-4

m-4
mt-4
mb-4
mx-auto
""")

    st.code("""
<div class="w-64 mx-auto">
    Centered
</div>
""", language="html")

    st.subheader("Typography")

    st.code("""
text-xs
text-sm
text-base
text-lg
text-xl
text-2xl
text-4xl
""")

    st.code("""
font-thin
font-light
font-normal
font-medium
font-semibold
font-bold
font-extrabold
""")

    st.subheader("Width & Height")

    st.code("""
w-32
h-32

w-full
h-full

w-screen
h-screen
""")

    st.subheader("Borders")

    st.code("""
border
border-2
border-4

border-red-500

rounded
rounded-md
rounded-lg
rounded-xl
rounded-full
""")

# ==================================================
# RESPONSIVE DESIGN
# ==================================================

elif topic == "Responsive Classes":

    st.header("Responsive Classes")

    st.table({
        "Prefix":[
            "sm:",
            "md:",
            "lg:",
            "xl:",
            "2xl:"
        ],
        "Width":[
            ">=640px",
            ">=768px",
            ">=1024px",
            ">=1280px",
            ">=1536px"
        ]
    })

    st.code("""
<div class="text-sm md:text-lg lg:text-2xl">
    Responsive Text
</div>
""", language="html")

    st.success("""
Mobile → Small Text

Tablet → Large Text

Desktop → Extra Large Text
""")

# ==================================================
# STATE VARIANTS
# ==================================================

elif topic == "State Variants":

    st.header("State Variants")

    st.subheader("Hover")

    st.code("""
<button class="bg-blue-500 hover:bg-blue-700">
    Hover Me
</button>
""", language="html")

    st.subheader("Focus")

    st.code("""
<input class="focus:border-blue-500">
""", language="html")

    st.subheader("Active")

    st.code("""
<button class="active:bg-red-500">
""", language="html")

    st.subheader("Dark Mode")

    st.code("""
<div class="bg-white dark:bg-gray-900">

<p class="text-black dark:text-white">
""", language="html")

# ==================================================
# ARBITRARY VALUES
# ==================================================

elif topic == "Arbitrary Values":

    st.header("Arbitrary Values")

    st.write("""
Use arbitrary values when predefined
Tailwind values are insufficient.
""")

    st.code("""
<div class="w-[350px]">

<div class="bg-[#1a73e8]">

<div class="mt-[27px]">
""", language="html")

# ==================================================
# ATTRIBUTES
# ==================================================

elif topic == "Tailwind Attributes":

    st.header("Tailwind Attributes")

    st.write("""
Tailwind primarily uses the HTML class attribute.
""")

    st.code("""
<button
class="bg-blue-500 text-white px-4 py-2 rounded">
    Save
</button>
""", language="html")

    st.code("""
<button
class="bg-blue-500 hover:bg-blue-700"
disabled>
    Submit
</button>
""", language="html")

# ==================================================
# CARD COMPONENT
# ==================================================

elif topic == "Card Component Example":

    st.header("Card Component")

    st.code("""
<div class="max-w-sm mx-auto bg-white rounded-xl shadow-md p-6">

    <h2 class="text-xl font-bold mb-2">
        Product Name
    </h2>

    <p class="text-gray-600 mb-4">
        Product description here.
    </p>

    <button
        class="bg-blue-500 hover:bg-blue-700 text-white px-4 py-2 rounded">
        Buy Now
    </button>

</div>
""", language="html")

    st.success("""
A complete card component built without writing custom CSS.
""")
