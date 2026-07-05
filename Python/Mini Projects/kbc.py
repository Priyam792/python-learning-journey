def quit():
    x = 0
    print("Do you want to quit ?")
    print("\nEnter '1' for yes \nEnter '2' for no ")
    x = int(input("\n →"))
    if x == 1:
        return 0
    else:
        return 1


def check(a, b):
    if a == b:
        return 0
    else:
        return 1


def options(*opt):
    c = ["a", "b", "c", "d"]

    opt1 = list(opt)
    for i in range(3):
        if i == 1 or i == 3:
            continue
        # le = str(i)
        # l = len(le)
        # print("⎺" * l)
        print(
            "(",
            c[i],
            ")",
            "|  ",
            opt[i],
            "|          ",
            "(",
            c[i + 1],
            ")",
            "|  ",
            opt[i + 1],
            "  |",
            "\n",
        )
        i = i + 1
        # print("⎺" * l)


print("!! Welcome to KBC !!".center(50))
print("\nWant to see the rules ?")
print("\nEnter '1' for yes \nEnter '2' for no ")
a = int(input("\n →"))
if a == 1:
    print(
        "If answer is correct then you win some money according to the question. \nIf the answer is incorrect then you lose all the money and don't able to continue the game. \nIf you want to quit the game with the money you won then you should quit before seeing the next question."
    )
else:
    pass
rs = 0
i = 0
ans = "a"
c = 0
while i == 0:
    print("\n\nQuestions : \n\n")
    print("1. Who is the cheif minister (C.M) of Tamil Nadu : ")
    options("Narendra Modi", "Ashok Gehalot", "Indra Gandhi", "Thalapathy Vijay")
    print("\n")
    ans = str(input("Enter your answer : "))
    c = check(ans, "d")
    if c == 0:
        rs = rs + 10000
    else:
        rs = rs - rs
        i = i + 1
    print("Your current balance : ", rs)
    c = quit()
    if c == 0:
        print("quitted succesfully")
        break
    else:
        pass

    print("2. In the Ramayana, who was the wife of Lord Rama? : ")
    options("Sita", "radha", "Draupadi", "Urmila")
    print("\n")
    ans = str(input("Enter your answer : "))
    c = check(ans, "a")
    if c == 0:
        rs = rs + 10000
    else:
        rs = rs - rs
        i = i + 1
        break
    print("Your current balance : ", rs)
    c = quit()
    if c == 0:
        print("quitted succesfully")
        break
    else:
        pass
