# multiplication_table.py

# Ask the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to print the multiplication table for the given number
for i in range(1, 11):  # Loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")
