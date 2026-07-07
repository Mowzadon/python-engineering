class Tool:

    def __init__(self, name, quantity, condition, location):
        self.name = name
        self.quantity = quantity
        self.condition = condition
        self.location = location

    def use(self): #quantity method for the class Tool
        self.quantity -= 1
        #notice there is no return line for a method linked to a class, since this method updates a class's attribute.
        #methods are for class, functions are a seperate idea with a return value.

    def repair(self):
        self.condition = "Good"

    def move(self, new_location):
        self.location = new_location
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Condition: {self.condition}")
        print(f"Location: {self.location}")

hammer = Tool(
    "Hammer", 
    3,
    "Bad",
    "Shelf A"
) #hammer object of the class Tool

drill = Tool("Drill", 1, "Fair", "Worksshop")

hammer.display()

hammer.use()
print(hammer.quantity)

hammer.repair()
print(hammer.condition)

hammer.move("workshop")
print(hammer.location)

drill.repair()
drill.move("Shelf A")
drill.display()
