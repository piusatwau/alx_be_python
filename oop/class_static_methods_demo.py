class Calculator:
    # Class attribute
    calculator_type = "Arithmetic Operations"
    
    def __repr__(self):
        # Returning a string representation of the object
        return f"calculation_type: {self.calculator_type}"
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b
    
    # Class method to multiply two numbers and print the class attribute
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculator_type}")
        return a * b
