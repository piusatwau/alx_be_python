# drawing equilateral triangle

'''
Define the height of the pyramid (number of rows) as a variable, for example: rows = 5.
Use nested while loops to achieve the following:
The outer loop will control the number of rows.
The inner loop will print spaces and then asterisks in each row, creating a triangular shape.
Remember to adjust the number of spaces and asterisks printed within the inner loop based on the current row number to form the pyramid.


'''


rows = 5 # this initializes the number of rows which acts asthe height of the traingle
row_counter = 1
while row_counter <= rows:
    spaces = rows-row_counter
    while spaces >0:
        print(" ", end="")
        spaces -= 1
        
    astericks = 2*row_counter-1
    while astericks >0:
        print("*", end="")
        astericks -= 1
    print()
    row_counter += 1

    
'''   
# Step 1: Define the height of the pyramid
rows = 5

# Step 2: Initialize the row counter
i = 1

# Step 3: Outer loop to iterate through the rows
while i <= rows:
    # Step 4: Inner loop to print spaces
    spaces = rows - i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1

    # Step 5: Inner loop to print asterisks
    stars = 2 * i - 1
    while stars > 0:
        print("*", end="")
        stars -= 1

    # Step 6: Move to the next line
    print()

    # Step 7: Increment row counter
    i += 1
'''