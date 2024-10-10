# a good understanding of polymorphism in Python, where the base class Shape has a method area(), 
# and the derived classes Rectangle and Circle override this method to provide specific implementations 
# for their respective shapes.


import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):        
        return math.pi*self.radius** 2
    