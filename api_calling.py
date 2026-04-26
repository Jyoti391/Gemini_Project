import streamlit as st
import google.genai as genai
from dotenv import load_dotenv
from gtts import gTTS
import io
import os

load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)

def node_generator(images):
    prompt = """summarize the picture in note format at max 100 words,
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text

def audio_transcription(text):
    speech = gTTS(text=text, lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    #st.audio(audio_buffer)
    return audio_buffer
def quiz_generator(image, difficulty):
    prompt = f"Make at least 3 quiz questions based on {difficulty} difficulty. Use markdown to format options clearly.Add correct answer and explanation"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image, prompt]
    )
    return response.text