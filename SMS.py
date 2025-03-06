"""" 
📌 Overview
The Student Management System is a Python-based program designed to store,
manage, and manipulate student records efficiently. 
This project provides basic functionality such as adding, displaying, searching, updating,
and deleting student information. 
"""
import termcolor
from termcolor import colored
# import pyfiglet

print(termcolor.colored(("\n📚 Student Management System\n"), color="green"))

# Student database
data_list = []  

# Menu System
def menuSystem():
    print(f"""{termcolor.colored("1. ", color="red")}Add Student
{termcolor.colored("2. ", color="red")}Display All Students
{termcolor.colored("3. ", color="red")}Search Student
{termcolor.colored("4. ", color="red")}Update Student
{termcolor.colored("5. ", color="red")}Delete Student
{termcolor.colored("6. ", color="red")}Exit
""")

menuSystem()  # Display menu

# Function to add students
def add_students():
    num_students = int(input(colored("Enter the number of students to add: ", "green")))

    for i in range(num_students):
        print(colored(f"\nEnter data for student {i + 1}:", "blue"))

        student_data = {
            "name": input(colored("Enter Name: ", "cyan")),
            "age": int(input(colored("Enter Age: ", "cyan"))),
            "id": input(colored("Enter ID: ", "cyan")),
            "grade": input(colored("Enter Grade: ", "cyan"))
        }

        data_list.append(student_data)
    print(colored("\nStudents added successfully!", "green"))

# Function to display all students
def display_students():
    if not data_list:
        print(colored("\nNo students found!", "red"))
        return

    print(colored("\nStudent Records:", "yellow"))
    for idx, student in enumerate(data_list, start=1):
        print(colored(f"Student {idx}: {student}", "magenta"))

# Function to search for a student by ID
def search_student_by_id():
    search_id = input(colored("\nEnter Student ID to search: ", "yellow"))
    for student in data_list:
        if student["id"] == search_id:
            print(colored("\nStudent Found:", "green"))
            print(colored(f"Name: {student['name']}", "cyan"))
            print(colored(f"Age: {student['age']}", "cyan"))
            print(colored(f"ID: {student['id']}", "cyan"))
            print(colored(f"Grade: {student['grade']}", "cyan"))
            return
    print(colored("\nStudent not found!", "red"))

# Function to update student information
def update_student_by_id():
    update_id = input(colored("\nEnter Student ID to update: ", "yellow"))
    for student in data_list:
        if student["id"] == update_id:
            print(colored("\nEnter new details (leave blank to keep the same value):", "blue"))
            new_name = input(colored("New Name: ", "cyan"))
            new_age = input(colored("New Age: ", "cyan"))
            new_grade = input(colored("New Grade: ", "cyan"))

            if new_name:
                student["name"] = new_name
            if new_age:
                student["age"] = int(new_age)
            if new_grade:
                student["grade"] = new_grade

            print(colored("\nStudent updated successfully!", "green"))
            return
    print(colored("\nStudent not found!", "red"))

# Function to delete a student by ID
def delete_student_by_id():
    delete_id = input(colored("\nEnter Student ID to delete: ", "yellow"))
    for i, student in enumerate(data_list):
        if student["id"] == delete_id:
            del data_list[i]
            print(colored("\nStudent deleted successfully!", "green"))
            return
    print(colored("\nStudent not found!", "red"))

# Main loop
while True:
    # menuSystem()  # Display menu
    try:
        operationType = int(input(colored("\nEnter your choice: ", "green")))

        if operationType == 1:
            add_students()
        elif operationType == 2:
            display_students()
        elif operationType == 3:
            search_student_by_id()
        elif operationType == 4:
            update_student_by_id()
        elif operationType == 5:
            delete_student_by_id()
        elif operationType == 6:
            print(colored("\nExiting the program. Goodbye! 👋", "yellow"))
            break
        else:
            print(colored("Invalid input! Please enter a number between 1 and 6.", "red"))

    except ValueError:
        print(colored("Invalid input! Please enter a valid number.", "red"))

