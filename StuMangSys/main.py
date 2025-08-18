# 📌 Project Suggestion: Student Management System (Console App)

# This will be a menu-driven Python app where you can manage students’ details.

# ✅ Concepts it will cover:

# Variables & Data Types → storing student info

# Input & Output → menu & user input

# Operators → ID generation, simple checks

# Conditional Statements → menu options (if/elif/else)

# Loops → repeat menu until exit

# Functions → separate tasks (add_student(), remove_student(), etc.)

# Dictionary → store student records ({id: {name, age, grade}})

# List & Tuple → subjects list, immutable student IDs

# Set → keep track of unique course names

# List Comprehension → filtering students (e.g., [s for s in students if s['grade'] > 80])

# File Handling → save & load student data in a text/CSV file

# Exception Handling → handle wrong input

# 🔹 Features:

# Add Student → ask name, age, grade, subjects

# View Students → display all student details

# Search Student → by ID or name

# Update Student → modify grade or subjects

# Delete Student

# List High Performers → using list comprehension

# Save Data → write to file (so it stays after program ends) (Pending)

# Load Data → read file on startup (Pending)

'''***********************************************************************************************************************'''

import uuid

keys = ["Name", "Age", "Grade", "Subjects"]
Students_Details = {}
unique_courses = set()

def add_Student():
    U_Id = str(uuid.uuid4())[:4]
    user_details = {}
    
    for key in keys:
        while True:
            try:
                value = input(f"Enter Student {key}: ").strip()
                if not value:
                    print(f"Error: {key} cannot be empty.")
                    continue
                if key == "Age":
                    value = int(value)
                    if value <= 0:
                        print("Error: Age must be a positive number.")
                        continue
                elif key == "Grade":
                    value = int(value)
                    if value < 0 or value > 100:
                        print("Error: Grade must be between 0 and 100.")
                        continue
                elif key == "Subjects":
                    value = [s.strip() for s in value.split(",") if s.strip()]  # Convert to list
                    if not value:
                        print("Error: At least one subject is required.")
                        continue
                    unique_courses.update(value)  # Add to unique courses set
                user_details[key] = value
                break
            except ValueError:
                print(f"Error: Invalid input for {key}. Please enter a valid {'integer' if key in ['Age', 'Grade'] else 'value'}.")
    
    Students_Details[U_Id] = user_details
    print(f"Student added with ID: {U_Id}")

def StuDetail():
    if not Students_Details:
        print("Error: No students found in the database.")
        return
    
    Student = input("Enter the Student ID: ").strip()
    if not Student:
        print("Error: Student ID cannot be empty.")
        return
    
    if Student in Students_Details:
        valOftu = Students_Details[Student]
        print(f"Here are the Student Details...\n"
              f"1. Student Name: {valOftu['Name']}.\n"
              f"2. Student Age: {valOftu['Age']}.\n"
              f"3. Student Grade: {valOftu['Grade']}.\n"
              f"4. Student Subjects: {', '.join(valOftu['Subjects'])}.")
    else:
        print("No Student Found with this ID.")

def ViewStuDetail():
    if not Students_Details:
        print("Error: No students found in the database.")
        return
    
    for keys, val in Students_Details.items():
        print(f"Student ID: {keys}")
        print("Labels:", list(val.keys()))
        print("Data:", [val['Name'], val['Age'], val['Grade'], ', '.join(val['Subjects'])])

