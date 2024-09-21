#using a for loop to generate a multiplication table

number = int(input("Enter a number to see its multiplication table: "))

for Y in range(1, 11):
    print(f"{number} * {Y} = {number*Y}")
