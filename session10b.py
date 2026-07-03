import streamlit as st

st.set_page_config(page_title="React Attendance App Explanation", layout="wide")

st.title("📘 React Student Attendance App - Complete Code Explanation")
st.write("This application explains every part of the React Student Attendance program.")

tab1, tab2, tab3 = st.tabs([
    "Part 1: State Variables",
    "Part 2: JSX & UI",
    "Part 3: Program Flow"
])

# ---------------------------------------------------
# PART 1
# ---------------------------------------------------
with tab1:

    st.header("1. React State Variables")

    st.code("""
function App() {

  const [name, setName] = useState("");
  const [regNo, setRegNo] = useState("");
  const [course, setCourse] = useState("");
  const [status, setStatus] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const submitAttendance = () => {
      setSubmitted(true);
  };
""", language="javascript")

    st.subheader("Explanation")

    st.markdown("""
### `function App()`
- Creates the React Functional Component.

---

### `const [name, setName] = useState("");`
- Stores the student's name.
- Initial value is an empty string.
- `setName()` updates the value.

Example:

```javascript
setName("John")
const [regNo, setRegNo] = useState("");
Stores the Register Number.

Example:

setRegNo("23MCA001")
const [course, setCourse] = useState("");
Stores the selected course.

Example:

setCourse("MCA")
const [status, setStatus] = useState("");
Stores attendance status.

Possible values:

Present
Absent
const [submitted, setSubmitted] = useState(false);
Indicates whether the form has been submitted.
Initially false.
Changes to true after clicking Submit.
submitAttendance()
const submitAttendance = () =>{
    setSubmitted(true);
}
Executes when Submit button is clicked.
Updates the submitted state.
React automatically refreshes the UI.
""")
#---------------------------------------------------
#PART 2
#---------------------------------------------------

with tab2:

    st.header("2. JSX User Interface")

    st.code("""

return (

<div style={{ width:"450px", margin:"30px auto", fontFamily:"Arial" }} > <h1>Student Attendance</h1>

<input
type="text"
placeholder="Student Name"
value={name}
onChange={(e)=>setName(e.target.value)}
/>

<br/><br/>

<input
type="text"
placeholder="Register Number"
value={regNo}
onChange={(e)=>setRegNo(e.target.value)}
/>

<br/><br/>

<select
value={course}
onChange={(e)=>setCourse(e.target.value)}

<option value="">Select Course</option> <option>BCA</option> <option>MCA</option> <option>BSc</option> </select>

<br/><br/>

<label>

<input
type="radio"
value="Present"
checked={status==="Present"}
onChange={(e)=>setStatus(e.target.value)}
/>

Present

</label>

  

<label>

<input
type="radio"
value="Absent"
checked={status==="Absent"}
onChange={(e)=>setStatus(e.target.value)}
/>

Absent

</label>

<br/><br/>

<button onClick={submitAttendance}> Submit Attendance </button>

{submitted && (

<div style={{ marginTop:"20px", border:"1px solid gray", padding:"15px", borderRadius:"10px" }} > <h2>Attendance Details</h2> <p><b>Name :</b> {name}</p> <p><b>Register No :</b> {regNo}</p> <p><b>Course :</b> {course}</p> <p><b>Status :</b> {status}</p> <h3 style={{color:"green"}}> ✔ Attendance Recorded Successfully </h3> </div>

)}

</div>

);

}

export default App;
""", language="javascript")

st.subheader("Step-by-Step Explanation")

explanations = [
    ("return()", "Returns the JSX that React displays on the webpage."),
    ("Main div", "Creates the main container for the attendance form."),
    ("width", "Sets container width to 450 pixels."),
    ("margin", "Centers the form horizontally."),
    ("fontFamily", "Uses Arial font."),
    ("<h1>", "Displays the heading 'Student Attendance'."),
    ("Student Name Input", "Text field for entering the student's name."),
    ("value={name}", "Displays the value stored in the name state."),
    ("onChange", "Updates the state whenever the user types."),
    ("Register Number", "Stores the student's register number."),
    ("Dropdown", "Allows the user to choose BCA, MCA, or BSc."),
    ("Radio Button", "Selects Present or Absent."),
    ("checked", "Checks whether the selected option matches the state."),
    ("Submit Button", "Calls submitAttendance() when clicked."),
    ("submitted && (...)", "Conditional rendering. Displays results only after submission."),
    ("Result Box", "Shows attendance details inside a bordered box."),
    ("Success Message", "Displays 'Attendance Recorded Successfully'."),
    ("export default App", "Exports the component so React can render it.")
]

for title, desc in explanations:
    st.markdown(f"**{title}**")
    st.write(desc)
#---------------------------------------------------
#PART 3
#---------------------------------------------------

with tab3:

    st.header("3. Program Flow")

    st.markdown("""
Start Application
        │
        ▼
Display Attendance Form
        │
        ▼
Enter Student Name
        │
        ▼
setName()
        │
        ▼
Enter Register Number
        │
        ▼
setRegNo()
        │
        ▼
Select Course
        │
        ▼
setCourse()
        │
        ▼
Choose Present / Absent
        │
        ▼
setStatus()
        │
        ▼
Click Submit
        │
        ▼
submitAttendance()
        │
        ▼
setSubmitted(true)
        │
        ▼
React Re-renders the Page
        │
        ▼
Attendance Details Displayed
        │
        ▼
✔ Attendance Recorded Successfully

""")

st.success("Summary")

st.markdown("""
Important React Concepts
Functional Component – function App()
JSX – HTML-like syntax inside JavaScript.
useState() – Stores dynamic data.
onChange Event – Updates state while typing.
onClick Event – Executes a function when a button is clicked.
Conditional Rendering – Displays content only when a condition is true.
React Re-rendering – Automatically updates the UI whenever the state changes.
""")