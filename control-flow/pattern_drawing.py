# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop for the rows
while row < size:
    # Use a for loop for the columns
    for _ in range(size):
        print("*", end="")  # Print '*' without going to a new line
    print()  # Move to the next line after printing all the stars for the current row
    row += 1  # Increment the row counter
