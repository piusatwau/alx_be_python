from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # this gets the current date and time and formats it to YYY-MM-DD HH:MM:SS
    print(f"Current date and time: {current_date}")
display_current_datetime()

def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days = number_of_days)
    future_date.strftime
    print(f"Future date: {future_date}")
calculate_future_date()
