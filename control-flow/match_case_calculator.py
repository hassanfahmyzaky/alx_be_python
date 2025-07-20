# match_case_calculator.py

# Prompt the user for the first number
num1 = float(input("Enter the first number: "))

# Prompt the user for the second number
num2 = float(input("Enter the second number: "))

# Ask for the operation to be performed
operation = input("Choose the operation (+, -, *, /): ")

# Perform the operation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")
