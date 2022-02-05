import pyttsx3 # pip3 install pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import psutil as ps
import pyjokes as pj
import os
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import python_weather
import pyowm

wolframalpha_app_id="4UH2XG-WKYV6E9PR7"
engine= pyttsx3.init()

def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def time_() :
    hh=datetime.datetime.now().strftime("%H: %M : %S ")
    l=hh.split(':')
    h=int(l[0])
    Time= datetime.datetime.now().strftime("%I : %M ")
    speak("It's")
    speak(Time)
    if(h>12):
        speak("PM")
    else:
        speak("AM")

def date_():
    date = datetime.datetime.now().strftime("%-d %B %Y")
    speak(date)

def greet():
    speak(" Hi!  kaushal welcome back ! ")
   
    hour= datetime.datetime.now().hour
    if(hour>=6 and hour<12):
        speak("good morning")
    elif hour>=12 and hour <18:
        speak("good afternoon")
    elif hour>=18 and hour<24:
        speak(" good evening ")
    else :
        speak(" wow ! you still awake? ")
    
    speak("How may I help You ?")



def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language="en-IN")
        print(query)
            
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content) :
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('kaushalmahajan08@gmail.com','ishwaree')
    server.sendmail('kaushalmahajan08@gmail.com',to,content)
    server.close()

def battery():
    battery_level=ps.sensors_battery()
    speak("battery is")
    speak(str(battery_level.percent))
    speak("percent")

def screenshot():
    os.system("screencapture screen.png")



if __name__=="__main__": 
    greet()

    while True :
        query=TakeCommand().lower()

        if 'time' in query :
            time_()

        elif 'date' in query:
            date_()
        
        elif 'wikipedia' in query:
            speak("Searching on wikipedia...")
            query=query.replace('wikipedia','')
            result= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia") 
            print(result)
            speak(result)
    
        elif 'send mail' in query :
            try :
                speak("Enter reciever's mail address")
                to = input("enter mail:")
                speak("what do you want to send ?")
                content=TakeCommand()
                speak(content)
                speak("shall i send ?")
                decision= TakeCommand()
                if decision=='yes' or decision=='yaa'or decision=='yep':
                    sendEmail(to,content)
                    speak("mail sent successfully")
                else :
                    break
            except Exception as e :
                speak ("sorry could not send mail")
        
        elif 'youtube' in query :
            speak("what do you want me to search ?")
            search_term=TakeCommand().lower()
            speak("searching on youtube..")
            wb.open("https://www.youtube.com/results?search_query="+search_term)

        elif 'google' in query :
            speak("what do you want me to search ?")
            search_term=TakeCommand().lower()
            speak("Searching Google..")
            wb.open("https://www.google.com/search?q="+search_term)
         
        elif 'battery' in query:
            battery()

        elif 'joke' in query:
            speak(pj.get_joke(language='en',category='all'))
        
        elif 'write a note'  in query  :
            speak("what should i write ?")
            note=TakeCommand()
            file=open('note.txt','w')
            file.write(note)
            speak("done!")
        elif 'show note' in query:
            speak("Showing notes")
            file=open('note.txt','r')
            print(file.read())
            speak(file.read()) 

        elif 'screenshot' in query :
            screenshot()

        elif 'Safari' in query:
            os.system("open /Applications/Safari.app")
        
        elif 'music' in query :
            os.system("open /System/Applications/Music.app")

        elif 'thanks' in query  or 'bye' in query  or 'get lost' in query  or 'offline' in query :
            speak("pleasure serving you!")
            speak("August signing off")
            quit()
        
        elif 'news' in query :
            try :
                news_url=urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=ea8eb1d0389c497393045b2b68ccb037")
                data=json.load(news_url)
                i=1
                speak("some top headlines are :")
                for item in data['articles']:
                    print(str(i)+'.'+item['title']+'\n')
                    speak(item['title'])
                    i+=1
                    if i>5:
                        break

            except Exception as e :
                speak("sorry could not fetch news for you")

        elif 'where is' in query:
            query=query.replace('where is','')
            speak("finding"+query)
            wb.open_new_tab("https://www.google.com/maps/place/"+query)

        elif 'my location' in query :
            wb.open_new_tab("https://www.google.com/maps/place/"+query)
            
        elif 'what is' in query or 'who is' in query :
            try:
                client=wolframalpha.Client(wolframalpha_app_id)
                question =query
                res=client.query(question)
                answer= next(res.results).text
                print(answer)
                speak(answer)
            except Exception as e:
                speak("no results found")
        elif 'calculate' in query :
            try:
                client=wolframalpha.Client(wolframalpha_app_id)
                question =query.replace('calculate','')
                res=client.query(question)
                answer= next(res.results).text
                print(answer)
                speak(answer)
            except Exception as e:
                speak("no results found")

        elif 'stop' in query or 'sleep' in query :
            i=1
            while i ==1:
                time.sleep(10)
                speak("shall i wake up?")
                ans=TakeCommand()
                if 'no' in query:
                    i==1
                else:
                    i==2

        elif 'what is your name' in query:
            speak("Hi ! I am august your virtual assistant, I am created by kaushal")

        elif 'love you' in query:
            speak("talking of love, I love you as a good boss")

        elif 'marry'in query :
            speak("umm, That seems tough")
        
        elif 'how are you' in query:
            speak("im fine sir all systems are good thanks for asking")

        elif 'what can you do' in query:
            speak("these are some tasks you can ask me")
            print("wikipedia india ...Take screenshot ...Search youtube ..Google search...Send mail .. Check battery ...Write a note....Open safari....Tell me news...Where is london....What is alpha ...Who is Lincoln...Calculate square root of 25...Sleep...bye....Tell me a joke ..Whats the time and date")
        

            
        else:
            speak("i am sorry , i didnt quite get you")
    
        



                
        




        
       

        
       