print("=== PYTHON CALCULATOR ===")
print("Starting program...")

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

while True: 
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice (1-5): "))

    if choice == 5: 
        print("Goodbye!")
        break

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if num1.replace(".", "").isdigit() and num2.replace(".", "").isdigit():
        num1 = float(num1)
        num2 = float(num2)
    else:
        print("Invalid input. Please enter numbers only.")
        exit()


    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")