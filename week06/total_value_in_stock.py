# Exercise 2: 
# Creating a Product Catalog

# Instruction:
# Define a Product class with attributes like name, price, and quantity. Implement a method to calculate the total value of products in stock.

class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_value(self):
        return self.price*self.quantity
rice = product("supa", 2000, 240)  
print(f"The total value of {rice.name} is ${rice.total_value()}")
