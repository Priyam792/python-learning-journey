# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]

# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

# Note: If you are not using windows, try to figure out how to do the same thing using some other package


# -------------------using pyttsx3 ----------------------
import pyttsx3 as p

a = p.init()


a.setProperty("rate", 150)
a.setProperty("volume", 1.0)
voices = a.getProperty("voices")  # getting details of current voice
a.setProperty("voice", voices[1].id)
a.runAndWait()
l = ["priyam", "namit", "jitender", "nitin", "bittu"]
for i in l:
    a.say(f"shoutout to {i}")
    a.runAndWait()
