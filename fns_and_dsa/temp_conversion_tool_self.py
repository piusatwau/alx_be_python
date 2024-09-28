# temperature conversion tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input("Enter the temperature to convert: "))
validate = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
def convert_to_celsius(fahrenheit):
    fahrenheit = temperature*FAHRENHEIT_TO_CELSIUS_FACTOR
convert_to_celsius(temperature)
    
    
def convert_to_fahrenheit(celsius):
    celsius = temperature*CELSIUS_TO_FAHRENHEIT_FACTOR
convert_to_fahrenheit(temperature)

if validate == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature} is {result}")
elif validate == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature} is {result}")
else:
    print("Please enter a valid temperature and unit")

    