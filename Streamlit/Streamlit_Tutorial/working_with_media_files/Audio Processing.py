# Audio Processing (Using pydub)

import streamlit as st

from pydub import AudioSegment

uploaded_audio = st.file_uploader("Choose an audio file...", type=["mp3", "wav"])
# After uploading audio file
if uploaded_audio is not None:
    audio = AudioSegment.from_file(uploaded_audio)
    
    # Trim the first 30 seconds
    trimmed_audio = audio[:30000]
    trimmed_audio.export("trimmed_audio.wav", format="wav")
    
    # Play the trimmed audio
    st.audio("trimmed_audio.wav")



# Provide a Download Button for the Processed Audio


import io

# After processing the audio
if uploaded_audio is not None:
    audio = AudioSegment.from_file(uploaded_audio)
    
    # Process audio (trim, change format, etc.)
    processed_audio = audio[:30000]  # Example: trimming the first 30 seconds
    processed_audio.export("processed_audio.mp3", format="mp3")
    
    # Save audio to BytesIO for download
    audio_byte_arr = io.BytesIO()
    processed_audio.export(audio_byte_arr, format="mp3")
    audio_byte_arr.seek(0)
    
    st.download_button(
        label="Download Processed Audio",
        data=audio_byte_arr,
        file_name="processed_audio.mp3",
        mime="audio/mpeg"
    )




