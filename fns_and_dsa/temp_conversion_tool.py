# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit}°F")
        elif unit == 'F':
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius}°C")
        else:
            print("Invalid input. Please enter 'C' or 'F' for temperature unit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

