import wolframalpha
import requests
import wikipedia
import pyjokes
import time
import json
import sys
import os

sys.path.append('stt/')
sys.path.append('tts/')
from tts import speak
from stt import whisper_stt
from playsound import playsound

#To get a programming jokes
def jokes():
    joke=pyjokes.get_joke(language='en',category='neutral')
    speak.speak(joke)
    playsound('test.wav')
    os.remove('test.wav')
    return joke

#To perform mathematical calculation
def computation(query):
    query=query.replace('alan','')
    query=query.replace('ellen','')
    query=query.replace('calculate','')
    query=query.replace('solve','')
    query=query.replace('compute','')
    query=query.replace('perform mathematical computation','')
    query=query.replace('equation','')
    query=query.replace('math calculation','')
    query=query.replace('do calculation','')
    query=query.replace('into','multiply by')
    if len(query)==0:
        return'Equation not provided,please try again..'
    else:
        client=wolframalpha.Client('VTY239-55Y8AXJEW4')
        res=client.query(query)
        result=next(res.results).text
        return result  
    
#To fetch weather forecast of particular city
def weather(location):
    location=location.replace('weather report','')
    location=location.replace('whats the weather','')
    location=location.replace("what's the weather",'')
    location=location.replace("weather forecast",'')
    location=location.replace('give me the weather report of','')
    location=location.replace("today's weather",'')
    location=location.replace('alan','')
    location=location.replace('ellen','')
    location=location.replace('give me','')
    location=location.replace('weather','')
    location=location.replace('give','')
    location=location.replace('of','')
    location=location.replace('?','')
    location=location.replace('!','')
    location=location.replace(".",'')

    if len(location)==0:
        location='mumbai'
    
    Base_Url="http://api.openweathermap.org/data/2.5/weather?"
    API_KEY="e0fdd235cc32f3a8e4530658254850a6"
    url=Base_Url+"appid="+API_KEY+"&q="+location
    response=requests.get(url).json()
    
    if(response['cod']=='404'):
        city=f"{location} not found."
        return city
    else:    
        temp_kelvin=response['main']['temp']
        temp_celsius=temp_kelvin-273.15
        wind_speed=response['wind']['speed']
        humidity=response['main']['humidity']
        description=response['weather'][0]['description']
        temp=f"Temperature in {location} : {temp_celsius:.2f}℃ degree celcius"
        wind=f"Wind Speed : {wind_speed} meters per second"
        humid=f"Humidity : {humidity}%"
        weather=f"General Weather in {location} : {description}"
        return temp,wind,humid,weather

#To retrive information from the wikipedia
def search_wiki(query):
    query=query.replace("wikipedia",'')
    query=query.replace("according to wikipedia",'')
    query=query.replace("from wikipedia",'')
    query=query.replace("search from wikipedia",'')
    if len(query)==0:
        return'Nothing found to search,please try again.'
    else:
        result=wikipedia.summary(query)
        return result

#To fetch latest news of India
def news(field):
    api_dict={"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=759eabe66a3949e79df242f6a6f37f9a",
    "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=759eabe66a3949e79df242f6a6f37f9a"}

    content=None
    url=None
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url=value
            break
        else:
            url="https://newsapi.org/v2/top-headlines?country=in&apiKey=759eabe66a3949e79df242f6a6f37f9a"
    news=requests.get(url).text
    news=json.loads(news)
    speak.speak("here is the news")
    playsound('test.wav')
    os.remove('test.wav')
    arts=news["articles"]
    article=[]
    for articles in arts:
        article.append([articles["title"],articles['url']])
    for i in range(5):
        speak.speak(article[i])
        playsound('test.wav')
        os.remove('test.wav')
        head=' '.join([str(element) for element in article])
        return head

def show_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    speak.speak('time is'+current_time)
    playsound('test.wav')
    os.remove('test.wav')
    return current_time

if __name__=="__main__":
    pass