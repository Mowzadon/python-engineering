class Tool: 
    
    def __init__(self, name, quantity, condition, location): #initialize the class tool
        self.name = name
        self.quantity = quantity
        self.condition = condition
        self.location = location

    def display(self): #display object and its attributes
        print(f"\nTool: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Condition: {self.condition}")
        print(f"Location: {self.location}")

    
    def use(self): #decrease quantity of tool
        self.quantity -=1
    
    def repair(self): #changes tool quantity to good
        self.condition = "Good"
    
    def move(self, new_location): #change tool's location
        self.location = new_location


hammer = Tool("Hammer", 3, "Good", "Shelf A")
drill = Tool("Drill", 1, "Fair", "Workshop")
wrench = Tool("Wrench", 5, "Excellent", "Drawer 2")



toolbox = [hammer, drill, wrench] #toolbox storing Tool objects

name = input("Tool name: ")
quantity = int(input("Quantity: "))
condition = input("Condition: ")
location = input("Location: ")

new_tool = Tool(name, quantity, condition, location)

toolbox.append(new_tool)

for tool in toolbox:
    tool.display()

