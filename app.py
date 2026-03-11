import streamlit as st
from video_generator import create_video

st.title("🎬 Automated Explainer Video Generator")

text_input = st.text_area(
    "Enter your script (separate slides with blank line)",
    height=200
)

if st.button("Generate Video"):

    if text_input.strip() == "":
        st.error("Please enter text")
    else:

        with st.spinner("Generating video..."):

            video_path = create_video(text_input)

        st.success("Video Generated!")

        st.video(video_path)

        with open(video_path,"rb") as file:
            st.download_button(
                "Download Video",
                file,
                file_name="explainer_video.mp4"
            )