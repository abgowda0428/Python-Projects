# Student Management System Using Python

import uuid

keys = ["Name", "Age", "Grade", "Subjects"]

Students_Details = {}

def add_Student():

    U_Id = str(uuid.uuid4())[:4]
    user_details = {}

    for key in keys:
        value = input(f"Enter Student {key} : ")
        user_details[key] = value
    
    Students_Details[U_Id] = user_details

def StuDetail():
    Flag = True
    Studet = input("Enter the Student Id .")
    print(Studet)
    for keys,valOftu in Students_Details.items():
        if Studet == keys:
            Flag = False
            print(f"Here the Student Details...\n 1.Student Name: {valOftu["Name"]} .\n 2.Student Age: {valOftu["Age"]} . \n 3.Student Grade: {valOftu["Grade"]} .\n 4.Studnet Subjects: {valOftu["Subjects"]} ")
    if Flag :
        print("No Student Found in this ID ....")

def ViewStuDetail():
    for keys,val in Students_Details.items():
        print(f"Student ID: {keys}")
        print("Lables:", list(val.keys()))
        print("Data:", list(val.values()))

def updateStu():
    userChoice = input("Enter the ID of Student, Which you Need to Update: ")
    if userChoice in Students_Details.keys():
        print(f"For {userChoice}, What You want to Update?")
        print("Available fields:", list(Students_Details[userChoice].keys()))
        field = input("Enter the field to update (e.g., age, grade, major): ")
        if field in Students_Details[userChoice]:
            new_value = input(f"Enter new value for {field}: ")
            Students_Details[userChoice][field] = new_value
            print(f"Updated {field} for {userChoice} to {new_value}")
            print("Updated details:", Students_Details[userChoice])
        else:
            print(f"Field {field} does not exist for {userChoice}")
    else:
        print(f"Student ID {userChoice} not found")

def deleteStu():
    userChoice = input("Enter the ID of Student to Delete: ")
    if userChoice in Students_Details.keys():
        deleted_student = Students_Details.pop(userChoice)
        print(f"Deleted {userChoice} with details: {deleted_student}")
        print("Updated Students_Details:", Students_Details)
    else:
        print(f"Student ID {userChoice} not found")

running = True

while running:  
    print("\n=== Welcome to Student Management System ===")
    print("1: Add Student Detail")
    print("2: Search Student Details")
    print("3: Delete Student")
    print("4: Update Student Details")
    print("5: View All Students")
    print("Type 'exit' to quit.")

    userInput = input("\nEnter your choice (1 – 5 or 'exit'): ").strip().lower()

    if userInput == "exit":
        print("Closing the application... Thanks for visiting! 😊")
        running = False
    elif userInput == "1":
        add_Student()
    elif userInput == "2":
        StuDetail()
    elif userInput == "3":
        deleteStu()
    elif userInput == "4":
        updateStu()
    elif userInput == "5":
        ViewStuDetail()
    else:
        print("⚠️ Invalid input, please enter 1 – 5 or 'exit'.")
