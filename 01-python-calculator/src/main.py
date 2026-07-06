from operations import add, subtract, multiply, divide
from input_utils import get_number

# Main Program Loop
# -----------------

def main():
    history = []
    while True:
        print("\n=== CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("6. Show history")

        choice = input("Choose (1-6): ")

        if choice == "5":
            print("Goodbye!")
            break
            # break stops the program from running.

        

        if choice not in ["1", "2", "3", "4", "6"]:
            print("Invalid option")
            continue
    
        if choice == "6":
            print(history)
            continue
            # continue makes the program jump back to the start of the loop, if the condition is satisfied.   


        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            print("Result:", result)
            history.append(result)
        elif choice == "2":
            result = subtract(num1, num2)
            print("Result:", result)
            history.append(result)
        elif choice == "3":
            result = multiply(num1, num2)
            print("Result:", result)
            history.append(result)
        elif choice == "4":
            result = divide(num1, num2)
            print("Result:", result)
            history.append(result)
        
        
            

#“run this code only if this file is the one being executed directly, not imported.”
if __name__ == "__main__":
    main()