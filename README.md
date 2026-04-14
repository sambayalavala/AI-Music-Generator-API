#  AI Music Generator API

##  Overview
This project is a simple FastAPI-based API that generates music from a text prompt.

---

##  Tech Stack
- FastAPI
- Python
- NumPy
- SciPy

---

##  API Endpoint

### POST /generate-music

#### Input:
{
  "prompt": "happy birthday tune"
}

#### Output:
{
  "result": "output.wav"
}

---

##  How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run server:
uvicorn main:app --reload

3. Open browser:
http://127.0.0.1:8000/docs

---

##  Output
- Generates a .wav music file
- Example: output.wav

---

##  Approach
This project uses a rule-based melody generator that creates simple tones using Python.

---

##  Project Structure

music_generator_api/
│
├── main.py
├── music_generator.py
├── output.wav
├── requirements.txt
├── README.md
