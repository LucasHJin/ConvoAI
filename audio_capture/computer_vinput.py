import sounddevice as sd
import numpy as np
import speech_recognition as sr
import soundfile as sf

sample_rate = 44100
duration = 3

recognizer = sr.Recognizer()

def record_and_transcribe(output_file, sample_rate):
    while True:            
        recording = sd.rec(duration * sample_rate, samplerate=sample_rate, channels=2, device='BlackHole')
        sd.wait() 

        sf.write('temp_file.wav', recording, sample_rate)

        try:
            with sr.AudioFile('temp_file.wav') as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                with open(output_file, 'a') as f:
                    f.write(text + ' ')
                    print("Transcribed text:", text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

output_file = "./txt/output.txt"
record_and_transcribe(output_file, sample_rate)