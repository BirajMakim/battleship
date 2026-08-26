# ---------------functions----------
from django_browser_reload.views import message


#
# def greet(name):
#     return f"Hello, {name}!"
#
# print(greet("Biraj"))
# print(greet("Bob"))


#-----Multiple parameters----------


# def add (a, b):
#     return a + b
# print(add(3, 5))
# print(add( 20, 80))



# def greet(name, language= "English"):
#     if language == "Nepali":
#         return f"Namaste, {name}!"
#     return f"Hello, {name}!"
#
# print(greet("Biraj"))
# print(greet("Biraj", "Nepali"))

#
# def calculate_avg(scores):
#     return sum(scores)/len(scores)
#
# marks = [88, 74, 92, 65, 79]
# print(f"Class average: {calculate_avg(marks):.2f}")


# def my_function():
#     print("Hello from a function")
#
# my_function()

# def covert_Temp(fahrenheit):
#     return (fahrenheit-32) *5/9
# print(covert_Temp(100))
#
#
#
# def get_greeting():
#     return "Hello from a function"
# # message = get_greeting()
# # print(message)
# #
# # print(get_greeting())

# def my_funtion(fname):
#     print(fname + " Refsnes")
# my_funtion("Emil")
# my_funtion("biraj")


# def my_function(name):
#     return "hello " +  name
# print(my_function("biraj"))


# def my_funtion(fname, lname):
#     return fname + lname
# print(my_funtion("Biraj", " Makim"))
#


# def my_function(name = " friend"):
#     print("Hello", name)
# my_function("DIYA")
# my_function()



# def my_function ( animal, name):
#     print("I have ", animal)
#     print("My dog name is", name)
# my_function(animal= "Dog", name="Lilly")

# def my_function(fruits):
#     for fruit in fruits:
#         print(fruit)
# my_fruits = ["Orange", "Banana", "Apple", "Mango"]
# my_function(my_fruits)


# def my_function(person):
#     print("Name: ", person["name"])
#     print("Age: ", person["age"])
#     print("Address: ", person["Address"])
#
# my_dict = {"name": "Biraj", "age": 24, "Address": "Thomastown"}
# my_function(my_dict)


# def my_function():
#     return ["apple", "Mango", "Banana"]
# fruits = my_function()
# print(fruits[0])
#

# print(f"Model {model} achieved {accuracy} % accuracy")
# print("That is " + str(accuracy) + "% which is " + ("great" if accuracy > 90 else "okay"))
#


# def summarise_data(numbers):
#
#     minimum = min(numbers)
#     maximum = max(numbers)
#     count= len(numbers)
#     average = sum(numbers)/ len(numbers)
#
#     return {
#         "min": minimum,
#         "max": maximum,
#         "average": average,
#         "count": count
#
#
#     }
#
#
# data = [45, 88, 92, 74, 61, 79, 83]
# result =  summarise_data(data)
# print(f"Count: {result['count']}")
# print(f"Max: {result['max']}")
# print(f"Min: {result['min']}")
# print(f"Average: {result['average']:.2f}")
#
#
# def clean_name(name):
#     name = name.strip()
#     name = name.capitalize()
#     return name
# print(clean_name("Alice"))