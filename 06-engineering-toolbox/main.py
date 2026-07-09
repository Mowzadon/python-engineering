from tool import Tool #import Tool class from tool.py

#initialize starting inventory objects
hammer = Tool("Hammer", 3, "Good", "Shelf A")
drill = Tool("Drill", 1, "Fair", "Workshop")
wrench = Tool("Wrench", 5, "Excellent", "Drawer 2")

inventory = [hammer, drill, wrench]

def add_tool():
    """
    (none) --> (none)
    Add a new tool to the inventory.
    """
    name = input("Enter the name of the tool: ")
    quantity = int(input("Enter the quantity of the tool: "))
    condition = input("Enter the condition of the tool: ")
    location = input("Enter the location of the tool: ")

    new_tool = Tool(name, quantity, condition, location)
    inventory.append(new_tool)
    print(f"{name} has been added to the inventory.")

#main program loop
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

        #View inventory option
        if option == "1":
            for tool in inventory: 
                tool.display()
                print()
                continue 
        
        #Add tool option
        if option == "2":
            add_tool()
            continue
            
        #Exit program loop option
        if option == "6":
            print("Goodbye!")
            break




if __name__ == "__main__":
    main()



