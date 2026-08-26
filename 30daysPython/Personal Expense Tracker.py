from datetime import datetime



class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")


    def display(self):
        print(f"Amount:{self.amount:.2f}")
        print(f"Category:{self.category}")
        print(f"Description:{self.description}")
        print(f"Date:{self.date}")

balance = []
def add_expense(amount, category, description):
    try:
       num = float(amount)
       balance.append(Expense(num,category,description))
       print(f"{num:.2f} is added to {category}")


    except (ValueError, TypeError):
        print("Invalid input. Enter valid number!")

        return

def display_all():
    if len(balance) == 0:
        print("No balance available!")
        return
    for b in balance:
        b.display()




def view_by_category(category):
    total = 0
    category_found = False
    for c in balance:
        if c.category.lower()== category.lower():
            category_found = True
            total += c.amount
            print(f"{c.description}:${c.amount:.2f}")

    if category_found:
        print(f"Total expenses on {category} is ${total}")

    else:
        print(f"No expenses found on this {category}")
    return total
def monthly_total ():
    current_month = datetime.now().strftime("%Y-%m")
    total = 0
    for b in balance:
        if b.date[:7] == current_month:
            total += b.amount

    print(f"Total expenses:{total}")

def biggest_expense():
    if not balance:
        print("No expenses found")
        return
    biggest = max(balance, key=lambda b:b.amount)
    print(f"Biggest expenses: {biggest.description} ${biggest.amount}")


budgets = {}

def set_budget(category, limit):
   budgets[category] = limit
   print(f"Budgets for {category} is set ${limit:.2f}")

def help_cal(category):
    total = 0
    for b in balance:
        if b.category.lower() == category.lower():
            total += b.amount
    return total



def check_budget(category):
    if category in budgets:

        diff = budgets[category] - help_cal(category)
        if diff > 0:
            print(f"You are on under budget by {diff}")

        elif diff < 0:
            print(f"You are over your limit budgets by {abs(diff)}")

        else:
            print("Exactly on budget")



def statistics():
    if len(balance) == 0:
        print(f" No data found")
        return
    total_spent = 0
    for b in balance:
        total_spent += b.amount
    print(f"Total spent overall: {total_spent}")

    biggest_expense()
    monthly_total()
    categories = set(b.category.lower() for b in balance)
    highest_category = max(categories, key=help_cal)
    print(f"Most expensive category is {highest_category} amount:{help_cal(highest_category)}")


def save_expense(filename="expenses.txt"):
    if len(balance) == 0:
        return
    with open(filename, "w") as f:
        for b in balance:
            f.write(",".join([b.category, str(b.amount), b.description, b.date]) + "\n")
    print(f"Successfully saved{len(balance)} expenses to {filename}.")


def load_expense(filename = "expenses.txt"):
    try:
        new_expenses = []
        with open (filename, "r") as f:
            for s in f:
                line = s.strip()
                parts = line.split(",")

                new = Expense( float(parts[1]),parts[0], parts[2])
                new.date = parts[3].strip()
                new_expenses.append(new)
            print(f"Loaded expenses {len(new_expenses)}")

    except FileNotFoundError:
        print("No Expenses saved")


    return new_expenses




def main():
    print("╔══════════════════════════════╗")
    print("║   PERSONAL EXPENSE TRACKER   ║")
    print("╚══════════════════════════════╝")
    global balance
    balance = load_expense()


    while True:
        print("\n1.Add expense")
        print("2.View by category")
        print("3.Monthly total")
        print("4.Biggest expense")
        print("5.Set budget limit")
        print("6.Display all expenses")
        print("7.Statistics")
        print("8.Save expenses")
        print("9.Check Budget")
        print("0.Exit")


        choice = int(input("Enter your choice:"))

        try:
            if choice == 1:
                amount =  float(input("Enter the amount you spent: "))
                category = input("Enter the category: ")
                description =  input("Enter the description: ")
                add_expense(amount, category, description)

            elif choice == 2:
                category = input("Enter the category: ")
                view_by_category(category)

            elif choice == 3:
                monthly_total()

            elif choice == 4:
                biggest_expense()

            elif choice == 5:
                category =  input("Enter the category: ")
                limit =  float(input("Enter the limit you want to set: "))
                set_budget(category,limit)

            elif choice == 6:
                display_all()

            elif choice == 7:
                statistics()

            elif choice == 8:
                save_expense(filename= "expenses.txt")

            elif choice == 9:
                category = input("Enter the category: ")
                check_budget(category)

            elif choice == 0:
                save_expense()
                print("Thank You, Bye! ")

                break
        except ValueError:
            print("Enter valid number")



if __name__== "__main__":
    main()





















