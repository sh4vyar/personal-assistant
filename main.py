from utilities.weather import get_weather
from helpers.get_city import get_city
from utilities.reminders import add_reminder, list_reminders
from utilities.search import search_web, play_on_youtube
from assets.assistant import listen, speak

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if not command:
            continue

        if "weather" in command:
            res = get_weather(get_city())
            print(res)
            speak(res)
        elif "search" in command:
            query = command.replace("search", "").strip()
            result = search_web(query)
            speak(result)
        elif "play" in command:
            query = command.replace("play", "").strip()
            speak(f"Playing {query} on YouTube.")
            play_on_youtube(query)
        elif "reminder" in command:
            if "add" in command:
                reminder = command.replace("add reminder", "").strip()
                speak(add_reminder(reminder))
            elif "list" in command:
                speak(list_reminders())
        
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I didn't understand that. Can you try again?")

if __name__ == "__main__":
    main()
