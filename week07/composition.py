# In Python, composition is a concept in object-oriented programming where one class is composed of one 
# or more objects from other classes. It is used to model a "has-a" relationship, meaning that a class 
# can have objects of other classes as part of its attributes. This allows for the reuse of code and promotes 
# modular design by breaking down complex systems into smaller, manageable pieces.


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.color = color
        self.year = year
        
    def __str__(self):
        return f"This is {self.model}, made in {self.year}. You can get it in {self.color}"
    
class Tyre:
    def __init__(self, size, cost):
        self.size = size
        self.cost = cost
    def __str__(self):
        return f"tyre size {self.size} costs ${self.cost}"
    
class Mercedes:
    def __init__(self, car, tyre):
        self.tyre = tyre
        self.car = car
    def __str__(self):
        return f"{self.car}, and the {self.tyre}"
    

my_car = Car("Mercedes G-Class", 2022, "Black")
my_tyre = Tyre(10, 200)
Mercedes1 = Mercedes(my_car, my_tyre)

print(Mercedes1.__str__())
    