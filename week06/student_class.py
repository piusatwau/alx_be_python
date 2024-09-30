# Exercise 1: 

# Creating a Student Class

# Instructions:

# Define a Student class with attributes like name and age. Include a method to display student information.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_student_info(self):
        return f"Name: {self.name}\n Age: {self.age}"
student1 = Student("Pius", 27)

print(student1.display_student_info())