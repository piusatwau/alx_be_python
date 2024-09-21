# pattern drawing using loops

size = int(input("Enter the size of the pattern: "))

count = 1

while count <= size:
    width = size*"*"
    for n in width:
        print(f"*", end="")
    print()
    count += 1
    
    