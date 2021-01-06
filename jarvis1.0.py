from ast import Index, fix_missing_locations
import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui
import random
import wolframalpha #pip install wolframalpha
import json
import requests
from urllib.request import urlopen
import time


from wikipedia.wikipedia import search


engine = pyttsx3.init()
wolframalpha_app_id = 'V95G9E-AVGER6EGVH'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Pekay Sir!!!")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("Good Morning Pekay Sir!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon Pekay Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Pekay Sir!")
    else:
        speak("Good Night Pekay Sir!")

    speak("Jarvis at your service. Please tell me how can I help you sir?")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again Please")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('useremail@gmail.com','passwors')
    server.sendmail('useremail@gmail.com',to,content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save('D:/jarvis/screenshots/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())


if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()


        if 'time' in query: 
            time_()

        if 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching.....")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)


        elif 'who am i' in query:
            speak("You are the creator of me! Literally my God!. Mr.Pranav alice Pekay, FOUNDER and CEO of Kryptonite Solutions")


        elif 'who is your creator' in query:
            speak("Mr.Pranav alice Pekay, FOUNDER and CEO of Kryptonite Solutions")


        elif 'who is pranav' in query:
            speak("Mr.Pranav alice Pekay, is the FOUNDER and CEO of Kryptonite Solutions India. He is also an Certified Ethical Hacker under EC-Council. who is specialized in cyber security analysis and cyber forensics and he is also a Full Stack Developer too...")
        
        
        elif 'who is pekay' in query:
            speak("Mr.Pranav alice Pekay, is the FOUNDER and CEO of Kryptonite Solutions India. He is also an Certified Ethical Hacker under EC-Council. who is specialized in cyber security analysis and cyber forensics and he is also a Full Stack Developer too...")


        elif 'who are you' in query:
            speak("Myself Jarvis. An Artificial Intelligence Based Voice Assistant Created By Mr.Pranav alice Pekay.!")


        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=TakeCommand()
                receiver='receiver_is_me@gmail.com'

                speak("who is the receiver")
                receiver=input("Enter Receiver's Email ID:")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('Email sent successfully.')

            except Exception as e:
                print(e)
                speak("unable to send Email.")


        elif 'search in chrome' in query:
            speak('What should i search for you sir?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'search in youtube' in query:
            speak('What should i search for you in youtube sir?')
            search_Term = TakeCommand().lower()
            speak("Here we go to YOUTUBE!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search in google' in query:
            speak('What should i search for you in google sir?')
            search_Term = TakeCommand().lower()
            speak("Searching...!")
            wb.open('https://www.google.com/search?q='+search_Term)


        elif 'cpu' in query:
            cpu()


        elif 'joke' in query:
            joke()

        
        elif 'go offline' in query:
            speak('Going offline sir!')
            quit()

        elif 'ms word' in query:
            speak('Opening Microsoft Word......')
            ms_word = r'C:/Program Files/Microsoft Office/root/Office16/winword.exe'
            os.startfile(ms_word)


        elif 'powerpoint' in query:
            speak('Opening Microsoft powerpoint......')
            powerpoint = r'C:/Program Files/Microsoft Office/root/Office16/powerpnt.exe'
            os.startfile(powerpoint)


        elif 'settings' in query:
            speak('Opening settings......')
            settings = r'C:/WINDOWS/System32/control.exe'
            os.startfile(settings)


        elif 'firefox' in query:
            speak('Opening Firefox......')
            firefox = r'C:/Program Files/Mozilla Firefox/firefox.exe'
            os.startfile(firefox)


        elif 'chrome' in query:
            speak('Opening Google Chrome......')
            google_chrome = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
            os.startfile(google_chrome)


        elif 'vs code' in query:
            speak('Opening Microsoft Visual Code......')
            vscode = r'C:/Users/pranav/AppData/Local/Programs/Microsoft VS Code/Code.exe'
            os.startfile(vscode)


        elif 'virtualbox' in query:
            speak('Opening Oracle Virtual Box......')
            virtualbox = r'D:/virtualbox/VirtualBox.exe'
            os.startfile(virtualbox)


        elif 'vmware' in query:
            speak('Opening VM Ware......')
            vmware = r'C:/Program Files (x86)/VMware/VMware Workstation/vmware.exe'
            os.startfile(vmware)


        elif 'whatsapp' in query:
            speak('Opening whatsapp......')
            whatsapp = r'C:/Users/pranav/AppData/Local/WhatsApp/WhatsApp.exe'
            os.startfile(whatsapp)

        elif 'take notes' in query:
            speak('What contents should i take notes sir?')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak("sir should i include Date and Time in your notes?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, SIR!')
            else:
                file.write(notes)

        elif 'read notes' in query:
            speak('Reading Saved notes')
            file = open('notes.txt','r')
            speak(file.read())
            print(file.read())


        elif 'screenshot' in query:
            speak('Took ScreenShot sir!')
            screenshot()

        elif 'play videos' in query:
            songs_dir = 'D:/Courses/Bug Bounty _ Web Hacking'
            music = os.listdir(songs_dir)
            speak('Which music should i play sir?')
            speak('select a number...')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                speak('I could not understand you. Please try Again.')
                ans = TakeCommand().lower()
            if 'number' in ans:
               no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
               no = random.randint(1,100)    
            os.startfile(os.path.join(songs_dir,music[no]))


        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The answer is : '+answer)
            speak('The answer is'+answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results.")
            

        elif 'remember this' in query:
            speak('what should i remember?')
            memory = TakeCommand()
            speak("you asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You Asked Me to remember that'+remember.read())

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f3b399cb920c43318f9cc75f59170068")
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top headlines from the Business Insustry')
                print('===================TOP HEADLINES==================='+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                    print(str(e))


        elif 'stop listening' in query:
            speak('For How many seconds you want me to stop listening to your commands sir?')           
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans) 


        elif 'log out' in query:
            os.system("shutdown -1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")





        




        
            





    







