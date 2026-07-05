import pyttsx3 as p

a = p.init()
a.setProperty("rate", 150)
a.setProperty("volume", 1.0)
voices = a.getProperty("voices")
a.setProperty("voice", voices[1].id)
v = input("Enter sentence to speech :: ")
a.say(v)
a.runAndWait()
