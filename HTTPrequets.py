import requests as r
from hear import hear
from speak import speak

speak("Hello i am Han")
while True:
    rq = hear()
    if rq == None:
        speak("Can you say again!!")
    elif "on" in rq:
        if "green" in rq:
            data = r.get("http://192.168.3.49/ongreen")
            print(data.text)
            speak("GREEN LED IS TURN ON") 
        elif "white" in rq:
            data = r.get("http://192.168.3.49/onwhite")
            print(data.text)
            speak("WHITE LED IS TURN ON")
        
    elif "off" in rq:
        if "green" in rq:
            data = r.get("http://192.168.3.49/offgreen")
            print(data.text)
            speak("GREEN LED IS TURN OFF") 
        elif "white" in rq:
            data = r.get("http://192.168.3.49/offwhite")
            print(data.text)
            speak("WHITE LED IS TURN OFF")  
    
    elif "goodbye" in rq:
        speak("Goodbye, see you later")
        break