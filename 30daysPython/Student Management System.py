from datetime import datetime




class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.scores = []
    def add_score(self,*score):
        for s in score:
            if 0 <= s <= 100:
                self.scores.append(s)

            else:
                print("Please Input valid number")
        return self.scores


    def average(self):
        if len(self.scores)==0:
            return 0
        return sum(self.scores) /len(self.scores)

    def grade(self):
        if self.average() >= 90:
            return "A+"
        elif self.average() >= 80:
            return "A"
        elif self.average() >= 70:
            return "B+"
        elif self.average() >= 60:
            return "C"
        else:
            return "F"
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Score:{self.scores}")
        print(f"Average:{self.average()}")
        print(f"Grade:{self.grade()}")


students = []

def add_student(students, name, age):

    students.append(Student(name,age))


def add_score_to_student(students):
    name = input("Enter the student name: ")
    for student in students:
        if student.name.lower() == name.lower():
            try:
                # User enters space-separated values: 85 92 78
                raw_input = input(f"Enter scores for {student.name} (separated by spaces): ")
                scores_list = [int(s) for s in raw_input.split()]

                # Pass unpacked scores into add_score(*score)
                student.add_score(*scores_list)
                print(f"Successfully added scores to {student.name}.")
            except ValueError:
                print("Invalid input! Please enter numbers separated by spaces.")
            return
    print(f"Student '{name}' not found!")

def remove_student(students,name):

    for x in students:
        if x.name.lower() == name.lower():
            students.remove(x)
            print(f"{name} removed")
            return
    print(f"Student {name} not found!")





def search_students(students, name):
    for x in students:
        if  x.name.lower() == name.lower():
            x.display()
            return x


        else:
            pass
    print("Student not found")


def display_all(students):
    if len(students) == 0:
        print("No students yet!")
        return
    for x in students:
        x.display()

def class_stats(students):

    stud_score = []
    for x in students:
        stud_score.extend(x.scores)
    if not students:
        print("No students in the class")
        return

    if not stud_score:
        print("No scores recorded for any student yet.")
        return

    highest_score =max(stud_score)
    lowest_score = min(stud_score)
    class_average = sum(stud_score)/len(stud_score)

    print(f"The highest score in the class is {highest_score}")
    print(f"The lowest score in the class is {lowest_score}")
    print(f"The class average is {class_average}")

    highest_average = 0
    top_student = None
    for x in students:
        if x.average() > highest_average:
            highest_average = x.average()
            top_student = x.name
    print(f"The top student name is {top_student} with and average of {highest_average}")




def save_students(students, filename="students.txt"):
    with open(filename, "w") as f:



        for student in students:
            text_scores = [str(s) for s in student.scores]


            combined_scores = ",".join(text_scores)
            text_line=f"{student.name},{student.age},{combined_scores}\n"
            f.write(text_line)

    now = datetime.now()

    todays_time = now.strftime("%Y-%m-%d at %H:%M:%S")
    print(f"Saved on {len(students)} students! " )
    print( f" Timestamp: {todays_time}")


def load_students(filename):
    new_list_student = []

    try:

        with open(filename, "r") as f:
            for l in f:
                clean_line =l.strip()
                if clean_line == "":
                    continue
                parts = clean_line.split(",")
                new_student = Student(parts[0],int(parts[1]))
                for n in parts[2:]:
                    if n != "":
                        num = int(n)
                        new_student.add_score(num)
                new_list_student.append(new_student)
        print(f" loaded {len(new_list_student) } students!")
    except FileNotFoundError:
        print("No save file found")
    return new_list_student



def main():
    print("╔══════════════════════════════╗")
    print("║   STUDENT MANAGEMENT SYSTEM  ║")
    print("╚══════════════════════════════╝")
    students = []

    while True:
        print("\n1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Class statistics")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Add score to student")
        print("0. Exit")

        choice = input("Enter your choice: ")
        try:

            if choice == "1":
                stud_name = input("Enter the student name: ")
                stud_age = int(input("Enter the student age: "))
                add_student(students,stud_name,stud_age)


            elif choice == "2":
                remove_stud = input("Enter the student name you would like to remove: ")
                remove_student(students,remove_stud)


            elif choice == "3":
                search_stud = input("Enter the name of student: ")
                search_students(students,search_stud)

            elif choice == "4":
                display_all(students)

            elif choice == "5":
                class_stats(students)

            elif choice == "6":
                save_students(students)

            elif choice == "7":

                students = load_students("students.txt")

            elif choice == "8":
                add_score_to_student(students)







            elif choice == "0":
                print("Good bye!")

                break


        except ValueError:
            print("Enter the valid number")



if __name__ == "__main__":
    main()




