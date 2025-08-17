import uuid

# Predefined keys for user data
keys = ["name", "age", "city"]

# Master dictionary to store all user data
master_dict = {}

def add_user_data():
    # Generate a unique ID
    user_id = str(uuid.uuid4())[0:8]  # Shortened UUID for simplicity
    user_data = {}
    
    print(f"\nNew User (ID: {user_id})")
    print("Please enter the following details:")
    
    # Collect user inputs for each key
    for key in keys:
        value = input(f"Enter {key}: ")
        user_data[key] = value  # To store the Value in the Dict with Pre-Defined Keys in the List form.
    
    # Store user data in master dictionary with unique ID
    master_dict[user_id] = user_data
    print(f"\nUser data stored: {user_data}")
    print(f"Current master dictionary: {master_dict}")

def main():
    while True:
        print("\nMenu:")
        print("1. Add user details")
        print("2. View all data")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            add_user_data()
        elif choice == "2":
            print("\nAll stored data:", master_dict)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


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

# Save Data → write to file (so it stays after program ends)

# Load Data → read file on startup