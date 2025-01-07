import os
from groq import Groq

def transcribe_audio(file_path):
    client = Groq()
    try:
        with open(file_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(file_path, file.read()),
                model="whisper-large-v3",
                response_format="verbose_json"
            )
            return transcription.text if hasattr(transcription, 'text') else "Error: Transcription text not found."
    except Exception as e:
        return f"Error during transcription: {e}"
