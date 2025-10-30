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