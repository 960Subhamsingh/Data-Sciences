import streamlit as st

# Title
st.title("Streamlit Interactive Widget Examples")

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increase counter'):
    st.session_state.counter += 1

st.write(f'Counter value: {st.session_state.counter}')

st.header("Button")
st.text("Displays a button that users can click to trigger an action.")
if st.button("Click Me"):
    st.write("clicked!")

st.header("checkbox")
st.text("Displays a checkbox that users can check or uncheck.")
checkbox_state = st.checkbox("Click me to enable something")

if(checkbox_state):
    st.write("checked")

st.header("Radio button")
st.text("Displays a set of radio buttons for users to select one option.")
radio_selection = st.radio("Choose an option:", ["Male", "Female", "Transparent"])
st.write(radio_selection)


st.header("selectbox")
st.text("Displays a dropdown selection box for users to choose from a list of options.")
select_box=st.selectbox("Choose an option:", ["Male", "Female", "Transparent"])
st.write("select_box : ",select_box)

st.header("Multiselect")

mutilselct_box= st.multiselect("Choose an option:", ["Male", "Female", "Transparent"])
st.write("select box :" , mutilselct_box)

fruits = st.multiselect('Pick some fruits', ['Apple', 'Banana', 'Orange', 'Grapes'])
st.write(f'You selected: {fruits}')

st.header("Slider")
st.text("Displays a slider for users to select a value from a given range.")
age = st.slider('Select your age', 0, 100, 25 )
st.write(f'Your age is {age}')

slider_value = st.slider("Select a value:", min_value=0, max_value=10, value=5, step=1)
st.write("Slider value:", slider_value)

# Slider widget to control a value
x = st.slider('Select a number', 0, 100, 50)

# Display result dynamically
st.write(f'Selected number is {x}')
st.write(f'Square of the number is {x**2}')

st.header("Select slider")
# select_slider_value = st.select_slider("Select a value:", options=range(10))
select_slider_value = st.select_slider("Select a value:", options=[1, 4, 5, 6, 3, 2, 'NLP'])

st.write("Selected slider value:", select_slider_value)

st.header("File Upload")
st.text("Allows users to upload files.")
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    st.write(f'File uploaded: {uploaded_file.name}')