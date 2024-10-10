class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def drive(self):
        print(f"The {self.model} is driving")

class Tyre:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    def __str__(self):
        return f"Tyre(brand={self.brand}, size={self.size})"


class Engine:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.horsepower = horsepower
    def __str__(self):
        return f"Engine(brand={self.brand}, horsepower={self.horsepower})"

class ElectricEngine:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.horsepower = horsepower
    def __str__(self):
        return f"ElectricEngine(brand={self.brand}, horsepower={self.horsepower})"

    def start(self):
        print(f"The {self.brand} engine is starting")


class Mercedes:
    def __init__(self, Engine, ElectricEngine, Tyre):
        self.Engine = Engine
        self.ElectricEngine = ElectricEngine
        self.Tyre = Tyre

    def __str__(self):
        return f"Mercedes(Engine={self.Engine}, ElectricEngine={self.ElectricEngine}, Tyre={self.Tyre})"
    
mercedesGClass = Mercedes({self.Engine("Mercedes", 100)}, {self.ElectricEngine("Mercedes", 100)}, {self.Tyre("Mercedes", 100)})

print(mercedesGClass)
