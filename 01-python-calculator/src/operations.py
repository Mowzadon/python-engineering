# Math Operations 
# ---------------
def add(a, b):
    """
    float, float --> float
    Takes two numbers and returns the sum as a float. 
    """
    return a + b

def subtract(a, b): 
    """
    float, float --> float
    Takes two numbers and returns the difference as a float. 
    """
    return a - b

def multiply(a, b): 
    """
    float, float --> float
    Takes two numbers and returns the product as a float. 
    """
    return a * b

def divide(a, b): 
    """
    float, float --> float
    Takes two numbers and returns the quotient. 
    """
    if b == 0: 
        return "Error: cannot divide by zero"
    return a / b
