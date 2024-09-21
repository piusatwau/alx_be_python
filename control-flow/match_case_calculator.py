# match case for simple mathematical calcutions

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        result = num1+num2
        print(f"The result is {result}")
        
    case "*":
        result = num1*num2
        print(f"The result is {result}")
        
    case "-":
        result = num1-num2
        print(f"The result is {result}")
        
    case "/":
        result = num1/num2
        if num1<=0:
            print("Zero (0) cannot be a divider, chose a number greater zero.")
        else:
            print(f"The result is {result}")