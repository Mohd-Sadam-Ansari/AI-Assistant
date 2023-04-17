import wolframalpha
import requests
import wikipedia
import pyjokes
import time
import json
import sys
import os

sys.path.append('tts/')
from tts import speak
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
    query=query.replace('.','')
    query=query.strip()

    try:
        if len(query)!=0:
            client=wolframalpha.Client('VTY239-55Y8AXJEW4')
            res=client.query(query)
            output=next(res.results).text
            speak.speak(output)
            playsound('test.wav')
            os.remove('test.wav')
            return output

    except:
        speak.speak('Equation not provided,please try again..')
        playsound('test.wav')
        os.remove('test.wav')
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
    location=location.strip()
    x=''

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
        temp=f"Temperature in {location} : {temp_celsius:.2f}℃ "
        wind=f"Wind Speed : {wind_speed} meters per second"
        humid=f"Humidity : {humidity}%"
        weather=f"General Weather in{location} : {description}"
        speak.speak(temp)
        playsound('test.wav')
        os.remove('test.wav')
        speak.speak(wind)
        playsound('test.wav')
        os.remove('test.wav')
        speak.speak(humid)
        playsound('test.wav')
        os.remove('test.wav')
        speak.speak(weather)
        playsound('test.wav')
        os.remove('test.wav')
        x=temp+" "+wind+" "+humid+" "+weather+" ."
        return x

#To retrive information from the wikipedia
def search_wiki(query):
    query=query.replace("wikipedia",'')
    query=query.replace("according to wikipedia",'')
    query=query.replace("from wikipedia",'')
    query=query.replace("search from wikipedia",'')
    query=query.replace("who is",'')
    try:
        if len(query)!=0:
            output=wikipedia.summary(query,2)
            speak.speak(output)
            playsound('test.wav')
            os.remove('test.wav')
            return output
    except:
        speak.speak("Nothing found from wikipedia")
        playsound('test.wav')
        os.remove('test.wav')

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
    speak.speak("fetching the news")
    playsound('test.wav')
    os.remove('test.wav')
    arts=news["articles"]
    head=[]
    new_url=[]
    day=['first','second','third','fourth','fifth']
    headlines=''
    for articles in arts:
        head.append(articles["title"])
        new_url.append(articles["url"])
    for i in range(len(day)):
        speak.speak(f"today's {day[i]} news is: {head[i]}")
        playsound('test.wav')
        os.remove('test.wav')
        headlines+=" "+str(i+1)+". "+str(head[i])+"---"+str(new_url[i])+"."   
    return headlines

def show_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

if __name__=="__main__":
    pass