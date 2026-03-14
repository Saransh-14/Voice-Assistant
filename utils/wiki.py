import wikipedia

wiki_triggers = ["what is", "who is", "tell me about", "seach the wikipedia", "tell me something about"]

# result = wikipedia.summary("guido van rossum", sentences=5)
# print(result)

def wiki_result(text):
    topic = text
    for key in wiki_triggers:
        topic = topic.replace(key, "")

    topic = topic.strip()
    print(topic)
    
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError:
        return "multiple results"
    except wikipedia.exceptions.PageError:
        return "page not found"
    except Exception:
        return "something went wrong"