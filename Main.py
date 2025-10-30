'''
Author: Luke Low
Title: Fence Cost calculator
Date: 31/10/25
Version 1.0
'''

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

    width = ask("width")
    length = ask("length")

    perimeter = 2*width + 2*length
    print(f"The perimeter is {perimeter} meters.")

    cost = ask("cost per meter")
    print(f"The total cost will be ${perimeter * cost}.")

    keep_going = input("\nWould you like to do another calculation? If yes, press <enter>, if no, press any other key. ")