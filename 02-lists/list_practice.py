#practicing lists
toolbox = ["Hammer", "Wrench", "Screwdriver"]

print(toolbox)
#will print the ENTIRE list object - including brackets
print(toolbox[0])

toolbox.append("Pliers")
print(toolbox)

new_tool = input("Enter a new tool: ")
toolbox.append(new_tool)

for tool in toolbox: 
    print(tool)
