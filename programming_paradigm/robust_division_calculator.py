def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator/denominator
    except ZeroDivisionError as e:
        return f"Error: Cannot divide by zero."
        
    except ValueError as e:
        print(e)
        
safe_divide(4, 5)
        
    