import streamlit as st
import os
from dotenv import load_dotenv
import tempfile
from src.transcribe import transcribe_audio
from src.analysis import analyze_text

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NGROK_AUTH_TOKEN = os.getenv("NGROK_AUTH_TOKEN")

# Streamlit app
st.title("Audio to Text and Q&A with LLaMA 3")

# File uploader
audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])
if audio_file:
    # Create a temporary file for the uploaded audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{audio_file.name.split('.')[-1]}") as temp_file:
        temp_filename = temp_file.name  # Get the path of the temporary file
        with open(temp_filename, "wb") as f:
            f.write(audio_file.read())

    st.write("Processing audio...")
    transcription = transcribe_audio(temp_filename)
    st.write("Transcription:")
    st.write(transcription)

    # Clean up the temporary file
    os.remove(temp_filename)

    # Q&A
    question = st.text_input("Ask a question about the transcription:")
    if question:
        st.write("Analyzing...")
        answer = analyze_text(transcription, question)
        st.write("Answer:")
        st.write(answer)
