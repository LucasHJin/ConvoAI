import pyaudio
import wave
import speech_recognition as sr
import parse_questions_chat

# Parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

def erase_file():
    with open("./txt/q_output.txt", "w") as f:
        pass

def erase_file2():
    with open("./txt/response.txt", "w") as f:
        pass

erase_file()
erase_file2()

# Function to record audio
def record_audio():
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Recording finished.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

# Function to transcribe audio
def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
        audio_data = recognizer.record(source)
        print("Transcribing audio...")
        try:
            text = recognizer.recognize_google(audio_data)
            print("Transcription: " + text)
            with open("./txt/output.txt", "w") as f:
                f.write(text)
                parse_questions_chat.write(parse_questions_chat.ask(text))

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    record_audio()
    transcribe_audio()

# def start_recording():
#     record_audio()
#     transcribe_audio()
    
#         # erase_file()
#         # thread = threading.Thread(target=record_and_transcribe)
#         # thread.start()

# def stop_recording():
#     print("recording stopped")

# Example usage
# start_recording()
# time.sleep(60)  # Record for 60 seconds
# stop_recording()
