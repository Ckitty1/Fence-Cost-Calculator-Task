'''
Author: Luke Low
Title: Fence Cost calculator
Date: 14/11/25
Version 1.1
'''

# Function for asking for an input. Eg. width, length, cost
# Checks for number errors
def ask(dimension):
    # Error message
    error = "That is not a valid number. Please enter a number more than zero next time."

    while True:
        try:
            # Asks for input
            response = float(input(f"Please enter the {dimension}: "))
            
            if response > 0:
                break

            else: 
                print(error)
            
        # Checks for error
        except ValueError:
            print(error)

    return(response)

# MAIN PROGRAM

print("\nWelcome to my fence cost calculator !!\n")

keep_going = ""

# Loops code
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

    # Asks whether wants to repeat program or not
    keep_going = input("\nWould you like to do another calculation? If yes, press <enter>, if no, press any other key. ")