from tool import Tool #import Tool class from tool.py

#initialize starting inventory objects
hammer = Tool("Hammer", 3, "Good", "Shelf A")
drill = Tool("Drill", 1, "Fair", "Workshop")
wrench = Tool("Wrench", 5, "Excellent", "Drawer 2")

inventory = [hammer, drill, wrench]


def add_tool(): #add new tool to inventory
    """
    Args:
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

def find_tool(tool_name): #find a tool in the existing inventory, if it exists. 
    """
    Search the inventory for a tool by name.

    Args:
        tool_name (str): The name of the tool to search for.

    Returns:
        Tool (obj)/None: The matching Tool object if found,
        otherwise None.
    """
    for tool in inventory:
        if tool.name.lower() == tool_name.lower():
            return tool

    return None


#main program loop
def main():
    """
    Args:
    (none) --> (none)

    Main Program loop
    """
    
    while True: 
    #User Menu
        print()
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
                
        #Add tool option
        elif option == "2": #use elif after the first if statement to avoid running all the if statements.
            add_tool()
            continue

        #Use tool option
        elif option == "3":
            tool_name = input("Which tool would you like to use? ")

            tool = find_tool(tool_name)

            if tool is not None:
                if tool.use():
                    print(f"{tool.name} has been used.")
                    print(f"Remaining quantity: {tool.quantity}")
                else:
                    print(f"{tool.name} is out of stock.")
            else:
                print("Tool not found.")
        
        #Repair tool option
        elif option == "4":
            tool_name = input("Which tool would you like to repair? ")

            tool = find_tool(tool_name)

            if tool is not None:
                tool.repair()
                print(f"{tool.name} has been repaired.")
            else:
                print("Tool not found.")

        #Move tool option
        elif option == "5":
            tool_name = input("Which yool would you like to move? ")

            tool = find_tool(tool_name)

            if tool is not None: 
                new_location = input("Enter the tool's new location: ")
                tool.move(new_location)
                print(f"{tool.name} has been moved to {tool.location}.")
            else:
                print("Tool not found")


        #Exit program loop option
        elif option == "6":
            print("Goodbye!")
            break

        else: 
            print("Invalid option. Please choose 1-6.")




if __name__ == "__main__":
    main()



