#Kristen Norman
#ENTD200 D005 Fall 2021
#Jason Black
#Week 6
#10Jan2021

decision = int(0) #Used to repeat or exit the WHILE Loop

while (decision != int(5)): #Overall Program Loop.
    #\n used to make the program more appealing.
    print("\n"*25, """

                --------Welcome to Python Calculator!--------
                _                                           _     
                _                Main Menu                  _
                _                                           _
                _        1. Addition (X+Y=Z)                _
                _        2. Subtraction (X-Y=Z)             _
                _        3. Multiplication (X*Y=Z)          _
                _        4. Division (X/Y=Z)                _
                _        5. Exit Program                    _
                _                                           _
                _    *Depending on your choice, you will    _
                _    input two(2) numbers and the chosen    _
                _    operator will be applied to them.      _
                _____________________________________________""","\n"*5)

    decision = input("Please enter a number to make your selection: ")

    while decision != int(1) or decision != int(2) or decision != int(3) or decision != int(4) or decision != int(5): #Error Correction for invalid entries.
        if type(decision) != int:
            try:
                decision = int(decision)
            except:
                pass
        else:
            pass
        if decision == int(1) or decision == int(2) or decision == int(3) or decision == int(4) or decision == int(5):
            break
        else:
            print("\n","You need to enter a valid integer to proceed...","\n"*1)
            decision = input("Please enter an integer/whole number to make your selection: ")
    if decision == int(1): #Start of Addition Loop
        addition = "y" #Variable used to repeat the program
        while addition == "y": #Loop to repeat Addition Loop
            name = input("What is your name?: ") #Name of User
            number1 = input("Please enter your first number: ") #Fist Number

            while type(number1) != int: #Error Correction
                if type(number1) != int:
                    try:
                        number1 = int(number1)
                    except:
                        pass
                else:
                    pass
                if type(number1) == int:
                    break
                else:
                    print("You need to enter an integer to proceed...","\n"*3)
                    number1 = input("Please enter your first number: ")

            number2 = input("Please enter your second number: ") #Second Number

            while type(number2) != int: #Error Correction
                if type(number2) != int:
                    try:
                        number2 = int(number2)
                    except:
                        pass
                else:
                    pass
                if type(number2) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n"*1)
                    number2 = input("Please enter your second number: ")
            total = number1 + number2
            print(name, number1, "+", number2, "equals", total)
            addition = input("Would you like to repeat the program? (y/n): ")
# End of Addition Loop

    if decision == int(2): #Start of Subtraction Loop
        subtraction = "y" #Variable to repeat Subtraction Loop
        while subtraction == "y": #Loop to repeat Subtraction Loop
            name = input("What is your name?: ") #Name of User
            number1 = input("Please enter your first number: ") #First Number

            while type(number1) != int: #Error Correction Loop
                if type(number1) != int:
                    try:
                        number1 = int(number1)
                    except:
                        pass
                else:
                    pass
                if type(number1) == int:
                    break
                else:
                    print("You need to enter an integer to proceed...","\n"*3)
                    number1 = input("Please enter your first number: ")

            number2 = input("Please enter your second number: ") #Second Number

            while type(number2) != int: #Error Correction Loop
                if type(number2) != int:
                    try:
                        number2 = int(number2)
                    except:
                        pass
                else:
                    pass
                if type(number2) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n"*1)
                    number2 = input("Please enter your second number: ")
            total = number1 - number2
            print(name, number1, "-", number2, "equals", total)
            subtraction = input("Would you like to repeat the program? (y/n): ")
#End of Subtraction Loop

    if decision == int(3): #Start of Multiplication Loop
        multiplication = "y" #Variable to repeat Multiplaction Loop
        while multiplication == "y": #Loop to repeat Multiplication Loop
            name = input("What is your name?: ") #Name of User
            number1 = input("Please enter your first number: ") #First Number

            while type(number1) != int: #Error Correction
                if type(number1) != int:
                    try:
                        number1 = int(number1)
                    except:
                        pass
                else:
                    pass
                if type(number1) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n"*1)
                    number1 = input("Please enter your first number: ")

            number2 = input("Please enter your second number: ") #Second Number

            while type(number2) != int: #Error Correction
                if type(number2) != int:
                    try:
                        number2 = int(number2)
                    except:
                        pass
                else:
                    pass
                if type(number2) == int:
                    break
                else:
                    print("You need to enter an integer to proceed...","\n"*3)
                    number2 = input("Please enter your second number: ")
            total = number1 * number2
            print(name, number1, "x", number2, "equals", total)
            multiplication = input("Would you like to repeat the program? (y/n): ")
# End of Multiplication Loop

    if decision == int(4): #Start of Division Loop
        division = "y" #Variable to repeat Division Loop
        while division == "y": #Loop to repeat Division Loop
            name = input("What is your name?: ") #Name of User
            number1 = input("Please enter your first number: ") #First Number

            while type(number1) != int: #Error Correction
                if type(number1) != int:
                    try:
                        number1 = int(number1)
                    except:
                        pass
                else:
                    pass
                if type(number1) == int:
                    break
                else:
                    print("You need to enter an integer to proceed...","\n"*3)
                    number1 = input("Please enter your first number: ")

            number2 = input("Please enter your second number: ") #Second Number

            while type(number2) != int: #Error Correction
                if type(number2) != int:
                    try:
                        number2 = int(number2)
                    except:
                        pass
                else:
                    pass
                if type(number2) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n"*1)
                    number2 = input("Please enter your second number: ")
            total = number1 / number2
            print(name, number1, "/", number2, "equals", total)
            division = input("Would you like to repeat the program? (y/n): ")
#End of Division Loop
    if decision == int(5): #To Properly Exit Program
        print("\n")
        print("Thanks for using the program! Hit Enter to Close it!")
        print("\n")
        input() #Creates a pause before closing the program.
        exit() #Exits the Program

