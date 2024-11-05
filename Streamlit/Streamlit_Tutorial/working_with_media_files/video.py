import streamlit as st

# Upload a video file
uploaded_video = st.file_uploader("Choose a video file...", type=["mp4", "avi", "mov"])

if uploaded_video is not None:
    st.video(uploaded_video)


st.title("Upload an audio file")
uploaded_audio = st.file_uploader("Choose an audio file...", type=["mp3", "wav"])

if uploaded_audio is not None:
    st.audio(uploaded_audio)

st.title("Displaying Media Files")
st.write("Streamlit provides easy-to-use methods to display images, play audio, or show videos in the app.")

st.video(uploaded_video, caption="Your Image", use_column_width=True)

# To display audio, Streamlit provides the st.audio() function, which supports MP3, WAV, or other audio formats.
st.audio(uploaded_audio)



