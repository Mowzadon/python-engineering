toolbox = ["Hammer", "Wrench", "Screwdriver"]

remove_tool = input("Enter a tool to remove: ")

if remove_tool in toolbox: 
    toolbox.remove(remove_tool)

else:
    print("Tool not found")

print(toolbox)
print(len(toolbox))

count = 0
for tool in toolbox:
    print(count, "-", tool)
    count += 1