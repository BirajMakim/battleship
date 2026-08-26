import random
print("Welcome to Rock, Paper, Scissors game!")
choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors:\n "))
com_choice = random.randint(0, 2)
print(f"Computer choose {com_choice}")

if choice >= 3 or choice < 0:
    print("Invalid input, Please enter valid number: ")
elif choice == "0" and com_choice == "2":
    print("You win")
elif com_choice == "0" and choice == "2":
    print("You lose")
elif com_choice > choice:
    print("You lose")
elif choice > com_choice:
    print("You win")
elif choice == com_choice:
    print("It's a draw")





