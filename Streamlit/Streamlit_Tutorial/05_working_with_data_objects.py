import streamlit as st
import pandas as pd

st.title("1. Displaying DataFrames with Pandas")
st.write("Pandas DataFrames are one of the most common data structures used in data science, and Streamlit provides a straightforward way to display them.")

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here is the sample data:")
st.dataframe(df)
st.title('Use to table function (st.table())')
st.table(df)
st.write("st.dataframe(df) renders the DataFrame in an interactive table format where you can scroll and sort.")
st.write("You can also use st.table(df) to show a static table if you don’t need the interactivity.")

st.header("2. Displaying Large DataFrames")

# Create a large sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin']
}

df = pd.DataFrame(data)

# Display only the first 5 rows
st.write("Here is the top 5 rows of the data:")
st.dataframe(df.head())

st.title("4. Interactive Data Exploration with Pandas")
st.write("Streamlit makes it easy to allow users to interact with data, such as filtering rows, sorting columns, or even selecting specific rows.")

# Allow the user to select a city to filter by
selected_city = st.selectbox('Select a city to filter by:', df['City'].unique())

# Filter the DataFrame based on the selected city
filtered_df = df[df['City'] == selected_city]

# Display the filtered DataFrame
st.write(f"People in {selected_city}:")
st.dataframe(filtered_df)


st.title("5. Manipulating and Modifying Data")

st.write("You can also modify and work with data dynamically using user inputs. For example, allowing users to add or remove data from a dataset.")

# Initial DataFrame
data = {
    'Name': ['subham kumar', 'Monu kumar','Sonu kumar','Ritu kumari'],
    'Age': [25, 30,45,56],
    'City': ['New York', 'INDIA','China','Russia']
}
df = pd.DataFrame(data)

# Allow user to add a new row
name = st.text_input("Name")
age = st.number_input("Age", min_value=0)
city = st.text_input("City")

if st.button("Add Entry"):
    new_row = pd.DataFrame({'Name':[name], 'Age': [age], 'City': [city]})
    df = pd.concat([df, new_row], ignore_index=True)
    st.write("Update Data")
    st.dataframe(df)


st.title("6. Working with JSON Data")
st.write("Streamlit allows you to easily work with JSON data by reading from files or directly from user input.")

import json

# Sample JSON data
json_data = '{"Name": "Alice", "Age": 25, "City": "New York"}'

# Parse the JSON string into a Python dictionary
data = json.loads(json_data)

# Display JSON data
st.json(data)


st.title("7. Working with Files (CSV, Excel, etc.)")

# Allow user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if(uploaded_file is not None):
    # Read the csv file into a DataFrame
    df = pd.read_csv(uploaded_file)
    # Display the Dataframe
    st.write("uploaded Data: ")
    st.dataframe(df)

st.title("8. Using st.session_state to Store Data Across Reruns")
st.write("Streamlit’s st.session_state allows you to store and persist data across reruns of the app, which is useful for interactive applications where the user might modify data or selections.")

# Check if session_state contains a list, otherwise initialize it
if 'data' not in st.session_state:
    st.session_state.data = []

# Allow the user to add data
new_data = st.text_input("Enter some data:")

if(st.button("Add Data")):
    if(new_data):
        st.session_state.data.append(new_data)
        st.write("Current Data in Session: ")
        st.write(st.session_state.data)

st.title("using the 'st.code' method")

st.write("The st.code method in Streamlit is used to display code in a formatted and highlighted way in the app. This is especially useful when you want to show snippets of code in your app for educational purposes, documentation, or to display code as part of a tutorial.")

code = '''import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)'''

st.code(code, language='python')


st.write("the code snippet is a shell command, and it will be displayed with syntax highlighting appropriate for bash scripts.")

sql_code = '''SELECT name, age FROM users WHERE age > 30 ORDER BY age DESC;'''

st.code(sql_code, language='Sql')


generic_code = '''// Simple JavaScript Example
const greet = () => {
    console.log("Hello, Streamlit!");
}
greet();'''

st.code(generic_code)

st.title("Metric")
st.write("The st.metric() function in Streamlit is used to display a metric with a label, a value, and an optional change indicator (e.g., showing the percentage change or absolute change between two values). It is ideal for displaying key metrics, such as performance indicators, KPIs (Key Performance Indicators), or other important values in an easy-to-read format.")

# Display a simple metric
st.metric(label="Revenue", value="$25,000")


st.title("DataEditor")
st.write("The st.dataeditor() function in Streamlit allows you to display a data editing interface for a Pandas DataFrame or similar table-like data. It lets users interactively edit values within the table, making it useful for applications where data needs to be modified by the user.")

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Show Data Editor
edited_df = st.data_editor(df)

# Display the edited DataFrame
st.write("Edited Data:")
st.dataframe(edited_df)






# st.image(uploaded_image, caption="Your Image", use_column_width=True)


