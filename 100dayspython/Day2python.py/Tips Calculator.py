# print("Welcome to Tips Calculator!")
# bill = float(input("What is the total bill?: "))
# tips = int(input("How much Tips would you like to give? 10, 12, 15: "))
# bill_split = int(input("How many people to split the bill: "))
# tips_cal = (bill + bill*(tips/100))/bill_split
# print(f"Each person should pay: ${tips_cal}")
#-------------odd and even num ------------

num = int(input("Enter the number: "))
if num % 2 == 0:
    print(f"Number {num} is even")
else:
    print(f"Number {num} is odd")