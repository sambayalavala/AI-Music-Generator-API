# AI Music Generator API

## Description
This is a simple FastAPI project that generates music from a text prompt.

## Features
- Text-based music generation
- Rule-based melody
- WAV file output

## Installation
pip install -r requirements.txt

## Run the Server
uvicorn main:app --reload

## API Endpoint

POST /generate-music

Request:
{
  "prompt": "happy birthday tune"
}

Response:
{
  "result": "output.wav"
}

## Output
Generated audio file (output.wav)