import streamlit as st

st.set_page_config(
    page_title="HTTP Methods Tutorial",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 HTTP Methods Interactive Tutorial")

st.sidebar.title("Topics")

topic = st.sidebar.radio(
    "Select Topic",
    [
        "Introduction",
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "HEAD",
        "OPTIONS",
        "CONNECT",
        "TRACE",
        "CRUD Mapping",
        "REST API Example",
        "Safe vs Idempotent Methods",
        "Real Life Analogy"
    ]
)

# ==================================================
# INTRODUCTION
# ==================================================

if topic == "Introduction":

    st.header("What are HTTP Methods?")

    st.write("""
HTTP methods (also called HTTP verbs) define
what action a client wants to perform on a server.

Examples:

- GET
- POST
- PUT
- PATCH
- DELETE
- HEAD
- OPTIONS
""")

    st.info("""
Think of HTTP methods as commands sent from
a browser or application to a server.
""")

# ==================================================
# GET
# ==================================================

elif topic == "GET":

    st.header("GET")

    st.write("Retrieve data from the server.")

    st.code("""
GET /users HTTP/1.1
Host: example.com
""")

    st.subheader("Response")

    st.code("""
[
    {"id":1,"name":"Alice"},
    {"id":2,"name":"Bob"}
]
""", language="json")

    st.subheader("HTML Example")

    st.code("""
<form action="/search" method="GET">
    <input name="q">
    <button>Search</button>
</form>
""", language="html")

    st.success("""
GET should not modify data.
Parameters are usually sent in the URL.
""")

# ==================================================
# POST
# ==================================================

elif topic == "POST":

    st.header("POST")

    st.write("Create new resources or send data.")

    st.code("""
POST /users HTTP/1.1
Content-Type: application/json

{
    "name":"John"
}
""")

    st.subheader("HTML Example")

    st.code("""
<form action="/register" method="POST">

    <input name="username">

    <button>Register</button>

</form>
""", language="html")

    st.success("""
POST requests usually create new resources.
Data is sent inside the request body.
""")

# ==================================================
# PUT
# ==================================================

elif topic == "PUT":

    st.header("PUT")

    st.write("Replace an entire resource.")

    st.code("""
PUT /users/1

{
    "id":1,
    "name":"John",
    "age":25
}
""", language="json")

    st.info("""
PUT updates the complete object.
It is idempotent.
""")

# ==================================================
# PATCH
# ==================================================

elif topic == "PATCH":

    st.header("PATCH")

    st.write("Update only specific fields.")

    st.code("""
PATCH /users/1

{
    "age":26
}
""", language="json")

    st.success("""
PATCH performs partial updates.
""")

# ==================================================
# DELETE
# ==================================================

elif topic == "DELETE":

    st.header("DELETE")

    st.code("""
DELETE /users/1
""")

    st.write("""
Removes a resource from the server.
""")

    st.info("""
DELETE is typically idempotent.
""")

# ==================================================
# HEAD
# ==================================================

elif topic == "HEAD":

    st.header("HEAD")

    st.write("""
Returns headers only, without response content.
""")

    st.code("""
HEAD /image.jpg
""")

    st.code("""
HTTP/1.1 200 OK
Content-Length: 524288
Content-Type: image/jpeg
""")

    st.success("""
Useful for checking file size
or whether a resource exists.
""")

# ==================================================
# OPTIONS
# ==================================================

elif topic == "OPTIONS":

    st.header("OPTIONS")

    st.code("""
OPTIONS /users
""")

    st.code("""
Allow: GET, POST, PUT, DELETE
""")

    st.info("""
OPTIONS tells clients what actions
are supported.

Very important in CORS.
""")

# ==================================================
# CONNECT
# ==================================================

elif topic == "CONNECT":

    st.header("CONNECT")

    st.code("""
CONNECT example.com:443
""")

    st.write("""
Used by proxies to establish
secure HTTPS tunnels.
""")

# ==================================================
# TRACE
# ==================================================

elif topic == "TRACE":

    st.header("TRACE")

    st.code("""
TRACE /
""")

    st.write("""
Used for debugging by echoing
the incoming request.
""")

    st.warning("""
TRACE is often disabled for security reasons.
""")

# ==================================================
# CRUD
# ==================================================

elif topic == "CRUD Mapping":

    st.header("CRUD Mapping")

    st.table({
        "CRUD": [
            "Create",
            "Read",
            "Update (Full)",
            "Update (Partial)",
            "Delete"
        ],
        "HTTP Method": [
            "POST",
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ]
    })

# ==================================================
# REST EXAMPLE
# ==================================================

elif topic == "REST API Example":

    st.header("Blog API Example")

    st.table({
        "Action": [
            "Get All Posts",
            "Get One Post",
            "Create Post",
            "Replace Post",
            "Edit Title",
            "Delete Post"
        ],

        "Endpoint": [
            "/posts",
            "/posts/5",
            "/posts",
            "/posts/5",
            "/posts/5",
            "/posts/5"
        ],

        "Method": [
            "GET",
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE"
        ]
    })

# ==================================================
# SAFE & IDEMPOTENT
# ==================================================

elif topic == "Safe vs Idempotent Methods":

    st.header("Safe Methods")

    st.markdown("""
- GET
- HEAD
- OPTIONS
- TRACE
""")

    st.header("Idempotent Methods")

    st.markdown("""
- GET
- PUT
- DELETE
- HEAD
- OPTIONS
""")

    st.subheader("Example")

    st.code("""
DELETE /users/5
DELETE /users/5
DELETE /users/5
""")

    st.success("""
The final state remains identical,
so DELETE is idempotent.
""")

    st.code("""
POST /orders
POST /orders
POST /orders
""")

    st.error("""
POST may create multiple orders,
so it is NOT idempotent.
""")

# ==================================================
# ANALOGY
# ==================================================

elif topic == "Real Life Analogy":

    st.header("Library Analogy")

    st.table({
        "HTTP Method": [
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE",
            "HEAD",
            "OPTIONS",
            "CONNECT",
            "TRACE"
        ],

        "Library Action": [
            "Read a book",
            "Add a book",
            "Replace a book edition",
            "Correct a typo",
            "Remove a book",
            "Check if a book exists",
            "Ask what actions are allowed",
            "Build a secure tunnel",
            "Inspect the request path"
        ]
    })

    st.success("""
Real-world analogies make HTTP methods
much easier to remember.
""")