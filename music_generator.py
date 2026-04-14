import numpy as np
from scipy.io.wavfile import write


NOTES = {
    "C": 261,
    "D": 294,
    "E": 329,
    "F": 349,
    "G": 392,
    "A": 440,
    "B": 493
}

def generate_music(prompt: str, filename="output.wav"):
    sample_rate = 44100
    duration = 0.4

    
    if "happy" in prompt.lower():
        melody = ["C", "E", "G", "E", "C"]
    elif "birthday" in prompt.lower():
        melody = ["C", "C", "D", "C", "F", "E"]
    elif "sad" in prompt.lower():
        melody = ["E", "D", "C", "D", "E"]
    else:
        melody = ["A", "B", "C", "B", "A"]

    audio = []

    for note in melody:
        freq = NOTES[note]
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = np.sin(freq * t * 2 * np.pi)
        audio.extend(wave)

    audio = np.array(audio)
    audio = audio * (2**15 - 1) / np.max(np.abs(audio))
    audio = audio.astype(np.int16)

    write(filename, sample_rate, audio)

    return filename
