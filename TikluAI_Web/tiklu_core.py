import datetime
import webbrowser
import os
import wikipedia
import random
import requests
import pyttsx3


IS_WEB_MODE = __name__ != "__main__"


engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"Jarvis: {text}")
    if not IS_WEB_MODE:
        engine.say(text)
        engine.runAndWait()

def get_news():
    speak("Fetching latest news...")
    webbrowser.open("https://news.google.com")

def get_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "I told my wife she should embrace her mistakes. She gave me a hug!",
        "What do you call fake spaghetti? An impasta!",
        "I would tell you a joke about UDP... but you might not get it.",
        "Why do cows have hooves instead of feet? Because they lactose!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    return random.choice(jokes)

def get_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3000 years old and still perfectly edible!",
        "A single cloud can weigh more than a million pounds.",
        "Bananas are berries, but strawberries are not!"
    ]
    return random.choice(facts)

def get_weather():
    api_key = "62a45ce0710bb2805d6ba2965c4cf806"
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Chakwal,PK&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 401:
            return "Invalid API key."
        elif response.status_code != 200:
            return f"Error - {data.get('message', 'Unknown error')}"
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return (
            f"Current weather in Chakwal, Pakistan:\n"
            f"- {weather.title()}\n"
            f"- Temperature: {temp}°C\n"
            f"- Humidity: {humidity}%\n"
            f"- Wind Speed: {wind_speed} m/s"
        )
    except Exception as e:
        return f"Failed to fetch weather due to error: {e}"

def get_tiklu_response(command):
    command = command.lower()
    
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The time is {now}"
        speak(response)
        return response

    elif "date" in command:
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        response = f"Today's date is {today}"
        speak(response)
        return response

    elif "datetime" in command or "date and time" in command:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = f"The current date and time is {now}"
        speak(response)
        return response

    elif "open google" in command:
        response = "Opening Google"
        speak(response)
        webbrowser.open("https://www.google.com")
        return response

    elif "open brave" in command:
        response = "Opening Brave Browser"
        speak(response)
        os.system("start brave")
        return response

    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        response = f"Searching Google for {query}"
        speak(response)
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return response

    elif "search wikipedia for" in command:
        query = command.replace("search wikipedia for", "").strip()
        speak(f"Searching Wikipedia for {query}")
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)
            return summary
        except wikipedia.exceptions.DisambiguationError:
            response = "Multiple results found. Please be more specific."
            speak(response)
            return response
        except wikipedia.exceptions.PageError:
            response = "No results found."
            speak(response)
            return response

    elif "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        response = f"Searching YouTube for {query}"
        speak(response)
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return response

    elif "open youtube" in command:
        response = "Opening YouTube"
        speak(response)
        webbrowser.open("https://www.youtube.com")
        return response

    elif "weather" in command:
        weather_report = get_weather()
        speak(weather_report)
        return weather_report

    elif "news" in command:
        speak("Fetching latest news...")
        get_news()
        return "Fetching latest news..."

    elif "joke" in command:
        joke = get_joke()
        speak(joke)
        return joke

    elif "fact" in command:
        fact = get_fact()
        speak(fact)
        return fact

    elif "open calculator" in command or "open cal" in command:
        response = "Opening Calculator"
        speak(response)
        os.system("calc")
        return response

    elif "open notepad" in command:
        response = "Opening Notepad"
        speak(response)
        os.system("notepad")
        return response

    elif "open command prompt" in command or "open cmd" in command:
        response = "Opening Command Prompt"
        speak(response)
        os.system("cmd")
        return response

    elif "shutdown" in command:
        response = "Shutting down the system"
        speak(response)
        os.system("shutdown /s /t 0")
        return response

    elif "restart" in command:
        response = "Restarting the system"
        speak(response)
        os.system("shutdown /r /t 0")
        return response

    elif "log off" in command:
        response = "Logging off the system"
        speak(response)
        os.system("shutdown /l")
        return response

    elif "exit" in command or "stop" in command:
        response = "Goodbye!"
        speak(response)
        return response

    else:
        response = "Sorry, I can't do that yet."
        speak(response)
        return response

def jarvis():
    speak("Hello, I am Jarvis. How can I assist you?")
    while True:
        command = input("You: ").lower()
        print("You said:", command)
        response = get_tiklu_response(command)
        if "goodbye" in response.lower():
            break

if __name__ == "__main__":
    jarvis()
