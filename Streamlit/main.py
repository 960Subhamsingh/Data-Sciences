import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from io import BytesIO
from PIL import Image
# from rembg import remove
# from cartooner import cartoonize
# import cv2


st.title("Simple Data Dashboard")
# write key and values 
# st.write({"key":["values"]})

# st.set_page_config(layout="wide", page_title="Image Background Remover")

st.sidebar.write("## Upload and download :gear:")
st.write(
    ":dog: Try uploading an image to watch the background magically removed."
)

# Create the file uploader
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])




uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if(uploaded_file is not None):
    st.write("file uploaded")
    data = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(data.head())

    st.subheader("Data Summary")
    st.write(data.describe())

    st.subheader("Filter Data")
    columns = data.columns.tolist()
    select_col = st.selectbox("Select column to filter by", columns)
    unique_values = data[select_col].unique()
    selected_value = st.selectbox("Select value", unique_values)
    filter_values = data[data[select_col]== selected_value]
    st.write(filter_values)

    st.subheader("Plot Data")
    x_column = st.selectbox("select x-axis column" , columns)
    y_column = st.selectbox("select y-axis column", columns)

    if st.button("Plot"):
        st.bar_chart(filter_values.set_index(x_column)[y_column])
        st.success('Positive Review')
    else:
        st.write("Waiting on file upload")
 
 

# st.help()