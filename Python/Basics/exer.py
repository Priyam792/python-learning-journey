import re
import time

import numpy as np

# pattern = r"\d+"
# text = """ My numbers are 12345 and 67890 and 11
# """

# match = re.findall(pattern, text)
# print(match)

# import json

# data = {"name": "Alice", "age": 25, "city": "New York"}
# # str = json.dumps(data)
# # print(type(str))
# with open("data.json", "w") as f:
#     json.dump(data, f)


# json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
# py_obj = json.loads(json_data)
# print(py_obj)
# print(type(py_obj))


# with open("data.json", "r") as file:
#     python_data = json.load(file)

# print(python_data)


# formatted_json = json.dumps(data, indent=4)
# print(formatted_json)


# a = np.array([1, 2, 4, 3])
# b = np.array([3, 5, 6, 2])
# b = a
# print(b)
# for i in b:
#     print(i)
# if 2 not in a:
#     print("y")
# else:
#     print("n")
# c = {4: 2, 5: 1, 6: 1}
# d = sorted(c.items(), key=lambda x: x[1])
# print(d)
# people = {"name": "Alice", "age": 30}
# print(people.items())

# for e, f in people.items():
#     print(e, ":", f)
# c = dict(zip(b, a))
# print(c)
# print(c[2])
# c = a + b
# print(c)

size = 1
a = list(range(size))
b = list(range(size))
start = time.time()
c = [x**y for x, y in zip(a, b)]
end = time.time()
print(f"List = {end - start}")

arr1 = np.array(a)
arr2 = np.array(b)
start = time.time()
fin = arr1 * arr1
end = time.time()
print(f"Array = {end - start}")

# arr = np.array([range(10, 101)])
# print(arr)
# print(arr.shape)
