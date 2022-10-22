import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id) #change index to change voices
engine.say('hii good morning')

engine.runAndWait()
