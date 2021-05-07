import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("JARVIS: ", audio)
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Halo bang yog!")
    else:
        speak("halo yog!")
        speak("Lets cekidot!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Silahkan bicara...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Memahami yang anda katakan...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
       
    except Exception as e:
        print(e)
        print("Maaf, silahkan coba lagi...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'buka youtube' in query:
            webbrowser.open("https:\\www.youtube.com")

        elif 'buka google' in query:
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            music_dir = 'D:\\#SEMESTER_6\\Artificial Intelegence\\Tubes\\Jarvis\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))
            
            
        elif 'open code ' in query:
            codePath = 'C:\\Users\\yoriz\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
