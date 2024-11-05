import streamlit as st

# Title
st.title("Streamlit Media and File Examples")


# Image
st.subheader("Image")
image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
if image is not None:
    st.image(image, caption="Uploaded Image", width=100)



# use link to display image
st.image("https://kgptalkie.com/wp-content/uploads/2019/03/cropped-iPad-Pro-Copy@2x-1.png", caption="KGP Talkie Logo", width=100)


st.title("Image Processing (Resizing or Cropping)")

from PIL import Image
# Upload an image file
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
# After uploading the image
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    
    # Resize image
    img_resized = img.resize((400, 400))
    st.image(img_resized, caption="Resized Image", use_column_width=True)


# Provide a Download Button for the Processed Image


import io

# Save processed image to a BytesIO object
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_resized = img.resize((400, 400))
    
    # Save image to memory (BytesIO)
    img_byte_arr = io.BytesIO()
    img_resized.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Allow user to download the processed image
    st.download_button(
        label="Download Processed Image",
        data=img_byte_arr,
        file_name="processed_image.png",
        mime="image/png"
    )

