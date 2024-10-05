def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return f"The result of the division is {numerator/denominator}"
        
    except ZeroDivisionError as e:
        return f"Error: Cannot divide by zero."
        
    except ValueError as e:
        return f"Error: Please enter numeric values only."
        
safe_divide(4, 5)
        
    