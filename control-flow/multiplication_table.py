# Step 1: Ask the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Use a for loop to generate the multiplication table
for i in range(1, 11):  # This will loop through numbers 1 to 10
    result = number * i  # Multiply the input number by the loop index
    print(f"{number} * {i} = {result}")  # Print the result in the desired format
