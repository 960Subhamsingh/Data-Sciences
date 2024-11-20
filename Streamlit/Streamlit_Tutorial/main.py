import streamlit as st
import pandas as pd

# Title
st.title("Simple Streamlit App")

# Input
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100)

# Button action
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")

# Data display
data = {'Column A': [1, 2, 3], 'Column B': [4, 5, 6]}
df = pd.DataFrame(data)
st.dataframe(df)

# Chart
st.line_chart(df)
