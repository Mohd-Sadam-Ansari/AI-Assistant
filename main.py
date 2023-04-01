import sys
import os
sys.path.append("..")
sys.path.append("tts/")
sys.path.append("intent_classification/")
sys.path.append("features/")
sys.path.append("stt/")


from stt import whisper_stt
from tts import speak
from intent_classification import model,alan,nltk_utils
from features import system,api,greet,browser
from playsound import playsound
def main():
    while True:
        whisper_stt.record_audio()
        query=whisper_stt.transcribe()
        Query=str(query).lower()
        keyword=alan.keyword_extract(Query)
        if keyword=='news':
            returned=api.news(Query)
        elif keyword=='create_file':
            system.create_files(Query)
        elif keyword=='camera':
            system.take_picture()
        elif keyword=='delete_file':
            system.delete_files(Query)
        elif keyword=='create_directory':
            system.create_directories(Query)
        elif keyword=='delete_directory':
            system.delete_directories(Query)
        elif keyword=='note':
            system.take_note(Query)
        elif keyword=='read_note':
            system.read_note()
        elif keyword=='restart':    
            system.restart()
        elif keyword=='shutdown':
            system.shutdown()
        elif keyword == 'time':
            api.show_time()
        elif keyword=='joke':
            joke=api.jokes()
        elif keyword=='goodbye':
            sys.exit()
        else:
            speak.speak(keyword)
            playsound('test.wav')
            os.remove("test.wav")

print(main())


