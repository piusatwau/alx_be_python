#using datetime module in python to display date, day and time


import datetime

# getting current time

current_time = datetime.datetime.now().time()
print(f"The time is {current_time}")

#getting current date

current_date = datetime.datetime.today().date()
print(f"Today is {current_date}")

#getting current year

current_year = datetime.datetime.today().year
print(f"The year is {current_year}")

# time in utc
utc_time = datetime.datetime.now(datetime.UTC)
print(f"The time in UTC is {utc_time}")

