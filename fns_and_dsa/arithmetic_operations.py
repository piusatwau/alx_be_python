
'''
Define a function named perform_operation.
Parameters: num1 (float), num2 (float), and operation (string). 
The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
The function should execute the arithmetic operation based on the operation parameter and the numerical values provided.
For division, include handling for division by zero, returning a specific message or value that your main.py script can recognize and display appropriately.
Return the result of the arithmetic operation

'''
'''

num1 = float(input("Please enter first number: "))
num2 = float(input("Please enter second number: "))

print("use: ")
print("1. add works as +")
print("2. subtract works as -")
print("3. divide works as /")
print("4. multiply works as *")

operation = input("Please enter the operation you would like to perform on the numbers ('add', 'subtract', 'multiply', or 'divide'): ").lower()

def perform_operation(num1, num2, operation):
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

'''

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform an arithmetic operation on two numbers based on the operation parameter.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float or str: The result of the operation, or an error message for division by zero.
    """
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        result = num1 / num2
    elif operation == "multiply":
        result = num1 * num2
    else:
        return "Error: Invalid operation"
    
    return result


# User Input
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

print("Operations available: 'add', 'subtract', 'multiply', 'divide'")
operation = input("Please enter the operation: ").lower()

# Perform the operation and print the result
result = perform_operation(num1, num2, operation)

if isinstance(result, str):
    print(result)  # This prints error messages
else:
    print(f"The result of {operation} is: {result}")

    
    