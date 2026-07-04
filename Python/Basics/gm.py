import time

t = time.strftime("%H:%M")
h = int(time.strftime("%H"))
# print(h)
if 4 <= h < 12:
    print("GOOD MORNING.", " It's", t)
elif 12 <= h < 15:
    print("GOOD AFTERNOON.", " It's", t)
elif 15 <= h < 20:
    print("GOOD EVENING.", " It's", t)
else:
    print("GOOD NIGHT.", " It's", t)
