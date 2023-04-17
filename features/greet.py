import datetime
import sys
import os
sys.path.append('tts/')
from tts import speak
from playsound import playsound

def greeting():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        greet="Good Morning"
        speak.speak(greet)
        playsound('test.wav')
        os.remove('test.wav')
    elif hour>12 and hour<16:
        greet="Good Afternoon"
        speak.speak(greet)
        playsound('test.wav')
        os.remove('test.wav')
    elif hour>15 and hour<22:
        greet="Good Evening"
        speak.speak(greet)
        playsound('test.wav')
        os.remove('test.wav')
    else:
        greet="Good Night"
        speak.speak(greet)
        playsound('test.wav')
        os.remove('test.wav')
    
