#Kristen Norman
#ENTD200 D005 Fall 2021
#Jason Black
#Week 6
#10Jan2021

decision = int(0) #Used to repeat or exit the WHILE Loop

while (decision != int(3)): #Overall Program Loop.
    #\n used to make the program more appealing.
    print("\n"*25, """

                --------Welcome to Gas Usage Calculator!--------
                _                                           _     
                _                Main Menu                  _
                _                                           _
                _        1. Miles Per Gallon (MPG)          _
                _        2. Kilometers Per Liter (Km/l)     _
                _        3. Exit Program                    _
                _                                           _
                _
                _____________________________________________""","\n"*5)

    decision = input("Please enter a number to make your selection: ")

    while decision != int(1) or decision != int(2) or decision != int(3):
        if type(decision) != int:
            try:
                decision = int(decision)
            except:
                pass
        else:
            pass
        if decision == int(1) or decision == int(2) or decision == int(3):
            break
        else:
            print("\n","You need to enter a valid integer to proceed...","\n"*1)
            decision = input("Please enter an integer/whole number to make your selection: ")

    if decision == int(1): #Start of MPG Loop
        repeater = "y" #Variable used to repeat the Program
        while repeater == "y": #Loop to repeat MPG Loop
            vehicle = input("What is your vehicle?: ") #Vehicle of User
            milesDriven = input("Please enter how many miles you drove: ") #Miles Driven

            while type(milesDriven) != int: #Error Correction
                if type(milesDriven) != int:
                    try:
                        milesDriven = int(milesDriven)
                    except:
                        pass
                else:
                    pass
                if type(milesDriven) == int:
                    break
                else:
                    print("You need to enter an integer to proceed...","\n"*3)
                    milesDriven = input("Please enter your miles driven: ")

            gallonsUsed = input("Please enter the gallons of gas you used: ") #Gallons of Gas Used

            while type(gallonsUsed) != int: #Error Correction
                if type(gallonsUsed) != int:
                    try:
                        gallonsUsed = int(gallonsUsed)
                    except:
                        pass
                else:
                    pass
                if type(gallonsUsed) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n"*1)
                    gallonsUsed = input("Please enter your gallons of gas used: ")
            MPG = milesDriven / gallonsUsed
            print("In your",vehicle,"you drove",milesDriven,"miles using",gallonsUsed,"gallons of gas and your Miles Per Gallon is", MPG,"\n")
            repeater = input("Would you like to repeat the program? (y/n): ")
# End of Miles Per Gallon Loop

    if decision == int(2): #Start of Km/l Loop
        repeater = "y" #Variable used to repeat the Program
        while repeater == "y": #Loop to repeat Km/l Loop
            vehicle = input("What is your vehicle?: ") #Vehicle of User
            kilometersDriven = input("Please enter how many kilometers you drove: ") #Kilometers Driven

            while type(kilometersDriven) != int: #Error Correction
                if type(kilometersDriven) != int:
                    try:
                        kilometersDriven = int(kilometersDriven)
                    except:
                        pass
                else:
                    pass
                if type(kilometersDriven) == int:
                    break
                else:
                    print("You need to enter an integer to proceed...","\n"*3)
                    kilometersDriven = input("Please enter your miles driven: ")

            litersUsed = input("Please enter the liters of gas you used: ") #Liters of Gas Used

            while type(litersUsed) != int: #Error Correction
                if type(litersUsed) != int:
                    try:
                        litersUsed = int(litersUsed)
                    except:
                        pass
                else:
                    pass
                if type(litersUsed) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n"*1)
                    gallonsUsed = input("Please enter your liters of gas used: ")
            KmL = kilometersDriven / litersUsed
            print("In your",vehicle,"you drove",kilometersDriven,"kilometers using",litersUsed,"liters of gas and your Kilometers per Liter is", KmL,"\n")
            repeater = input("Would you like to repeat the program? (y/n): ")
# End of Kilometers per Liter Loop

    if decision == int(3): #To Properly Exit Program
        print("\n")
        print("Thanks for using the program! Hit Enter to Close it!")
        print("\n")
        input() #Creates a pause before closing the program.
        exit() #Exits the Program
