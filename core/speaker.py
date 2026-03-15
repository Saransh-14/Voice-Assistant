import pyttsx3 as tts

engine = tts.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices', )
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

