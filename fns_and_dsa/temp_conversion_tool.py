# Global conversion factors (EXACTLY as required)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # NO extra spaces, NO parentheses, exact 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").upper()
        
        if unit == 'F':
            print(f"{temp}°F = {convert_to_celsius(temp)}°C")
        elif unit == 'C':
            print(f"{temp}°C = {convert_to_fahrenheit(temp)}°F")
        else:
            print("Error: Please enter 'C' or 'F'.")
    except ValueError:
        print("Error: Temperature must be a number.")

if __name__ == "__main__":
    main()