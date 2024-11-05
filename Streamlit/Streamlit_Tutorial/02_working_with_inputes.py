import streamlit as st

#  Title
st.title("Text Input Examples")

# Text_Input
name = st.text_input("Enter the name:"," ")
# Display
st.write("Name:", name.upper())

# Text Area
feedback = st.text_area("Enter you feedback:", "")
st.write("feedback:",feedback)

# Number Input 
age = st.number_input("Enter you age: ", min_value=0,max_value=100, step=1)
st.write("Age :",age)

#  Data Input
date = st.date_input("Select a date:")
st.write("Date : " , date) 

# Time Input
time = st.time_input("Select a time:")
st.write("Time :" , time)

# Color Picker
color = st.color_picker("Pick a color")
st.write("color:", color)

# Display inputs

# print color based on color values

# HTML
html_code = """
        <h1 style='color: {};'>This is a blue heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
""".format(color)
st.markdown(html_code, unsafe_allow_html=True)