def updateStu():
    if not Students_Details:
        print("Error: No students found in the database.")
        return
    
    userChoice = input("Enter the ID of Student to Update: ").strip()
    if not userChoice:
        print("Error: Student ID cannot be empty.")
        return
    
    if userChoice in Students_Details:
        print(f"For {userChoice}, What do you want to Update?")
        print("Available fields:", list(Students_Details[userChoice].keys()))
        field = input("Enter the field to update (e.g., Name, Age, Grade, Subjects): ").strip()
        if not field:
            print("Error: Field cannot be empty.")
            return
        if field in Students_Details[userChoice]:
            try:
                new_value = input(f"Enter new value for {field}: ").strip()
                if not new_value:
                    print(f"Error: New value for {field} cannot be empty.")
                    return
                if field == "Age":
                    new_value = int(new_value)
                    if new_value <= 0:
                        print("Error: Age must be a positive number.")
                        return
                elif field == "Grade":
                    new_value = int(new_value)
                    if new_value < 0 or new_value > 100:
                        print("Error: Grade must be between 0 and 100.")
                        return
                elif field == "Subjects":
                    new_value = [s.strip() for s in new_value.split(",") if s.strip()]
                    if not new_value:
                        print("Error: At least one subject is required.")
                        return
                    unique_courses.update(new_value)  # Update unique courses
                Students_Details[userChoice][field] = new_value
                print(f"Updated {field} for {userChoice} to {new_value}")
                print("Updated details:", Students_Details[userChoice])
            except ValueError:
                print(f"Error: Invalid input for {field}. Please enter a valid {'integer' if field in ['Age', 'Grade'] else 'value'}.")
        else:
            print(f"Field {field} does not exist for {userChoice}")
    else:
        print(f"Student ID {userChoice} not found")

def deleteStu():
    if not Students_Details:
        print("Error: No students found in the database.")
        return
    
    userChoice = input("Enter the ID of Student to Delete: ").strip()
    if not userChoice:
        print("Error: Student ID cannot be empty.")
        return
    
    if userChoice in Students_Details:
        deleted_student = Students_Details.pop(userChoice)
        # Optionally refresh unique_courses (if needed, can recompute from all students)
        print(f"Deleted {userChoice} with details: {deleted_student}")
        print("Updated Students_Details:", Students_Details)
    else:
        print(f"Student ID {userChoice} not found")

def viewUniqueCourses():
    if not unique_courses:
        print("No courses registered yet.")
        return
    print("Unique Courses:", ", ".join(sorted(unique_courses)))

def filterStudents():
    if not Students_Details:
        print("Error: No students found in the database.")
        return
    
    try:
        threshold = int(input("Enter the minimum grade to filter (0-100): "))
        if threshold < 0 or threshold > 100:
            print("Error: Grade threshold must be between 0 and 100.")
            return
        
        filtered = [s for s in Students_Details.items() if s[1]['Grade'] > threshold]
        if not filtered:
            print(f"No students found with Grade > {threshold}.")
            return
        
        print(f"\nStudents with Grade > {threshold}:")
        for student_id, details in filtered:
            print(f"Student ID: {student_id}")
            print(f"Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}, Subjects: {', '.join(details['Subjects'])}")
    except ValueError:
        print("Error: Please enter a valid integer for the grade threshold.")

running = True
while running:
    try:
        print("\n=== Welcome to Student Management System ===")
        print("1: Add Student Detail")
        print("2: Search Student Details")
        print("3: Delete Student")
        print("4: Update Student Details")
        print("5: View All Students")
        print("6: View Unique Courses")
        print("7: Filter Students by Grade")
        print("Type 'exit' to quit.")
        
        userInput = input("\nEnter your choice (1 – 7 or 'exit'): ").strip().lower()
        
        if userInput == "exit":
            print("Closing the application... Thanks for visiting! 😊")
            running = False
        elif userInput in ["1", "2", "3", "4", "5", "6", "7"]:
            if userInput == "1":
                add_Student()
            elif userInput == "2":
                StuDetail()
            elif userInput == "3":
                deleteStu()
            elif userInput == "4":
                updateStu()
            elif userInput == "5":
                ViewStuDetail()
            elif userInput == "6":
                viewUniqueCourses()
            elif userInput == "7":
                filterStudents()
        else:
            print("⚠️ Invalid input, please enter 1 – 7 or 'exit'.")
    except KeyboardInterrupt:
        print("\nOperation interrupted. Closing the application...")
        running = False
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")