import datetime
from logging import exception
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis , Please Tell Me How May I Help You")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
        
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e) 
        print("Say That Again Please...")
        return "None"   
        
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lamegameryt20@gmail.com','Colarado123')
    server.sendmail('lamegameryt20@gmail.com',to,content)
    server.close()
    


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query, sentences=3)
            speak("According To Wikipedia")
            print(results)
            speak(results)
        elif "open youtube"in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("Google.com")
        elif "Anime" in query:
            webbrowser.open("gogoanime.fi")
        elif "Shopping" in query:
            webbrowser.open("amazon.in")
        elif "Play Music" in query:
           music_dir= 'D:\\Songs'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[5])) 
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath='C:\\Users\\rajashekar V.T\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'open valorant' in query:
            valorantPath= 'C:\Riot Games\Riot Client\\RiotClientServices.exe'
            os.startfile(valorantPath)
        elif 'open fortnite' in query:
            fortnitePath='D:\\Epic Games\\Epic Games\\Fortnite\\FortniteGame\\Binaries\\Win64\\FortniteLauncher.exe'
            os.startfile(fortnitePath)
        elif 'send email to raj' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="lamegameryt20@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry i am not able to send the email at the moment,please try again later")    
        elif('quit'or 'stop'or'shut down') in query:
            exit()
       
                           
