import webbrowser
import pywhatkit
import pyautogui
from pywikihow import search_wikihow
import wikipedia

def play_on_youtube(query):
    query=query.replace('alan','')
    query=query.replace('ellen','')
    query=query.replace('play song on youtube','')
    query=query.replace('youtube','')
    query=query.replace('video','')
    query=query.replace('movie','')
    query=query.replace('search','')

    pywhatkit.playonyt(query)
    pyautogui.press('enter')
      

def sites(data):
    data=data.replace('alan','')
    data=data.replace('ellen','')
    data=data.replace('please','')
    data=data.replace('visit','')
    data=data.replace('can you','')
    data=data.replace('website','')
    data=data.replace('.com','')
    data=data.replace('.','')
    data=data.strip()

    if len(data)==0:
        speak.speak('website name is not found, please try again.')
        playsound('tets.wav')
    link=f'https://www.{data}.com'    
    webbrowser.open(link)

def google_search(query):
    query=query.replace('alan','')
    query=query.replace('ellen','')
    query=query.replace('google search','')
    query=query.replace('google','')
    query=query.strip()
    try:
        pywhatkit.search(query)
        result=wikipedia.summary(query,2)
        return result
    except:
        return "No speakable content available."

def how_to(query):
    max_results=1
    how_to_func=search_wikihow(query=query,max_results=max_results)
    assert len(how_to_func) == 1
    how_to_func[0]
    result=how_to_func[0].summary
    return result
