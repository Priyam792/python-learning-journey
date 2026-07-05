print("!!! WELCOME TO SNAKE , WATER , GUN !!!".center(50))
us = 0
bs = 0
name = str(input("Enter your name : "))
bot = "Gary"
b = int(input("Do you want to costumize your bot name ? \n1 for yes \n2 for no \n:"))
if b == 1:
    bot = str(input("Enter your BOT name : "))
else:
    print(f"Default BOT's name = {bot}")
c = {1, 2, 3}
d = {1: "SNAKE", 2: "WATER", 3: "GUN"}
rounds = int(input("How much round you want : "))


def choose():
    op = ["1 for SNAKE", "2 for WATER", "3 for GUN ", "4 for QUIT"]
    for i in range(2):
        print(op[i + i], op[i + i + 1].center(34))


for i in range(rounds):
    print(f"ROUND : {i + 1}")
    print("Enter your choice : ")
    choose()
    ch = int(input(": "))
    if ch == 4:
        break
    a = c.pop()
    print(f"\nYou choose {d[ch]} and Bot choose {d[a]}\n")
    c.add(a)
    if ch == a:
        print("!!! Draw !!!".center(35))
    elif (ch == 1 and a == 2) or (ch == 2 and a == 3) or (ch == 3 and a == 1):
        print("!!! You Win !!!".center(35))
        us = us + 1
    elif (ch == 1 and a == 3) or (ch == 2 and a == 1) or (ch == 3 and a == 2):
        print("!!! You lose !!!".center(35))
        bs = bs + 1

print(f"Your score : {us}\nBot's score : {bs}")
if us > bs:
    print(f"The winner is : {name}")
elif us < bs:
    print(f"The winner is : {bot}")
else:
    print(f"{name} and {bot} you both did your best . But there is no winner :)")
