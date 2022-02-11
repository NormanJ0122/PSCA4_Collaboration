#Kristen Norman
#ENTD200 D005 Fall 2021
#Jason Black
#Week 4
#27Dec2021

decision = int(0) #Variable for User to make decisions within the Program.

while (decision != int(4)): #Overall Program Loop. Program returns here unless user wants to Exit.
    #\n*20 keeps the screen clean between selections.
    print("\n"*20, """
             Main Menu:
1. Display Creator Information
2. Payroll Calculator
3. Miles Per Gallon Calculator
4. Exit Program

Type numerical response and hit 'Enter' below to confirm decision.""")

    decision = int(input()) #User telling program which nested loop, or option, to execute.
    if (decision == int(1)): #Displays creator's information.
        print("\n"*20, """
Creator: Kristen Norman
Course: ENTD200 D005 Fall 2021
Instructor: Jason Black
Section of Course: Week 4
Date Created: 27Dec2021

Press 'Enter' to return to Main Menu""")
        input() #Used to pause before returning to Main Menu.

    if (decision == int(2)): #Payroll Calculator Sub-Program.
        print("Welcome to Payroll Calculator!")
        name = str(input("Enter name of Employee:  "))
        hourlyRate = float(input("Enter your hourly wage:  "))
        hoursWorked = float(input("Enter your hours worked in a month:  "))
        monthlyPay = (hourlyRate * hoursWorked)
        print("\n"*20)
        print("For employee", name)
        print("Your hours rate is:", hourlyRate)
        print("You worked", hoursWorked, "hours.")
        print("Your total pay for the month is:", monthlyPay)
        print("Press 'Enter' to return to Main Menu")
        input() #Used to pause before returning to Main Menu.


    if (decision == int(3)): #Mile Per Gallon Calculator Sub-Program
        print("Welcome to Miles Per Gallon Calculator!")
        vehicle = str(input("What vehicle are you driving?:  "))
        milesDriven = float(input("How many miles did you drive?:  "))
        gallonsUsed = float(input("How many gallons of gas did you use?:  "))
        milesPerGallon = (milesDriven / gallonsUsed)
        print("\n"*20)
        print("For your", vehicle)
        print("You drove", milesDriven, "miles.")
        print("You used", gallonsUsed, "gallons.")
        print("Your Miles Per Gallon (MPG) for this trip was:", milesPerGallon)
        print("Press 'Enter' to return to Main Menu")
        input() #Used to pause before returning to Main Menu.

    if (decision != int(4)): #Returns user to Main Menu if selection does not equal 4.
        continue
else:
    print("End of Program! \nPress Enter")
    exit() #Auto-prompts the user to kill the program properly.
