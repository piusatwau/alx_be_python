class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __str__(self):
        return f"The new student is {self.first_name} {self.last_name}, is {self.age} old"
    
student1 = Student("Atwau", "Pius", 27)
print(student1)