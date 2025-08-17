# Quize App

print(">>>>>>>>>>>>>>>>(: Welcome to Quize App :)<<<<<<<<<<<<<<<<<<<<")

print("******************************************************************")

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is immutable in Python?": "tuple",
    "Which symbol is used for comments in Python?": "#",
    "What is the output of 2 ** 3 in Python?": "8",
    "Which keyword is used to exit a loop in Python?": "break"
}
print("You want to Play Quize or Want to gain Knowledge ??..")
userInput = input("Press: 1 for Quize Press: 2 for Referece. ")

if userInput == "1":

    def QuizeApp():

        totalMarks = 0

        for q,a in questions.items():
            answer = input(f"{q} ")
            if answer == a :
                totalMarks += 1
        
        if totalMarks == 5:
            print("Your Brillent")
        elif totalMarks <= 3:
            print("You Need Work Hard..")
        else:
            print("Better Luck Next Time Buddy....")

    again = True    


    while again:
        QuizeApp()
        WantToContinue = input("Do Want Try Again ??(Y/N) ")
        if WantToContinue == "N":
            again = False
            print("Thanks For Giving Try....")
        else:
            print("Lets Countinue Buddy..Think again and try....")
else:
    ref = questions.items()
    for val in ref:
        print(f"Questions: {val[0]}, Answers: {val[1]} .")
        
