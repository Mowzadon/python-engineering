class Tool: 
    """
    Class of objects refered to as 'Tool'.
    Represents a tool in the engineering toolbox.

    Each Tool object stores information about a single tool,
    including its name, quantity, condition, and location.
    """

    def __init__(self, name, quantity, condition, location):
        """
        Initialize a new Tool object.

        Args:
            name (str): Name of the tool.
            quantity (int): Number of tools available.
            condition (str): Current condition of the tool.
            location (str): Storage location of the tool.
        """
        self.name = name
        self.condition = condition 
        self.quantity = quantity
        self.location = location
        
    def use(self):
        """
        Decrease the available quantity of the tool by one.
        """
    
    def repair(self): 
        """
        Restore the tool's condition to 'Good'.
        """
        self.condition = "Good"
    
    def move(self, new_location):
        """
        Move the tool to a new storage location.

        Args:
            new_location (str): The new location for the tool.
        """
        self.location = new_location
    
    def display(self):
        """
        Display the tool's information.
        """
        print(f"\nTool: {self.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Condition: {self.condition}")
        print(f"Location: {self.location}")
                