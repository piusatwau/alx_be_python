import math

angle = int(input("Please enter the angle you wish to calculate tangent for: "))

def tangent(angle):
    return math.tan(angle)
print(f"The tangent of {angle} is {tangent(angle)}")
tangent(angle)