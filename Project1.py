#Student Management System (Python Console Application)

import json
import os

FILE_NAME = "students.json"


# -------------------------------
# Load Student Records
# -------------------------------
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


# -------------------------------
# Save Student Records
# -------------------------------
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


# -------------------------------
# Add Student
# -------------------------------
def add_student():
    print("\n------ Add Student ------")

    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:
            if student["Roll"] == roll:
                print("Student already exists!")
                return

        name = input("Enter Name: ")

        if not name.replace(" ", "").isalpha():
            print("Invalid Name!")
            return

        age = int(input("Enter Age: "))

        if age < 16 or age > 30:
            print("Age should be between 16 and 30.")
            return

        branch = input("Enter Branch: ")

        cgpa = float(input("Enter CGPA: "))

        if cgpa < 0 or cgpa > 10:
            print("CGPA should be between 0 and 10.")
            return

        student = {
            "Roll": roll,
            "Name": name,
            "Age": age,
            "Branch": branch,
            "CGPA": cgpa
        }

        students.append(student)
        save_students()

        print("Student Added Successfully!")

    except ValueError:
        print("Invalid Input!")


# -------------------------------
# View Students
# -------------------------------
def view_students():
    print("\n----------- Student Records -----------")

    if len(students) == 0:
        print("No Records Found.")
        return

    print("-" * 72)
    print("{:<10}{:<20}{:<10}{:<15}{:<10}".format(
        "Roll", "Name", "Age", "Branch", "CGPA"))
    print("-" * 72)

    for s in students:
        print("{:<10}{:<20}{:<10}{:<15}{:<10}".format(
            s["Roll"],
            s["Name"],
            s["Age"],
            s["Branch"],
            s["CGPA"]
        ))

    print("-" * 72)


# -------------------------------
# Search Student
# -------------------------------
def search_student():
    print("\n------ Search Student ------")

    try:
        roll = int(input("Enter Roll Number: "))

        for s in students:
            if s["Roll"] == roll:
                print("\nStudent Found")
                print("Roll   :", s["Roll"])
                print("Name   :", s["Name"])
                print("Age    :", s["Age"])
                print("Branch :", s["Branch"])
                print("CGPA   :", s["CGPA"])
                return

        print("Student Not Found!")

    except ValueError:
        print("Invalid Roll Number.")


# -------------------------------
# Update Student
# -------------------------------
def update_student():
    print("\n------ Update Student ------")

    try:
        roll = int(input("Enter Roll Number: "))

        for s in students:

            if s["Roll"] == roll:

                print("Leave blank to keep old value.")

                name = input(f"Name ({s['Name']}): ")
                if name != "":
                    s["Name"] = name

                age = input(f"Age ({s['Age']}): ")
                if age != "":
                    age = int(age)
                    if 16 <= age <= 30:
                        s["Age"] = age
                    else:
                        print("Invalid Age")

                branch = input(f"Branch ({s['Branch']}): ")
                if branch != "":
                    s["Branch"] = branch

                cgpa = input(f"CGPA ({s['CGPA']}): ")
                if cgpa != "":
                    cgpa = float(cgpa)
                    if 0 <= cgpa <= 10:
                        s["CGPA"] = cgpa
                    else:
                        print("Invalid CGPA")

                save_students()

                print("Record Updated Successfully!")
                return

        print("Student Not Found.")

    except ValueError:
        print("Invalid Input.")


# -------------------------------
# Delete Student
# -------------------------------
def delete_student():
    print("\n------ Delete Student ------")

    try:
        roll = int(input("Enter Roll Number: "))

        for s in students:

            if s["Roll"] == roll:
                students.remove(s)
                save_students()
                print("Student Deleted Successfully!")
                return

        print("Student Not Found.")

    except ValueError:
        print("Invalid Input.")


# -------------------------------
# Count Students
# -------------------------------
def total_students():
    print("\nTotal Students :", len(students))


# -------------------------------
# Menu
# -------------------------------
def menu():

    while True:

        print("\n")
        print("=" * 40)
        print("     STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Total Students")
        print("7. Exit")
        print("=" * 40)

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            total_students()

        elif choice == "7":
            print("\nThank You!")
            print("Project Closed Successfully.")
            break

        else:
            print("Invalid Choice.")


# -------------------------------
# Main
# -------------------------------
menu()