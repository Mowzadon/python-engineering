from tool import Tool #import Tool class from tool.py

#initialize starting inventory objects
hammer = Tool("Hammer", 3, "Good", "Shelf A")
drill = Tool("Drill", 1, "Fair", "Workshop")
wrench = Tool("Wrench", 5, "Poor", "Drawer 2")

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

def remove_tool(tool): #remove a tool from inventory list, if it exists.
    """
    Remove an object of the class Tool freom the list
    """   
    inventory.remove(tool)
    print(f"{tool.name} has been removed from the inventory.")

def find_tool(tool_name): #find a tool in the existing inventory, return it if it exits, otherwise return None. 
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

def tool_not_found(): #prints a message to the user when a tool is not found. 
    """
    Display a message when a requested tool cannot be found.
    """
    print("Tool not found.") #you can't have a print statement as a return value, because it will return None

def show_stats():
    """
    Display summary of statistics about the current inventory.
    """
    unique_tools = len(inventory)

    total_quantity = 0
    tools_needing_repair = 0

    for tool in inventory: 
        total_quantity += tool.quantity

        if tool.condition != "Good":
            tools_needing_repair += 1
    print("\n===== Inventory Statistics =====\n")
    print(f"Unique tools: {unique_tools}")
    print(f"Total quantity: {total_quantity}")
    print(f"Tools needing repair: {tools_needing_repair}")



#main program loop
def main():
    """
    Args:
    (none) --> (none)

    Main Program loop
    """
    
    while True: 
    #User Menu
        print("\n============================\nEngineering Toolbox\n============================")
        print()
        print("1. View Inventory")
        print("2. Add Tool")
        print("3. Use Tool")
        print("4. Repair Tool")
        print("5. Move Tool")
        print("6. Remove Tool")
        print("7. Inventory Statistics")
        print("8. Exit")

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
                tool_not_found()
        
        #Repair tool option
        elif option == "4":
            tool_name = input("Which tool would you like to repair? ")

            tool = find_tool(tool_name)

            if tool is not None:
                tool.repair()
                print(f"{tool.name} has been repaired.")
            else:
                tool_not_found()

        #Move tool option
        elif option == "5":
            tool_name = input("Which tool would you like to move? ")

            tool = find_tool(tool_name)

            if tool is not None: 
                new_location = input("Enter the tool's new location: ")
                tool.move(new_location)
                print(f"{tool.name} has been moved to {tool.location}.")
            else:
                tool_not_found()


        #Remove tool option
        elif option == "6": 
            tool_name = input("Which tool would you like to remove? ")

            tool = find_tool(tool_name)

            if tool is not None: 
                remove_tool(tool)

            else: 
                tool_not_found()

        #Display inventory statistics option
        elif option == "7":
            show_stats()
        


        #Exit program loop option
        elif option == "8":
            print("Goodbye!")
            break

        else: 
            print("Invalid option. Please choose 1-7.")




if __name__ == "__main__":
    main()



