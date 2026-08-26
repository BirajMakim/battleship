#-----------modules ------------

# # 1. Built-in — comes with Python, no install needed
# import os
# import math
# import random
# import datetime
#
# # 2. Third-party — install with pip, then import
# import requests
# import pandas
#
#
# # 2. Third-party — install with pip, then import


# import mymodule
# # mymodule.greeting("Jonathan")
#
# # a = mymodule.person1["age"]
# # print(a)
#

# import mymodule as mx
# a = mx.person1["name"]
# print(a)


# import platform
# x = platform.processor()
# print(x)

# import platform
# x = platform.python_version()
# print(x)

# import math
# x = dir(math)
# print(x)
#
# import mymodule
# a = dir(mymodule)
# print(a)


# # import datetime
# x = datetime.datetime.now()
# print(x)

#
# import os
#
# print (os.getcwd())
# # os.mkdir("New_folder")
# print(os.listdir("."))

#
# import random
# print(random.randint(1,100))
# print(random.choice([""]))

# import os
# import random
#
# print (os.getcwd())
# # os.mkdir("python_practice")
# print(os.listdir())

# import random
# import string
#
# def generate_password(length = 8):
#     characters = string.ascii_letters + string.digits
#     password = ""
#     for i in range(length):
#         password += random.choice(characters)
#
#     return password
# print(generate_password())
# print(generate_password(12))
#

# import datetime
# from importlib.metadata import files
# from itertools import count
#
#
# def daily_logger(message):
#     now = datetime.datetime.now()
#     today = now.strftime("%d-%m-%y")
#     time = now.strftime("%H:%M:%S")
#     filename = f"log_{today}.txt"
#     with open(filename, "a") as f:
#         f.write(f"{time} {[message ]}\n")
#     with open(filename, "r") as f:
#         print(f.read())
#     return message
#
# daily_logger("System started")
# daily_logger("User logged in")
# daily_logger("Backup complete")


# import os
# def file_counter(path):
#     files = os.listdir(path)
#     count = len(files)
#     return f"Found {count} files in {path}"
# print(file_counter("."))