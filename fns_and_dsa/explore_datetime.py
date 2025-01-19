from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Print the current date and time in the desired format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user for a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Calculate the future date by adding the days to the current date
    future_date = datetime.now() + timedelta(days=days_to_add)

    # Print the future date in the desired format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Display current date and time
    display_current_datetime()

    # Calculate and display future date
    calculate_future_date()

if __name__ == "__main__":
    main()

