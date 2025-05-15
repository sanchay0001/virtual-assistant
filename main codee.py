import speech_recognition as sr  # For recognizing speech input from the microphone
import pyttsx3  # For converting text to speech (TTS)
import pywhatkit  # For playing YouTube videos, sending messages, etc.
import datetime  # To get the current date and time
import wikipedia  # To fetch summaries from Wikipedia
import pyjokes # For telling random jokes

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()  # #SpeechRecognition: create a listener to recognize speech
engine = pyttsx3.init()  # #TTS: initialize the text-to-speech engine

# Set voice property to a female voice (index 1)
voices = engine.getProperty('voices')  # #TTS: get available voices
engine.setProperty('voice', voices[1].id)  # #TTS: set voice to female (you can try voices[0] for male)

# Function to make the assistant speak
def talk(text):  # #TTS function: speak the provided text
    engine.say(text)  # Queue the text to speak
    engine.runAndWait()  # Run the speech engine

# Function to listen to the user's voice command
def take_command():
    command = ""  # #Initialize
    try:
        with sr.Microphone() as source:
            print('Listening...')  # #MicrophoneActive
            voice = listener.listen(source)
            command = listener.recognize_google(voice)  # #GoogleSpeechRecognition
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')  # #WakeWordRemoved
                print(f"Recognized command: {command}")
    except Exception as e:
        print(f"Error: {e}")  # #ErrorLog
    return command  # Always return something, even if blank

# Function to process and respond to commands
def run_alexa():  # #Main Logic: process command and perform actions
    command = take_command()  # Get the user's voice input
    print(command)  # Print it for debugging
    if 'play' in command:  # If command includes 'play'
        song = command.replace('play', '')  # Extract song name
        talk('playing ' + song)  # Inform the user
        pywhatkit.playonyt(song)  # Play the song on YouTube
    elif 'time' in command:  # If command includes 'time'
        time = datetime.datetime.now().strftime('%I:%M %p')  # Get current time in 12-hour format
        talk('Current time is ' + time)  # Speak the time
    elif 'who is' in command:  # If command asks 'who is'
        person = command.replace('who is', '')  # Extract the person's name
        info = wikipedia.summary(person, 1)  # Get a 1-sentence summary from Wikipedia
        print(info)  # Print it
        talk(info)  # Speak it
    elif 'joke' in command:  # If command includes 'joke'
        talk(pyjokes.get_joke())  # Speak a random joke
    

# Keep the assistant running in an infinite loop
while True:  # #Loop: continuously listen and respond
    run_alexa()
