from hear import *
from speak import *
from db_handle import *
from datetime import datetime, date, time
import webbrowser

speak ("Hello I am Han!!")

while True:
    sound  = hear()
    
    if sound == None:
        speak("Say again please")
    # elif "hôm nay" in sound or "bây giờ" in sound:
    #     now = datetime.now()
    #     if "mấy giờ" in sound:
    #         tm = now.strftime("%H giờ %M phút %S giây")
    #         speak(tm)
    #     if "ngày" in sound:
    #         tm = now.strftime("Hôm nay là ngày %d tháng %m năm %y")
    #         speak(tm)
    elif "open" in sound:
        if "facebook" in sound:
            webbrowser.open("https://www.facebook.com/")
        if "youtube" in sound:
            webbrowser.open("https://www.youtube.com/")
    # elif "you" in sound and "khỏe" in sound:
    #     speak("I am good")
    # elif "bạn" in sound and "tuổi" in sound in sound:
    #     speak("I am 22 years old")
    elif "goodbye" in sound:
        speak("See you later!!")
        break
    else:
        index = handle_data(sound)
        speak(ans[index])