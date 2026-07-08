from tool import Tool #import Tool class from tool.py

#initialize starting inventory objects
hammer = Tool("Hammer", 3, "Good", "Shelf A")
drill = Tool("Drill", 1, "Fair", "Workshop")
wrench = Tool("Wrench", 5, "Excellent", "Drawer 2")

inventory = [hammer, drill, wrench]

def main():
    """
    (none) --> (none)
    Main Program loop
    """
    
    while True: 
    #User Menu
        print("============================\nEngineering Toolbox\n============================")
        print()
        print("1. View Inventory")
        print("2. Add Tool")
        print("3. Use Tool")
        print("4. Repair Tool")
        print("5. Move Tool")
        print("6. Exit")
        print()

        option = input("Choose an option: ")

        if option == "1":
            for tool in inventory: 
                tool.display()
                continue 

        if option == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


