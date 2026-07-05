import os
import time

import notify2 as no

no.init("water reminder")

n = no.Notification("Water Reminder", "Drink water and take a break", "🌢")

# n.show()
print("\a")
t = int(time.time())
a = t
while True:
    n.show()
    os.system("play -n synth 0.5 sine 1000")  # beep for 0.5 seconds
    time.sleep(1)
