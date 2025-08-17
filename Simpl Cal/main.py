# Simple Calculator

print("Welcome to Calculator")
 
Operations = ["+","-","*","/"]

userExist = True

while userExist :

    userInputOperation = input("Chosse Operation for Calculation or Type 'exist' to End Programm : (+ - * /) => ")

    if userInputOperation.lower() == "exist":
        print("Your Existed from the Calculator, have great day :) ")
        userExist = False
    else:

        if userInputOperation in Operations:

            userInputNumbers_1 = float(input("Take any first Numbers.."))
            userInputNumbers_2 = float(input("Take the second Number.."))

            if userInputOperation == "+":
                print("The Output For Addition is :",userInputNumbers_1 + userInputNumbers_2)
            elif userInputOperation == "-":
                print("The Output for Subtraction is :",userInputNumbers_1 - userInputNumbers_2)
            elif userInputOperation == "*":
                print("The OutPut for Multiplication is :",userInputNumbers_1 * userInputNumbers_2)
            elif userInputOperation == "/":
                if userInputNumbers_2 == 0:
                    print("Zero Division Error")
                else:
                    print("The Output for Divison is :",userInputNumbers_1 / userInputNumbers_2)
        else:
            print("Enter the Operations Given in Prompt..")

        WantToContinue = input("Do You want to Continue, Y/N ? ")

        if WantToContinue.lower() != "y":
            print("Your Existed from the Calculator, have great day :) ")
            userExist = False
        else:
            print("I am Ready for Next Operation...")





