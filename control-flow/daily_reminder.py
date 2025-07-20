# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to react based on task priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Modify the reminder based on time-bound status
if time_bound == "yes":
    reminder += " That requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the final reminder
print(f"Reminder: {reminder}")
