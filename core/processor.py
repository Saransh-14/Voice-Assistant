from core.speaker import speak
import pywhatkit as kit
import utils.clock as clock
import utils.wiki as wiki
import utils.app_manager as am

google_triggo = [    "search google for", "open google and search about",
    "google", "open google and search", "search for", "look up", "find"]
yt_triggo = ["play", "play on youtube", "on youtube"]

def process_command(command):

#time telling function==================
    if "what" and "time" in command:
        speak(clock.curr_time())

# #wikipedia search===================== 
    elif any(key in command for key in wiki.wiki_triggers):
        result = wiki.wiki_result(command)
        if result == "multiple results":
            speak("There are multiple results. Please be more specific.")
        elif result == "page not found":
            speak("Sorry, I could not find anything on Wikipedia.")
        elif result == "something went wrong":
            speak("Something went wrong while searching Wikipedia.")
        else:
            speak(f"according to wikipedia, {result}")

#google browser search=================
    elif any(key in command for key in google_triggo):
        topic = command
        for key in google_triggo:
            if key in topic:
                topic = topic.replace(key, "")
        topic = topic.strip()
        speak(f"opening google to search {topic}")
        kit.search(topic)
        

#youtube accessing=====================
    elif any(key in command for key in yt_triggo):
        topic = command
        for key in yt_triggo:
            if key in topic:
                topic = topic.replace(key, "")
        topic = topic.strip()
        
        speak(f"playing {topic}")
        kit.playonyt(topic)
        
#app management========================
    elif any(key in command for key in am.fun_calls.keys()):
        app = command
        trigger = 0
        for key in am.fun_calls.keys():
            if key in command:
                app = app.replace(key,"")
                trigger = key
        app = app.strip()
        found = am.open_app(app, trigger)
        if found==0:
            speak("Sorry, Application Not Found")
        
        
    
    



