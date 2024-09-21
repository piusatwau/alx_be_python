#using a for loop to generate a multiplication table

number = int(input("Enter a number to see its multiplication table: "))

for y in range(1, 11):
    z = y*number
    print(f"{number} * {y} = {z}")
