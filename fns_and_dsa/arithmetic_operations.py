
'''
Define a function named perform_operation.
Parameters: num1 (float), num2 (float), and operation (string). 
The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
Return the result of the arithmetic operation

'''


num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))

print("use: ")
print("1. add works as +")
print("2. subtract works as -")
print("3. divide works as /")
print("4. multiply works as *")

operation = input("Please enter the operation you would like to perform on the numbers ('add', 'subtract', 'multiply', or 'divide'): ").lower()

def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case "add":
            result = num1+num2
            print(f"Result: {result}")
        case "subtract":
            result = num1-num2
            print(f"Result: {result}")
        case "divide":
            if num2 == 0:
                print("Error, you can't divide by 0, enter a number greater than 0")
            else:
                result = num1/num2
                print(f"Result: {result}")
        case "multiply":
            result = num1*num2
            print(f"Result: {result}")
        case _:
            print(f"Enter valid numbers and operator")
perform_operation(num1, num2, operation)

    
    