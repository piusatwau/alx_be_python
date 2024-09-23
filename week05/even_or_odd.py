# function that checks if a number is even or odd

print("I am a simple computer that allows you to check if a number is even or odd")
number = int(input("Please enter the number you would like to check: "))

def even_or_odd_checker(number):
    if number%2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
        
even_or_odd_checker(number)