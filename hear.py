import speech_recognition as sr

def hear():
    print("Listening...")
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Me: ", end='')
        audio = r.listen(source, phrase_time_limit=3)
        try:
            text = r.recognize_google(audio, language="en-US")
            print(text)
            return str(text).lower()
        except:
            return None
        
print(hear())