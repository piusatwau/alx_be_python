# match case for simple mathematical calcutions

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

case = input("Choose the operation (+, -, *, /): ")

match case:
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
        if num2 == 0:
            print("Cannot dvide by 0")
        else:
            result = num1/num2
            print(f"The result is {result}")