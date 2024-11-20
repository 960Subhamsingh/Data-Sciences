
# CREATE DATABASE crud_app;
# USE crud_app;

# CREATE TABLE users (tiger

#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100)
# );


import streamlit as st
import mysql.connector
import pandas as pd


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='crud_app'
    )
    return connection



def create_user(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()

def read_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

def update_user(user_id, name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

 
st.title("CRUD Application")

# Create User
st.header("Create User")
with st.form("create_user_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Create User")
    if submitted:
        create_user(name, email)
        st.success("User created successfully!")

# Read Users
st.header("Users List")
users = read_users()
df = pd.DataFrame(users)
st.dataframe(df)

# Update User
st.header("Update User")
user_id = st.number_input("User ID", min_value=1, step=1)
with st.form("update_user_form"):
    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    update_submitted = st.form_submit_button("Update User")
    if update_submitted:
        update_user(user_id, new_name, new_email)
        st.success("User updated successfully!")

# Delete User
st.header("Delete User")
delete_user_id = st.number_input("Delete User ID", min_value=1, step=1)
if st.button("Delete User"):
    delete_user(delete_user_id)
    st.success("User deleted successfully!")

 
# Run the Streamlit application by executing the following command in your terminal:

#  streamlit run app.py

 
