# variable scope in python
# LEGB

information = "Welcome to 2026 Uganda general elections!"
first_name = input("What is your first name?: ")

def greetings():
    age = int(input("How old are you?: "))
    
    if age>18:
        print(f"Good morning {first_name}, you are eligible to vote")
    else:
        print(f"Good morning {first_name}, you are still young to vote")

print(information)
greetings()
    
    