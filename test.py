import streamlit as st
from google import genai

st.title("Gemini Test")

st.write("Secret Exists:", "GEMINI_API_KEY" in st.secrets)

if st.button("Test Gemini"):

    try:

        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Say hello"
        )

        st.success(response.text)

    except Exception as e:

        st.error(str(e))