def daily_reminder():
    # Step 1: Prompt for Task Description
    task = input("Enter your task: ")
    
    # Step 2: Prompt for Task Priority
    priority = input("Priority (high/medium/low): ").lower()
    
    # Step 3: Ask if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Step 4: Use Match Case to process task based on priority
    match priority:
        case "high":
            priority_message = "high priority task"
        case "medium":
            priority_message = "medium priority task"
        case "low":
            priority_message = "low priority task"
        case _:
            priority_message = "unknown priority task"
    
    # Step 5: Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder_message = f"'{task}' is a {priority_message} that requires immediate attention today!"
    else:
        reminder_message = f"Note: '{task}' is a {priority_message}. Consider completing it when you have free time."
    
    # Step 6: Print the reminder message
    print(f"Reminder: '{task}' is a {priority} priority task that {'requires immediate attention today!' if time_bound == 'yes' else 'Consider completing it when you have free time.'}")


# Call the function to run the script
daily_reminder()
