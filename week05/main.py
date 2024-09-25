# importing functions from a given module
# in this case, I create a simple arithmetic module called calculator.py that contains 
# simple arithmetic operations

import calculator

sum = calculator.add(5, 3)

difference = calculator.subtract(5, 3)

product = calculator.multiply(5, 3)

divident = calculator.divide(5, 3)

print(sum, difference, product, divident)