
students = {
    "Biraj": 98,
    "Diya": 91,
    "Bob": 81,
    "Alice": 75
}

def grade_calculator(score):
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B+"
    else:
        grade = "C"
    return grade

def add_student(name, score):
    students[name] = score

def remove_student(name):
    students.pop(name)

def show_report():
    print("\n--- Student Report ---")
    for name, score in students.items():
        grade = grade_calculator(score)
        print(f"{name}: {score} | Grade: {grade}")

def show_summary():
    scores = list(students.values())
    print("\n--- Class Summary ---")
    print(f"Highest: {max(scores)}")
    print(f"Lowest:  {min(scores)}")
    print(f"Average: {sum(scores)/len(scores):.2f}")

# --- Run it ---
add_student("Shakti", 60)
remove_student("Bob")
show_report()
show_summary()