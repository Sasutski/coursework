from datetime import datetime
import speech_recognition as sr
import pyttsx4
import webbrowser 
import wikipedia
import wolframalpha
import validators
import subprocess

engine = pyttsx4.init('nsss')
voices = engine.getProperty('voices')

activationword = "computer"

def speak(text, rate=180):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print("Listening for Command")
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)
    try:
        print("Recognizing Command")
        query = listener.recognize_google(input_speech, language='en-GB')
        print(f"Input speech was: {query}\n")

    except sr.UnknownValueError:
        print("I did not quite catch that")
        speak("I did not quite catch that")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("I'm having trouble connecting to the server.")
        return "None"
    return query

if __name__ == '__main__':
    speak("All systems nominal")
    while True:
        query = parseCommand().lower()

        if query.startswith(activationword):
            query = query[len(activationword):].strip().split()

            # List commands
            if query[0] == "say":
                query.pop(0)
                if 'hello' in query:
                    print('Greetings All\n')
                    speak('Greetings All')
                else:
                    speech = ' '.join(query)
                    speak(speech)
            
            # open web browser
            if query[0] in ["go", "open", "visit"] and len(query) > 1:
                url = None
                if query[1] == "to":
                    query.pop(0)  # Remove the "go" command
                    query.pop(0)  # Remove the "to" command
                    url = ' '.join(query)
                elif query[1] == "the" and query[2] == "website":
                    query.pop(0)  # Remove the "open" command
                    query.pop(0)  # Remove the "the" command
                    query.pop(0)  # Remove the "website" command
                    url = ' '.join(query)
                else:
                    url = ' '.join(query[1:])  # Remove the command and join the rest of the query

                if not url.startswith('http'):
                    url = 'http://' + url
                if not validators.url(url):
                    speak("Invalid URL")
                else:
                    speak("Opening...")
                    webbrowser.open(url)
                    speak("Opened")

            # Check for updates
            if query[0] == "check" and query[1] == "updates":
                speak("Checking for updates...")
                try:
                    output = subprocess.check_output(["brew", "upgrade", "--formula", "--dry-run"])
                    updates_available = False
                    for line in output.decode("utf-8").splitlines():
                        if "would upgrade" in line:
                            updates_available = True
                            speak(f"Update available for {line.split()[1]}")
                    if not updates_available:
                        speak("Your system is up to date.")
                except subprocess.CalledProcessError as e:
                    speak("Error checking for updates.")
                    print(f"Error: {e}")

            # quit the AI
            if query[0] == "quit":
                break
