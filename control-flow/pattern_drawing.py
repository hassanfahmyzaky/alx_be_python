# pattern_drawing.py

# Ask the user to input a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 1

# Use a while loop to create the rows
while row <= size:
    # Inside the while loop, use a for loop to print the asterisks
    for col in range(size):
        print("*", end="")  # end="" ensures it prints on the same line
    # Print a newline character after each row
    print()
    # Increment the row counter
    row += 1
