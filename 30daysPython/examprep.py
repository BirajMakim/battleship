#
# # --------------------- OOP------------------
#
#
# class Myclass:
#     x = 5
# p1 = Myclass()
# p2 = Myclass()
# p3 = Myclass()
#
# print(p1.x)
# print(p2.x)
# print(p3.x)
from tabnanny import check
from tkinter.font import names

from django_browser_reload.views import message


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("Biraj", 24)
# print(p1.name)
# print(p1.age)


# ----------without __init__----------------
# class Person:
#     pass
# p1 = Person()
# p1.name = "Biraj"
# p1.age = 24
# print(p1.name)
# print(p1.age)

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age= age
#         self.grade= grade
#
# student1 = Student("Biraj", 24, "A+")
# student2 = Student("Diya", 22, "A")
# print(student1.age)
# print(student2.grade)


# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print("Hello, my name is " + self.name)
# p1 = Person("Biraj", 24)
# p1.greet()

# class Student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return "A+"
#         elif self.score >= 80:
#             return "A"
#         elif self.score >= 70:
#             return "B"
#         else:
#             return "C"
#
#     def introduce(self):
#         return f"Hi, I am {self.name} and my grade is {self.get_grade()}"
#
#
# s1 = Student("Biraj", 24, 92)
# print(s1.get_grade())
# print(s1.introduce())

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         return "Hello, " + self.name
#
#     def welcome(self):
#         message = self.greet()
#         print( message + "! Welcome to our website")
#
# p1 = Person("Biraj")
# p1.welcome()


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def summary(self):
#         print(F"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Pages: {self.pages}")
#
#
# b1 = Book("The Alchemist", "Paulo coelho", 208)
# b1.summary()
#
#
# class BankAccount:
#
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposite(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def show_balance(self):
#         print(f"Balance:{self.balance}")
#
# acc = BankAccount("Biraj", 1000)
# acc.deposite(500)
# acc.withdraw(200)
# acc.show_balance()
#
#
# class Employee:
#     def __init__(self, name,department, salary):
#         self.name = name
#         self.department = department
#         self.salary = salary
#
#     def give_raise(self,percent):
#         self.salary = ((percent/100)* self.salary) + self.salary
#
#     def details(self):
#         print(f"Name: {self.name}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")
#
# emp = Employee("Biraj", "IT", 50000)
# emp.give_raise(10)
# emp.details()
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# r1 = Rectangle(5, 10)
# print(r1.area())
# print(r1.perimeter())




# ---------Class Properties vs Object Properties-----


# class Person:
#     species = "Human"   #class property
#
#     def __init__(self, name):
#         self.name = name   #instance property
#
# p1 = Person("Biraj")
# p2 = Person("Diya")
# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)
#
#
# class Person:
#   lastname = ""
#
#   def __init__(self, name):
#     self.name = name
#
# p1 = Person("Linus")
# p2 = Person("Emil")
#
# Person.lastname = "Refsnes"
#
# print(p1.name, p1.lastname)
# print(p2.lastname)

# import math
#
# x1 = (-b + math.sqrt(b**2 -4*a*c))/ (2*a)
# x2 = (-b - math.sqrt(b**2 -4*a*c))/ (2*a)
#
# result = (a*(x**2+b))/(c*x + d)
#
# result = (3 + 4*x)/5 - (10*(y-5)*(a+b+c))/x + 9(4/x+(9+x)/y)




# for count in range(5):
#     print (count + 1, end =" ")
#
#
# for count in range(1, 4):
#     print (count, end =" ")




# for count in range(1, 6, 2):
#     print (count, end =" ")

# for count in range(6, 1, -1):
#     print (count, end =" ")


# for name in range(101):
#     print(str(name) + " Biraj")

# testString = "string"
# for ch in testString:
#     print(ch, ord(ch))


# x=12
# y=345
# z= 7
# print(f"{x:>6}{y:>6}{z:>6}")

# amount = 398.567567
# formated = format(amount, ".2f")
# print(formated)
#
# x = int(input ("Enter the num: "))
# if x < 0:
#     print(-x)
# else:
#     print(x)

# testString = "str i n g"
# count = 0
# for ch in testString:
#     if ch == ' ':
#         count += 1
# print("Number of spaces:", count)


# count = 0
#
# with open("myfile.txt", "r") as f:
#     for line in f:
#         count += 1
#
# print("Number of lines", count)
# filename = input("Enter the filename: ")
# count = 0
# with open(filename, "r") as f:
#     for line in f:
#         words = line.split()
#         for w in words:
#             if len(w) == 4:
#                 count += 1
#
#
# print("Number of four-letter words:", count)
#


# total = 0
# count = 0
# with open("num.txt", "r") as f:
#     for line in f:
#         num = int(line.strip())
#         total += num
#         count += 1
#
# if count>0:
#     average = total/count
#     print(f"Average: {average}")
# else:
#     print("File is empty")
#
#
#

# import string
# plaintext = input("Enter the plaintext: ")
# distance = int(input("Enter the distance value: "))
# encrypted = " "
# for char in plaintext:
#     encrypted += chr(ord(char) + distance)
#
# print(f"Encrypted text: {encrypted}")
#
# ciphertext = input("Enter the encrypted text: ")
# distance = int(input("Enter the distance value"))
#
#
# decrypted = " "
# for char in ciphertext:
#     decrypted += chr(ord(char) - distance)
#
# print(f"Decrypted text: {decrypted}")


# inputfile = input("Enter the input filename: ")
# outputfile = input("Enter the output filename: ")
# with open(inputfile, "r") as infile:
#     with open(outputfile, "w") as outfile:
#         for line in infile:
#             outfile.write(line)
# print("File is copied successfully")
#

# d = [5,7,9,6]
#
# d.append(10)
# print(d)
#
# d.insert(2,22)
# d.pop(1)
# newd = [90,89,101]
# d.extend(newd)
#
# index = d.index(7) if 7 in d else -1


# data = [  5,6,8,90,100]
# result= [ ]
# for num in data:
#     if num != 0:
#         result.append(num)
#
# print(result)
#
# def summation(low, high):
#     total = 0
#     for num in range(low, high + 1):
#         total += num
#     return total
# print(summation(1,6))


# data ={
#     "b": 20,
#     "a": 35
# }
#
# print(data['a'])
# data.get("c", None)
# print(data)
# print(data.keys())
# # data.pop("b")
# # print(data)
#
# for key in sorted(data.keys()):
#     print(key)


# def mean(num):
#     if len(num)==0:
#         return 0
#
#     return sum(num)/ len(num)
#
# def median(numbers):
#     if len(numbers) == 0:
#         return 0
#     sorted_num= sorted(numbers)
#     midpoint = len(sorted_num)//2
#     if len(sorted_num) % 2 == 0:
#         return (sorted_num[midpoint-1]+ (sorted_num[midpoint])) /2
#     else:
#         return sorted_num[midpoint]


# class Triangle:
#     number_of_sides = 3
#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2= angle2
#         self.angle3 = angle3
#
#
#     def check_angles(self):
#         if self.angle1 + self.angle2 + self.angle3 == 180:
#             return True
#         else:
#             return False
# my_triangle = Triangle(90,30,60)
# print(my_triangle.check_angles())
#
#
# class Song:
#
#
#     def __init__(self,lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         print(self.lyrics)
#
#
# happy_bday = Song(["May god bless you, ",
#                        "Have a sunshine on you,",
#                        "Happy Birthday to you !"])
# print(happy_bday.sing_me_a_song())

# class Lunch:
#     def __init__(self, menu):
#         self.menu = menu
#
#     def menu_price(self):
#         if self.menu == "menu 1":
#             print(f"Your choice: {self.menu} Price 12.00")
#         elif self.menu == "menu 2":
#             print("Your choice:", self.menu, "Price 13.40")
#         else:
#             print("Error in menu")
#
#
# # Test the class
# Paul = Lunch("menu 1")
# Paul.menu_price()


# def countdown(n):
#     if n <= 0:        # Stops at 0 OR any negative number
#         print("Go!")
#     else:
#         print(n)
#         countdown(n - 1)
#
# countdown(8)  # Safe! prints "Go!" immediately


# def sum_numbers(n):
#     if n == 0:           # Base case
#         return 0
#     else:
#         return n + sum_numbers(n - 1)  # Recursive case
#
# print(sum_numbers(5))



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))


# def hello (n):
#     if n <=0:
#         return
#     else:
#         print("Hello")
#         hello(n-1)
# hello(3)
#



