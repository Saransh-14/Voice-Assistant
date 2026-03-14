import pyttsx3 as tts

engine = tts.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices', )
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

