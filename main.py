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
import webbrowser

def mainexecution():
    whisper_stt.record_audio()
    query=whisper_stt.transcribe()
    Query=str(query).lower()
    keyword=alan.keyword_extract(Query)
    print(Query)
    if keyword=='news':

        result=api.news(Query)
    elif keyword=='create_file':
        result=system.create_files(Query)
    elif keyword=='camera':
        result=system.take_picture()
    elif keyword=='delete_file':
        result=system.delete_files(Query)
    elif keyword=='create_directory':
        result=system.create_directories(Query)
    elif keyword=='delete_directory':
        result=system.delete_directories(Query)
    elif keyword=='note':
        result=system.take_note(Query)
    elif keyword=='read_note':
        result=system.read_note()
        speak.speak(result)
        playsound('test.wav')
    elif keyword=='restart':    
        result=system.restart()
    elif keyword=='shutdown':
        result=system.shutdown()
    elif keyword == 'time':
        result=api.show_time()
    elif keyword=='joke':
        result=joke=api.jokes()
    elif keyword=='weather':
        result=api.weather(Query)
    elif keyword=='manual':
        result=system.manual(Query)
    elif keyword=='open':
        result=system.launch_app(Query)
    elif keyword=='wikipedia':
        result=api.search_wiki(Query)
    elif keyword=='google_search':
        result=browser.google_search(Query)
        speak.speak(result)
        playsound('test.wav')
    elif keyword=='how_to':
        result=browser.how_to(Query)
    elif keyword=='play_on_yt':
        result=browser.play_on_youtube(Query)
    elif keyword=='ip_address':
        result=system.ip_address()
    elif keyword=='job_schedule':
        result=system.job_schedule()
    elif keyword=='switch_tab':
        result=system.switch_window()
    elif keyword=='visit':
        result=sites(Query)
    elif keyword=='computation':
        result=api.computation(Query)
    elif keyword=='goodbye':
        sys.exit()
    else:
        result=keyword
        speak.speak(result)
        playsound('test.wav')
        os.remove("test.wav")
    return result        


print(mainexecution())