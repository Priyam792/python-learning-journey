# age = int(input("Enter your age : "))
# if age <18 :
#     print("Teen or child")
# else :
#     print("adult")

# for i in range (1,11):
#     print(i)

# for i in range (1 , 21):
#     if i%2 == 0:
#         print(i)

# i = int(input("Enter your age : "))
# if i == 0 :
#     print("Zero")
# elif i < 0 :
#     print("Negative")
# else :
#     print("Positive")

# r = 0 
# for i in range (1 , 101 ):
#     r +=i 

# print (r)

# for i in range(1, 6):
#     print("*" * i)

# num = 5
# factorial = 1
# for i in range(1, num + 1):
#         factorial *= i
# print(factorial)

# for i in range (1,11):
#     if i%3 ==0 :
#         pass
#     else :
#         print(i)

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

# import random

# print(random.randint(1, 10))   # random int
# print(random.random())         # 0 to 1
# print(random.choice([1,2,3]))  # random from list

# import re

# text = "Python is fun"
# result = re.match("Python", text)

# print(result)
# text = "I love Python"
# result = re.search("Python", text)

# print(result)


# numbers = [1, 2, 4, 3]
# numbers.append(5)      # add
# numbers.remove(2)      # remove
# print(numbers.sort())        # sort
# numbers.reverse()      # reverse

# ad = lambda a, b ,c: a + b + c
# print(ad(2, 3 , 4))

import numpy as np

arr = np.array([1, 2, 3, 4])
print(np.zeros((2,2)))