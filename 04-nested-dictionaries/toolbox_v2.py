toolbox = {
    "Hammer": {
        "quantity": 3,
        "condition": "Good",
        "location": "Shelf A",
        "Available": True

    },

    "Wrench": {
        "quantity": 5,
        "condition": "Fair",
        "location": "Drawer 2",
        "Available": True

    },

    "Screwdriver": {
        "quantity": 2,
        "condition": "Excellent",
        "location": "Shelf B",
        "Available": True

    },

    "Drill": {
        "quantity": 1,
        "condition": "Poor",
        "location": "Workshop",
        "Available": True
    }
}


for tool, attributes in toolbox.items(): #tool is the first key, attribute is the nested dictionary
    print(tool)
    print("Quantity:", attributes["quantity"])
    print("Condition:", attributes["condition"])
    print("Location:", attributes["location"])
    print("Available", attributes["Available"])
    print() #prints empty line

print("Tools needing attention:\n")

for tool, attributes in toolbox.items():
    if attributes["condition"] == "Poor":
        print(tool)