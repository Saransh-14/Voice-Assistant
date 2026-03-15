import speech_recognition as sr
r = sr.Recognizer()
r.energy_threshold = 350
r.pause_threshold = 2

def listen():

    text = ""    

    with sr.Microphone() as source:
        # print("Adjust for background noise please wait......")
        r.adjust_for_ambient_noise(source, duration=1)
        
        print("listening.....")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        # print("You said: ",command)
    except sr.UnknownValueError:
        print("Sorry...couln't understand")
    except sr.RequestError:
        print("Internet Error couldn't load the request")

    return text.lower()

# command = listen()
# print("You said: ",command)

