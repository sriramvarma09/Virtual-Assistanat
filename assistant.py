#engine.say()for talking
#engine.runandwait() for making sure audio is clear
#sr.microphone for accesing micro phone
import dictonary
import speech_recognition as sr
import pyttsx3                                  #speak
import pywhatkit                                #accesing yt
import datetime
import wikipedia
import pyjokes
from googlesearch import search
listner=sr.Recognizer()
engine=pyttsx3.init()                            #creating an engine instance for speacking
voices=engine.getProperty('voices')              #getting speech properties
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)        

def talk(text):
    print(text)
    info = wikipedia.summary(text, sentences=2,auto_suggest=False)            #gathering wikipedia info foe 2 lines
    engine.say(info)                             #speaking the info
    engine.runAndWait()
    print(info)                               

def take_command():
    with sr.Microphone() as source:
        print("what can i help")
        voice=listner.listen(source,phrase_time_limit=3)
        commands=listner.recognize_google(voice)
        commands=commands.lower()
        print(commands)  
    return commands

def singleword(command):
    ls=list(command.split(" "))
    if len(ls)==1:
        return True
    else:
        return False

   

def run():
    command = take_command()
    #print(command,"1")
    if 'play' in command:
        #print("playsome")
        song = command.replace('play', '')
        print(song)
        if command =='':
            engine.say("song is not set")
            engine.runAndWait()
            quit()
        engine.say('playing '+ song)
        engine.runAndWait()
        pywhatkit.playonyt (song)
    elif 'time' in command:
        #print("datesum")
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say('Current time is '+ time)
        engine.runAndWait()
    elif 'who is' in command:
        #print("who some")
        person = command.replace('who is','')
        print(person)
        talk(person)
    
    elif 'joke' in command:
        #print("in joke")
        jokees=(pyjokes.get_joke())
        engine.say(jokees)
        engine.runAndWait()
    elif singleword(command):
        for i in dictonary.dicto(command):
            engine.say(i)
            engine.runAndWait()
        
    
    elif 'exit' in command:
        #print("in exit")
        exit()
    
    
    else:
        #print("else")
         for j in search(command, tld="co.in", num=1, stop=1, pause=2):
            print(j)

while True:
    run()
'''elif 'on a date' in command:
        print("on some")
        engine.say('sorry, I have a headache')
        engine.runAndWait()
    elif 'are you single' in command:
        print("in some")
        engine.say('I am in a relationship with internet')
        engine.runAndWait()'''
