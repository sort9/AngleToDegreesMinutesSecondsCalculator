# Program to convert angle to degrees, minutes, seconds form 

def main():
    
    # Take angle input from user
    angleAfterDecimal = float(input("What is the angle that you would like to convert? (I.e. 0.4423 for 82.4423°)"))
    
    # Conversion calculations for minutes
    minutes = angleAfterDecimal * 60
    print("Minutes" + minutes)
    print(" ")
    
    # Take minute input from user
    minutesAfterDecimal = float(input("How many minutes would you like to convert? (I.e. 0.569 for 67.569)"))
    
    # Conversion calculations for seconds
    secondsCalc = minutesAfterDecimal * 60
    print("Seconds: " + secondsCalc)
    
main()
