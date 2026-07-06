#Toolbox
toolbox = {
    "Hammer": 3,
    "Wrench": 5,
    "Screwdriver": 2
}

def display_inventory():
    print("Current Toolbox:")

    for tool in toolbox:
        print(tool, toolbox[tool])
    

while True:

#Gather user input to remove a tool.
    remove_tool = input("Enter a tool to remove: \nType \"View\" to view inventory. \nType \"Exit\" to exit the program. ")
    #Capitalize the user input
    remove_tool = remove_tool.title()

    #Exit program
    if remove_tool == "Exit":
        break

    if remove_tool == "View": 
        display_inventory()
        continue


    if remove_tool in toolbox: 
        #If tool is in toolbox, decrease its count by 1.
        toolbox[remove_tool] -= 1
        #If the number of any tool == 0, that tool will be removed from the toolbox.
        if toolbox[remove_tool] == 0: 
            del toolbox[remove_tool]
        
    else: 
        print("Tool not found")

    #Loop through each tool in the toolbox and print them all. 
    display_inventory()