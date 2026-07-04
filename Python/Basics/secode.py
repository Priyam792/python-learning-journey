if __name__ == "__main__":
    print("What you want : ")
    print("Enter 1 for coding a code.\nEnter 2 for decoding a code.\n")
    a = int(input(":"))
c = {
    "hou",
    "ohf",
    "jfd",
    "owr",
    "iue",
    "isf",
    "suh",
    "osi",
    "qwi",
    "hzx",
    "xnm",
    "vnb",
    "hvg",
    "uwy",
}

if __name__ == "__main__":
    if a == 1:
        print(f"You choose {a}.")
        code = str(input("Enter your code : "))
        b = code.split(" ")

        for i in b:
            if len(i) < 3:
                temp = i[0]
                i = i[1:] + temp
                print(i)
            else:
                temp = i[0]
                d = c.pop()
                e = c.pop()
                i = d + i[1:] + temp + e
                print(i)
                c.add(d)
                c.add(e)
    elif a == 2:
        print(f"You choose {a}.")
        decode = str(input("Enter you code : "))
        f = decode.split(" ")

        for i in f:
            if len(i) < 3:
                temp = i[-1]
                i = temp + i[0]
                print(i)
            else:
                cu = i[3:-3]
                temp = cu[-1]
                i = temp + cu[0:-1]
                print(i)
