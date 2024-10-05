def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError as e:
        return f"Error: Cannot divide by zero."
        
    except ValueError as e:
        return f"Error: Please enter numeric values only."
        
safe_divide(4, 5)
        
    