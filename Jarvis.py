#RESEARCH TOPIC
'''
ARTIFICIAL INTELLIGENCE
WORKING ON A CHATBOT
Desktop Assistant
'''
#IMPORTING ALL THE NECESSARY LIBRARIES OR MODULES:::--
import pyttsx3                                   
import datetime                           
import speech_recognition as sr                    
import wikipedia                                  
import webbrowser                                 
import random                                                                           
import calendar
import subprocess as sp
import os                                             
import subprocess
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
dirpath=[]
folder=[]
engine = pyttsx3.init()                           
voices = engine.getProperty('voices')             
engine.setProperty('voice',voices[1].id)          
#functions are defined here ## METHODS-->#
'''--------------------------------------------------------'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
'''--------------------------------------------------------'''
def open_notepad():
    programName= "notepad.exe"
    sp.Popen([programName])
def day_today():
    datetime.datetime.now("%A")
    print(now.strftime("%A"))
    speak(now.strftime("%A"))
'''---------------------------------------------------------'''
def display_process():
    sp.call([r'testing.bat'])  
    file1 = open('process.txt', 'r') 
    Lines = file1.readlines() 
    count = 0
    # Strips the newline character 
    for line in Lines: 
        print("Line{}: {}".format(count, line.strip()))
def explore(path):
    # explorer would choke on forward slashes
    import os
    entries = os.listdir(path)
    for item in range(0,len(entries)):
        print(item,"=",entries[item])
        folder.append(entries[item].lower())
        
    path = os.path.normpath(path)
    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', path])
'''--------------------------------------------------------'''
def open_calculator():
    programName= "calc.exe"
    sp.Popen([programName])
def shopping_on_google():
    speak('What Do You Want?')
    S=takeCommand()
    webbrowser.open("https://www.google.com/search?q="+S+"&sxsrf=ALeKk03t3XY_tsWX8E_-kcnqziiHJbbcNA:1611055413627&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjt2ZGN8afuAhXRzTgGHet-BXsQ_AUoAXoECAQQAw&biw=1600&bih=841")
'''--------------------------------------------------------'''
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born])
'''--------------------------------------------------------'''
def open_paint():
    programName = "mspaint.exe"
    sp.Popen([programName])
'''--------------------------------------------------------'''
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
'''--------------------------------------------------------'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("LISTENING...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You Said",query)
    except Exception as e:
        print(e)
        print("COULD NOT RECOGNIZE SAY AGAIN PLEASE..")
        return "None"
    return query
