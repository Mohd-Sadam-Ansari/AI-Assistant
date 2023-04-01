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
    return True  

def sites(data):
    webbrowser.open(f'www.{data}.com')
    return True

def online_order(query):
    query=query.replace("find me",'')
    query=query.replace("i want to order a",'')
    query=query.replace("i want to order",'')
    query=query.replace("order a",'')
    query=query.replace("order me a",'')
    query=query.replace('alan','')
    query=query.replace('ellen','')

    if 'pizza' in query:
        web="https://pizzaonline.dominos.co.in/menu?"
        webbrowser.open(web)
    elif 'food' in query:
        web='https://www.zomato.com/mumbai/order-food-online'
        webbrowser.open(web)
    else:
        web='https://www.flipkart.com/search?q='+query
        webbrowser.open(web)

def google_search(query):
    query=query.replace('alan','')
    query=query.replace('ellen','')
    query=query.replace('google search','')
    query=query.replace('google','')
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
