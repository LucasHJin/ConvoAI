import sounddevice as sd
import numpy as np
import speech_recognition as sr
import soundfile as sf

sample_rate = 44100
duration = 5  

recognizer = sr.Recognizer()

def record_audio(output_file, sample_rate, duration):
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, device='BlackHole')
    sd.wait() 

    sf.write('temp_file.wav', recording, sample_rate)
    try:
        with sr.AudioFile('temp_file.wav') as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Speech recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

output_file = "output.txt"
transcribed_text = record_audio(output_file, sample_rate, duration)
print("Transcribed text:")
print(transcribed_text)