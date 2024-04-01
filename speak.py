from gtts import gTTS
import playsound
import os

def speak(text):
    print("You: " + text)
    tts = gTTS(text= text, lang= "en", slow = False)
    tts.save("./py_project/sound.mp3")
    playsound.playsound("D:\C++\py_project\sound.mp3", True)
    #os.remove("D:\C++\py_project\sound.mp3")
    
speak("Hello, good morning")