print("Welcome to our Fahrenheit/Celsius Conversion Program!")
measure = str(input("Do you measure degrees in Celsius or Fahrenheit? (C/F):  "))
temperature = int(input("What temperature is it?:  "))
if (measure != 'C'):
    total = ((temperature - 32) *5/9)
    print("Your converted temperature is:  ", total)
else:
    total = float(((temperature*1.8)+32), 1)
    print("Your converted temperature is:  ", total)
input("Press enter to close program.")