###############################################################################
'''--------------------------------------------------------'''
if __name__ == "__main__":
   wishMe()
   while True:
       
       query = takeCommand().lower()
       

       if 'wikipedia' in query:
           speak("What do you want to search")
           
           ask = takeCommand()
           results = wikipedia.summary(ask, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
           continue
       elif 'show system process' in query:
           speak("Showing System Process")
           display_process()
           continue
       elif 'open youtube' in query:
           speak("opening youtube")
           webbrowser.open("www.youtube.com")
           continue
       elif 'open google' in query:
           speak("opening google")
           webbrowser.open("www.google.com")
           continue
       elif 'open facebook' in query:
           speak("searching")
           webbrowser.open("www.facebook.com")
           continue
       elif 'open stack overflow' in query:
           speak("Searching")
           webbrowser.open("www.stackoverflow.com")
           continue
       elif "folder" or "Folder"  or "FOLDER" in query:
        for item in range(0,len(folder)):
            if folder[item] in query.lower():
                print("!!!!!!!!!",dirpath[0]+folder[item])
                explore(dirpath[0]+folder[item])
            else:
                print("folder does not exist")
        
        continue
       elif 'play music' in query:
           speak("Please wait playing the song")
           directory = 'C:\\Users\ANSH4177\Desktop\songs'
           songs = os.listdir(directory)
           s = random.choice(songs)
           os.startfile(s)
           continue
       elif 'day' in query:
           speak("the day today is")
           day_today()
           continue
       elif 'what is the time' in query:
           strTime = datetime.datetime.now().strftime("%H %M")
           speak("sir the time is"+strTime+"")
           continue
       elif 'hello' in query:
           speak("Hello Sir.")
           continue
       elif 'date today' in query:
           now = datetime.datetime.now()
           print ("Current date : ")
           print (now.strftime("%Y-%M-%D"))
           speak(now.strftime("%Y-%M-%D"))
           continue
       elif 'what is my name' in query:
           speak("your name is aansh")
           continue
       elif 'open notepad' in query:
           speak("opening notepad")
           open_notepad()
           continue
       elif 'open paint' in query:
           speak("opening paint")
           open_paint()
           continue
       elif 'Shop' or 'shop' or 'buy' or 'Buy' in query:
           shopping_on_google()
       elif 'open calculator' in query:
           speak("opening calculator")
           open_calculator()
           continue
       elif 'what is your name' in query:
           speak("My name is Jarvis, Sir!")
           continue
       elif 'how are you' in query:
           speak(" I am fine sir, thank you!!")
           continue
       elif 'directions' or 'Directions' or 'Route' or 'route' in query:
           speak("Where do you want to go, sir")
           location = takeCommand()
           speak("Hold On Sir I Will Show You Where"+location+"")
           webbrowser.open("https://www.google.com/maps/place/"+location+"")
           continue
       elif 'open drive' in query:
           speak("Which Drive you want to open, sir")
           drive=takeCommand()
           if 'C' in drive or 'c' in drive:
               os.startfile("C:")
           elif 'D' in drive or 'd' in drive:
               os.startfile("D:")
           elif 'E' in drive or 'e' in drive:
               os.startfile("E:")
           else:
               speak("DRIVE DOES NOT EXIST")
           continue
       elif 'show files ' in query or 'print files from drive' in query:
           speak("From Which drive, Sir")
           drive = takeCommand()
           c='y'
           while(c=='y'):
               
               if 'C' in drive or 'c' in drive:
                   os.listdir("C:")
                   entry = os.listdir("C:")
                   for i in range(0,len(entry)):
                       print(i,"=",entry[i])
               elif 'D' in drive or 'd' in drive:
                  os.listdir("D:")
                  entry = os.listdir("D:")
                  for i in range(0,len(entry)):
                      print(i,"=",entry[i])
               elif 'E' in drive or 'e' in drive:
                   os.listdir("E:")
                   entry = os.listdir("E:")
                   for i in range(0,len(entry)):
                       print(i,"=",entry[i])
               else:
                   speak("DRIVE DOES NOT EXIST")
               speak("Do You Want to Exit Drive Explorer")
               c = takeCommand()
               if 'yes' in c:
                   speak("Exiting The Drive Explorer")
                   break
               else:
                   continue
               
       elif 'hey jarvis' in query:
           speak(" I AM AWAKE, SIR")
           continue
       elif 'thank you jarvis' in query:
           speak("Your Welcome Sir")
           continue
       elif 'open whatsapp' in query:
           webbrowser.open("https://web.whatsapp.com/")
           continue
       elif 'search google' in query:
           speak("What do you want to search, sir")
           S = takeCommand()
           webbrowser.open("https://www.google.com/search?q="+S+"")
           continue
       elif 'wake me' in query:
           d = 'C:\\Users\ANSH VOHRA\Desktop\songs'
           songs = os.listdir(d)
           os.startfile(os.path.join(d, songs[0]))
           continue
       elif 'netflix' in query:
           speak("openning app")
           os.system("start Netflix:")
           continue
       elif 'open spotify' in query:
           os.system('start spotify:')
           continue
       elif 'photos' in query:
           os.system("start Photos:")
           continue
       elif 'temperature outside' in query:
           
           continue
       elif 'quit' in query:
           speak("BYE SIR, HAVE A GOOD DAY")
           break
'''----------------------------------------------------------------------------'''
###------------------------------------------------------------------------###
###--------------###-------------###------------###-------------###
     
           
           
         
           
   
        