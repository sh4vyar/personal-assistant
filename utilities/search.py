import wikipedia
import pywhatkit

def search_web(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.DisambiguationError:
        return "The term is too ambiguous. Can you be more specific?"
    except Exception:
        return "I couldn't find anything about that."

def play_on_youtube(query):
    pywhatkit.playonyt(query)
