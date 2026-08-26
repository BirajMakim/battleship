#-------OOP----------
#----- Inheritance -----

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# # x = Person("Biraj", "Doe")
# # x.printname()
#
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname,lname)
#         self.graduationyear = year
#
#     def welcome(self):
#         print()
#
#
# x1 =  Student("Hitman", "Olsen", 2025)
# print(x1.graduationyear)



# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name)
#
# class Dog(Animal):
#     pass
# d1 = Dog("Rex")
# d1.speak()


# ----------Polymorphism---------
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#
#     def move(self):
#         print("Move!")
#
# class Car(Vehicle):
#     pass
#
# class Boat(Vehicle):
#     def move(self):
#         print("Sail!")
#
# class Plane(Vehicle):
#     def move(self):
#         print("Fly!")
#
# car1 = Car("Ford", "Mustang")
# boat1 = Boat("Ibiza", "Touring 20")
# plane1 = Plane("Boeing", "747")
# for x in (car1, boat1,plane1):
#     print(x.brand)
#     print(x.model)
#     x.move()

# class Cat:
#
#     def sound(self):
#         print("Meow")
#
# class Fox:
#     def sound(self):
#         print("Wa-pa-pa-pa-pa-pow!")
#
# c1 = Cat()
# f1 = Fox()
# for x in (c1,f1):
#     x.sound()


# --------- encapsulation-------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#
# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.get_age())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be positive")
#
#
# p1 = Person("Tobias", 25)
# print(p1.get_age())
# p1.set_age(26)
# print(p1.get_age())
#

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.__grade = 0
#
#     def set_grade(self,grade):
#         if 0 <= grade <= 100:
#             self. __grade = grade
#         else:
#             print("Grade must be between 0 and 100")
#
#     def get_grade(self):
#         return self.__grade
#
#     def get_status(self):
#         if self.__grade >= 60:
#             return "Passed"
#         else:
#             return "Failed"
# student = Student("Emil")
# student.set_grade(85)
# print(student.get_grade())
# print(student.get_status())

# class Person:
#     def __init__(self,name,salary):
#         self.name = name
#         self._salary = salary #Protected property
#
# p1 = Person("Linus", 5000)
# print(p1.name)
# print(p1._salary)
#
#
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def __validate(self, num):
#         if not isinstance(num, (int, float)):
#             return False
#         return True
#
#     def add(self, num):
#         if self.__validate(num):
#             self.result += num
#
#         else:
#             print("Invalid number")
# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)
#
#
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended