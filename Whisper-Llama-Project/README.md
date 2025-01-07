# Whisper-Llama Project

This project leverages OpenAI's Whisper model to convert audio to text and utilizes LLaMA 3 for question-answering based on the transcribed text. The application is built with **Streamlit** for a user-friendly interface and **Groq API** for faster computations, making it suitable for real-time applications.

## Features

- **Audio-to-Text**: Upload an audio file (MP3 or WAV) and convert it to text using OpenAI's Whisper model.
- **Question-Answering**: Ask questions based on the transcribed text, and receive relevant answers using LLaMA 3.
- **Real-Time Interaction**: The app provides real-time transcription and Q&A using a simple and intuitive interface.

## Tech Stack

- **Python**: Programming language for backend processing.
- **Streamlit**: Web framework for building the app interface.
- **OpenAI Whisper**: Used for converting audio to text.
- **LLaMA 3**: For analyzing text and generating answers to questions.
- **Groq API**: Optimized for lightweight and fast computation.
- **Ngrok**: For tunneling to expose your local server to the web.

## Setup and Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your system. This project also uses a virtual environment for managing dependencies.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Whisper-Llama-Project.git
cd Whisper-Llama-Project
