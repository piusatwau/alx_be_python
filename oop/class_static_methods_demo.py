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
        print(f"Calculation Type: {cls.calculator_type}")
        return a * b
    
solution1 = Calculator.add(45, 6)
solution2 = Calculator.multiply(24, 4)
print(solution1)
print(solution2)