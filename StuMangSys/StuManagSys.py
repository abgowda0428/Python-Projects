# Student Management System Using Python

import uuid

keys = ["Name", "Age", "Grade", "Subjects"]

Students_Details = {}

def add_Student():

    U_Id = str(uuid.uuid4())[:0]
    user_details = {}

    for key in keys:
        value = input(f"Enter Student {key} : ")
        user_details[key] = value
    
    Students_Details[U_Id] = user_details

def StartApplications():

    print("Welcome to Student Management System..")
    print("Select the Below Options to Proceed with the Application.")
    print("Enter 1: ADD Student Detail.")
    print("Enter 2: For Search Student Details.")
    print("Enter 3: To Delete the Student.")
    print("Enter 4: For Update the Student Details.")
    print("Enter 5: For View all Students Details.")
    print("Enter 'Exit' to Close the Application.")