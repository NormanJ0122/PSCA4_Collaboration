#Kristen Norman
#ENTD200 D005 Fall 2021
#Jason Black
#Week 6
#10Jan2021

decision = int(0) #Used to repeat or exit the WHILE Loop

while (decision != int(3)): #Overall Program Loop.
    #\n used to make the program more appealing.
    print("\n"*25, """

                --------Welcome to PayRoll Calculator!--------
                -                                                                     
                -                          Main Menu
                -                 1. Calculate Payroll
                -                 2. Exit Program
                ------------------------------------------------
""","\n"*5)

    decision = input("Please enter a number to make your selection: ")

    while decision != int(1) or decision != int(2):
        if type(decision) != int:
            try:
                decision = int(decision)
            except:
                pass
        else:
            pass
        if decision == int(1) or decision == int(2):
            break
        else:
            print("\n","You need to enter a valid integer to proceed...","\n"*1)
            decision = input("Please enter an integer/whole number to make your selection: ")

    if decision == int(1): #Start of Payroll Calculation
        repeater = "y" #Variable used to repeat the Program
        while repeater == "y": #Loop to repeat Payroll Calculation
            print("\n"*3,"Welcome to Payroll Calculator!","\n"*2)
            name = input("Enter the name of the Employee:  ")
            print("\n"*2)
            hourlyRate = input("Enter their hourly wage:  ")
            while type(hourlyRate) != int: #Error Correction
                if type(hourlyRate) != int:
                    try:
                        hourlyRate = int(hourlyRate)
                    except:
                        pass
                else:
                    pass
                if type(hourlyRate) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n")
                    hourlyRate = input("Please enter their hourly rate as an integer: ")
            print("\n"*2)
            hoursWorked = input("Enter their hours worked:  ")
            while type(hoursWorked) != int: #Error Correction
                if type(hoursWorked) != int:
                    try:
                        hoursWorked = int(hoursWorked)
                    except:
                        pass
                else:
                    pass
                if type(hoursWorked) == int:
                    break
                else:
                    print("\n","You need to enter an integer to proceed...","\n"*1)
                    hoursWorked = input("Please enter your hours worked as an integer: ")
            totalPay = (hourlyRate * hoursWorked)
            print("\n"*2)
            print("For employee", name)
            print("Their hourly rate is:", hourlyRate)
            print("They worked", hoursWorked, "hours.")
            print("Their total pay is:", totalPay)
            repeater = input("Would you like to repeat the program? (y/n): ")
#End of Payroll Calculation Loop

    if decision == int(2): #To Properly Exit Program
        print("\n")
        print("Thanks for using the program! Hit Enter to Close it!")
        print("\n")
        input() #Creates a pause before closing the program.
        exit() #Exits the Program
