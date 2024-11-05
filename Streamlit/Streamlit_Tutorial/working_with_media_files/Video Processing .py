# Video Processing (USing moviepy
import streamlit as st

from moviepy.editor import VideoFileClip


uploaded_video = st.file_uploader("Choose a video file...", type=["mp4", "avi", "mov"])

# Load and display video after upload
if uploaded_video is not None:
    video = VideoFileClip(uploaded_video)
    video_preview = video.subclip(0, 5)  # Preview the first 5 seconds
    st.video(video_preview)