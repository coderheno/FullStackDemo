import React, { useState } from "react";

function App() {

  const [name, setName] = useState("");

  const [regNo, setRegNo] = useState("");

  const [course, setCourse] = useState("");

  const [status, setStatus] = useState("");

  const [submitted, setSubmitted] = useState(false);

  const submitAttendance = () => {

    setSubmitted(true);

  };

  return (

    <div
      style={{
        width: "450px",
        margin: "30px auto",
        fontFamily: "Arial"
      }}
    >

      <h1>Student Attendance</h1>

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

      >

        <option value="">Select Course</option>

        <option>BCA</option>

        <option>MCA</option>

        <option>BSc</option>

      </select>

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

      &nbsp;&nbsp;

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

      <button onClick={submitAttendance}>

        Submit Attendance

      </button>

      {submitted && (

      <div
      style={{
      marginTop:"20px",
      border:"1px solid gray",
      padding:"15px",
      borderRadius:"10px"
      }}
      >

      <h2>Attendance Details</h2>

      <p><b>Name :</b> {name}</p>

      <p><b>Register No :</b> {regNo}</p>

      <p><b>Course :</b> {course}</p>

      <p><b>Status :</b> {status}</p>

      <h3 style={{color:"green"}}>

      ✔ Attendance Recorded Successfully

      </h3>

      </div>

      )}

    </div>

  );

}

export default App;