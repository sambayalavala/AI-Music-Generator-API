from fastapi import FastAPI
from pydantic import BaseModel
from music_generator import generate_music

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

class MusicRequest(BaseModel):
    prompt: str

@app.post("/generate-music")
def generate_music_api(request: MusicRequest):
    file_path = generate_music(request.prompt)

    return {
        "result": file_path
    }
