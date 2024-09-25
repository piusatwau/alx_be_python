import math

angle = int(input("please enter the angle you wish to calculate sine for: "))

def sine(angle):
    return math.sin(angle)
print(f"The sine of {angle} is {sine(angle)}")
sine(angle)