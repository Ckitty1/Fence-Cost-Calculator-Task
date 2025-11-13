'''
Author: Luke Low
Title: Fence Cost calculator
Date: 14/11/25
Version 1.1
'''

# Function for asking for an input. Eg. width, length, cost
# Checks for number errors
def ask(dimension):
    error = "That is not a valid number. Please enter a number more than zero next time."

    while True:
        try:
            response = float(input(f"Please enter the {dimension}: "))
            
            if response > 0:
                break

            else: 
                print(error)
            
        except ValueError:
            print(error)

    return(response)

# MAIN PROGRAM

print("\nWelcome to my fence cost calculator !!\n")

keep_going = ""
    
while keep_going == "":

    # Asks for width and length
    width = ask("width")
    length = ask("length")

    # Calculates perimeter
    perimeter = 2*width + 2*length
    print(f"The perimeter is {perimeter} meters.")

    # Asks for cost per meter
    cost = ask("cost per meter")

    # Outputs the cost per meter in a normal sentence
    print(f"The total cost will be ${perimeter * cost}.")

    keep_going = input("\nWould you like to do another calculation? If yes, press <enter>, if no, press any other key. ")