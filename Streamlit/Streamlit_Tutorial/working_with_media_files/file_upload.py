import streamlit as st

uploaded_files = st.file_uploader("Choose multiple images...", type=["jpg", "png"], accept_multiple_files=True)

if uploaded_files is not None:
    for upload_file in uploaded_files:
          st.image(uploaded_files, caption=f"Uploaded {upload_file.name}",use_column_width=True)


uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    # Access file details
    file_name = uploaded_file.name
    file_size = uploaded_file.size
    file_type = uploaded_file.type

    st.write(f"File Name: {file_name}")
    st.write(f"File Size: {file_size} bytes")
    st.write(f"File Type: {file_type}")     

# Image Upload and Processing 

from PIL import Image
import io
if uploaded_file is not None:
    # Open the image using PIL
    img = Image.open(uploaded_file)
    
    # Display the original image
    st.image(img, caption="Uploaded Image.", use_column_width=True)
    
    # Resize the image (for example, to 400x400)
    img_resized = img.resize((400, 400))
    st.image(img_resized, caption="Resized Image.", use_column_width=True)
    
    # Save resized image to a BytesIO object for downloading
    img_byte_arr = io.BytesIO()
    img_resized.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    # Allow user to download the resized image
    st.download_button(
        label="Download Resized Image",
        data=img_byte_arr,
        file_name="resized_image.png",
        mime="image/png"
    )


# Check File Size: You can inspect the file size and display an error message if it exceeds a certain limit.

uploaded_file = st.file_uploader("Choose a file...", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    file_size = uploaded_file.size
    if file_size > 10 * 1024 * 1024:  # 10MB
        st.warning("File is too large! Please upload a file under 10MB.")
    else:
        # Process the file
        st.image(uploaded_file)