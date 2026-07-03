import streamlit as st
import pandas as pd

st.title("EDA of a Dataset")

file = st.file_uploader("Upload CSV File", type="csv")

if file:
    df = pd.read_csv(file)

    st.header("Dataset")
    st.dataframe(df)

    st.header("Part A: Dataset Understanding")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
    st.write("Data Types")
    st.write(df.dtypes)

    target = st.selectbox("Select Target Variable (Optional)", ["None"] + list(df.columns))
    st.write("Target Variable:", target)

    st.header("Part B: Data Quality")
    st.write("Missing Values")
    st.write(df.isnull().sum())

    st.write("Duplicate Records:", df.duplicated().sum())

    st.header("Part C: Feature Analysis")
    st.write("Numerical Features")
    st.write(df.select_dtypes(include="number").columns.tolist())

    st.write("Categorical Features")
    st.write(df.select_dtypes(exclude="number").columns.tolist())

    st.write("Summary Statistics")
    st.write(df.describe())

    st.header("Part D: Insights")
    st.write("Correlation Matrix")
    st.write(df.corr(numeric_only=True))

    st.write("""
    **Suggested Insights**
    - Identify important numerical features.
    - Observe missing values and duplicates.
    - Check relationships using correlation.
    - Decide whether the dataset is suitable for Machine Learning.
    """)