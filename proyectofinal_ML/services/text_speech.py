import pyttsx3
import speech_recognition as sr

# TTS
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    print(voice)
engine.setProperty('voice', 'spanish+f1')
engine.setProperty('rate', 145)

# STT
botName = "LLM"
listener = sr.Recognizer()


def text_to_speech(text):
     engine.say(text)
     engine.runAndWait()

def seepch_to_text():
     try:
          with sr.Microphone() as source:
               print("Escuchando...")
               pc = listener.listen(source)
               rec = listener.recognize_google(pc)
               rec = rec.lower()
               return rec
     except:
          print("Error: SR")