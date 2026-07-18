import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something ")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google_cloud(audio)
    print("You said:", text)

except Exception as e:
    print("Error ", e)
