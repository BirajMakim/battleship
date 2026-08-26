# print("Welcome to Rollercoaster!")
# height = int(input("Enter your height in cm: "))
# ticket = 0
# if height >= 120:
#     print("You can ride rollercoaster")
#     age = int(input("Enter your age: "))
#     if age <= 12:
#         print("Child ticket is $5")
#         ticket = 5
#     elif age <=18:
#         print("Youth ticket is $12")
#         ticket = 12
#     else:
#         print("Adult ticket is $18")
#         ticket = 18
#
#     photo = input("Do you want your photo y/n: ")
#     if photo == "y":
#         ticket += 3
#         print(f"your ticket price is ${ticket}")
#
#     print(f"Your ticket price is ${ticket}")
# else:
#     print("You cann't ride")



# -------------------------pizza order------------------------
# print("Welcome to pizza Deliveries")
# size = input("Which size pizza do you want? S, M, L: ")
# pepperoni = input("Do want to add pepperoni? y/n: ")
# extra_cheese = input("Do you want to add extra cheese on pizza? y/n: ")
# pizza_price = 0
# if size == "s":
#     pizza_price = 15
# elif size == "m":
#     pizza_price = 20
# elif size == "l":
#     pizza_price = 25
# else:
#     print("Invalid error")
#
# if pepperoni == "y":
#     if size == "s":
#         pizza_price += 2
#     else:
#         pizza_price += 3
# else:
#     pizza_price = pizza_price
# if extra_cheese == "y":
#     pizza_price += 1
#     print(f"Your pizza price is ${pizza_price} ")
# else:
#     print(f"Your pizza price is ${pizza_price}")
#
#

# -------------treasure island------------------
# print("Welcome to Treasure Island.Your mission is to find the treasure.")
# direction = input("Choose Right or Left: ").lower()
# if direction == "left":
#     print("Congrats for surviving")
#     sec_level = input("Choose the option Wait or Swim?: ").lower()
#     if sec_level == "wait":
#         print("Congrats for surviving!")
#         third_level = input("Please choose the Door, Red, Yellow, Blue?: ").lower()
#         if third_level == "yellow":
#             print("You win!")
#         elif third_level == "red":
#             print("Burn by Fire. Game Over!")
#         else:
#             print("Eaten by beast. Game Over!")
#
#     else:
#         print("Attack by trout. Game Over")
# else:
#     print("Game over You fall into the hole")


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])