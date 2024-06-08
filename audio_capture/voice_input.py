# recognize_voices.py
import speech_recognition as sr
import pyttsx3 
import os
import time

r = sr.Recognizer() 

def erase_file():
    with open("./txt/output.txt", "w") as f:
        pass

def erase_file2():
    with open("./txt/response.txt", "w") as f:
        pass

def get_input():
    try:
        with sr.Microphone() as source2: # microphone input
            r.adjust_for_ambient_noise(source2, duration=0.2) # prepare for ambient noise

            # audio input
            audio2 = r.listen(source2)

            # try to convert to string
            gottenText = r.recognize_google(audio2)
            gottenText = gottenText.lower()

            return gottenText

    # cases where audio can't be understood
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")

    return None

def give_string(text):
    # add text to a file
    with open("./txt/output.txt", "a") as f:
        f.write(text + "\n")

# starting the recording
erase_file()
erase_file2()

stop_file = "stop.txt"

while not os.path.exists(stop_file):
    text = get_input()
    if text:
        give_string(text)
        print("Wrote Text")
    time.sleep(1)  # sleep for a bit to avoid busy waiting

# Cleanup: Remove the stop file after stopping
os.remove(stop_file)
print("Recording stopped.")
