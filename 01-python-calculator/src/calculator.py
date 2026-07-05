print("=== PYTHON CALCULATOR ===")


# Input Handling --> without program crashes
# ------------------------------------------
def get_number(num_prompt):
    while True: 
        try: 
            return float(input(num_prompt))
        except ValueError: 
            #handles ValueError if user input fails to get converted to float --> preventing program crash. 
            print("Input invalid. Please enter a number.")

# Math Operations 
# ---------------
def add(a, b):
    """
    float, float --> float
    Takes two numbers and returns the sum as a float. 
    """
    return a + b

def subtract(a, b): 
    """
    float, float --> float
    Takes two numbers and returns the difference as a float. 
    """
    return a - b

def multiply(a, b): 
    """
    float, float --> float
    Takes two numbers and returns the product as a float. 
    """
    return a * b

def divide(a, b): 
    """
    float, float --> float
    Takes two numbers and returns the quotient. 
    """
    if b == 0: 
        return "Error: cannot divide by zero"
    return a / b

# Main Program Loop
# -----------------
while True: 
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5': 
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid option. Try again.")
        continue

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    #if num1.replace(".", "").isdigit() and num2.replace(".", "").isdigit():
        #num1 = float(num1)
        #num2 = float(num2)
    #else:
        #print("Invalid input. Please enter numbers only.")
        #exit()


    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")