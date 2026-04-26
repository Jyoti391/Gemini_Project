import streamlit as st
from api_calling import node_generator ,audio_transcription ,quiz_generator
from PIL import Image

st.title("Note summary and quiz generator")
st.markdown("Upload up to 3 images for generating quiz")
st.divider()

pressed = False
select_option = None
images = None

with st.sidebar:
    st.header("Contents")

    images = st.file_uploader(
        "Upload the photos of quiz generation",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )

    if images:
        st.subheader("Your uploaded images")

        if len(images) > 3:
            st.error("Upload at max 3")
        else:
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    select_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ("Easy", "Medium", "Hard"),
        placeholder="Select an option"
    )

    pressed = st.button("Click for generation quiz", type="primary")

    if select_option:
        st.markdown(f"You selected **{select_option}** difficulty")

if pressed:
    if not images:
        st.error("You must upload images")
    elif not select_option:
        st.error("You must select a difficulty")
    elif len(images) > 3:
        st.error("Upload at max 3")
    else:
        with st.container(border=True):
            st.subheader("Notes")
            pil_images = [Image.open(img) for img in images]
            generate_images = node_generator(pil_images)
            st.text(generate_images)
        
        with st.container(border=True):
            st.subheader("Audio Transcript")
            generate_images=generate_images.replace("#","")
            generate_images=generate_images.replace("*","")
            generate_images=generate_images.replace("'","")
            generate_images=generate_images.replace("-","")
            audio_transcrip=audio_transcription(generate_images)
            with st.spinner("AI is generating audio"):
                audio_transcrip=audio_transcription(generate_images)
            st.audio(audio_transcrip)

        with st.container(border=True):
            st.subheader(f"Quiz {(select_option)} difficulty generator")
           
            with st.spinner("Ai is generating quizes"):
                  quizzes = quiz_generator(pil_images, select_option)
                  st.markdown(quizzes)
          

            
