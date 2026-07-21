import os
import streamlit as st

from video_to_Text import transcribe_video


# Folder Setup

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# Streamlit Page
st.set_page_config(
    page_title="AI Video To Text",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 AI Video to Text Converter")

st.write(
    "Upload a video and convert speech into text using OpenAI Whisper."
)

# ----------------------------
# Upload Video
# ----------------------------

uploaded_file = st.file_uploader(
    "Choose a Video",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_file is not None:

    video_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Video Uploaded")

    st.video(video_path)

    # ----------------------------
    # Convert Button
    # ----------------------------

    if st.button("🎙 Convert Video to Text"):

        with st.spinner("Processing Video..."):

            transcript = transcribe_video(video_path)

        st.success("✅ Completed")

        st.subheader("Transcript")

        st.text_area(
            "",
            transcript,
            height=200
        )

        st.download_button(
            "⬇ Download Transcript",
            transcript,
            file_name="transcript.txt"
        )