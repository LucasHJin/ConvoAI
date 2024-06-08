#recognize voices and take in
import speech_recognition as sr
import pyttsx3 


r = sr.Recognizer() 

def erase_file():
    with open("output.txt", "w") as f:
        pass

def get_input():
    while (1):
        try:
            with sr.Microphone() as source2: #microphone input
                r.adjust_for_ambient_noise(source2, duration=0.2) #prepare for ambient noise

                #audio input
                audio2 = r.listen(source2)

                #try to convert to string
                gottenText = r.recognize_google(audio2)
                gottenText = gottenText.lower()

                return gottenText

        #cases where audio can't be understood
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")

    return

def give_string(text):
    #add text to a file
    f = open("output.txt", "a")

    f.write(text)
    f.write("\n")
    f.close()

    return


#starting the recording

erase_file()

while (1):
    text = get_input()
    give_string(text)

    print("Wrote Text")