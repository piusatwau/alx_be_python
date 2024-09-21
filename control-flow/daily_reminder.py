#daily reminder

'''
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "no":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")

'''

# Daily Reminder Script

# Prompt user for task description
task = input("Enter your task: ")

# Prompt user for task priority
priority = input("Priority (high/medium/low): ").lower()  # Convert input to lowercase for uniformity

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level entered."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Output the final customized reminder
print(reminder)
