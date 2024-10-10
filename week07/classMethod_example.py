# CLASS METHOD

class Dog:
    breed = "bull dog"
    
    def __init__(self, name):
        self.name = name
        
   #Class methods are a great way to modify shared class attributes
    @classmethod
    def change_breed(cls, new_breed):
        cls.breed = new_breed
        
    def show_info(self):
        print(f"{self.name} is a {self.breed}")
        
    # static methods are a great way to write methods that are specific to a given class
    # for example a given classs may be having a formular to calculate something
    # This is where static methods come in    
    @staticmethod
    def fareneheight(celsius):
        return celsius*(5/9)+32
        
dog1 = Dog("Buddy")
dog1.show_info()
print(dog1.fareneheight(35))