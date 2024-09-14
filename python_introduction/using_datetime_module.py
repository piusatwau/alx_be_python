import datetime

# Get the current year
current_year = datetime.date.today().year
print(f"Today is {current_year}")

# Define the target year and calculate the age difference
target_year = int(input(print("Now enter the future year for which you want to know how old you will be: ")))
current_age = int(input(print("How old are you now? ")))
age_difference = target_year - current_year
future_age = age_difference + current_age
print(f"In {target_year}, you will be {future_age} year(s) old")

#... (rest of the code remains the same)