class library:
    def __init__(self):
        self.book = []
        self.nobook = 0

    def add(self):
        print("Do you want to add a book ?")
        a = input("Enter yes or no : ")
        while a == "yes" or a == "":
            b = input("Enter the name of the book : ")
            self.book.append(b)
            self.nobook += 1
            a = input("Add another : ")
        else:
            pass

    def check(self):
        if self.nobook == len(self.book):
            print(f"You entered {self.nobook} no. of books.")
        else:
            ValueError("No. of book is not equal to book in the list")

    def show(self):
        if self.nobook == 0:
            pass
        else:
            print("Your books are :")
            for i in self.book:
                print(i)


lib = library()
lib.add()
lib.check()
lib.show()
