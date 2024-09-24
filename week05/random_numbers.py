#generating random numbers and storing them in a set
#the numbers must be 10, and unique

import random

random_numbers = set()

while len(random_numbers) < 10:
    random_numbers.add(random.randint(1, 10))
    
print(random_numbers)

#LEARNING
#if you just write a simple function with an incorporated for loop, the code will run 10 times and puts those 
# values into the set. but remember sets store only unique values, meaning any repeatedly generated number will be removed
# at the end you will remain with a set with less than 10 values
# best to use a for loop with len function

# below is the inefficient code example

import random

# Generate 10 random numbers between 1 and 10 and store them in a set
random_numbers = {random.randint(1, 10) for _ in range(10)}
print(random_numbers)
 
