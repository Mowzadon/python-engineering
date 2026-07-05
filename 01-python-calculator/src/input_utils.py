# Input Handling --> without program crashes
# ------------------------------------------
def get_number(num_prompt):
    while True: 
        try: 
            return float(input(num_prompt))
        except ValueError: 
            #handles ValueError if user input fails to get converted to float --> preventing program crash. 
            print("Input invalid. Please enter a number.")
            