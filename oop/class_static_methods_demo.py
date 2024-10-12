class Calculator:
    calculator_type = "Arithmetics Operations"
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def multiply(cls, a, b):
        print(f"calculation_type", "Arithmetic Operations")
        return a * b
    