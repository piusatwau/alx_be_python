# temperature conversion tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
degree_symbol = chr(176) # unicode for degree symbol

temperature = int(input("Enter the temperature to convert: "))
validate = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
def convert_to_celsius(fahrenheit):
    return (temperature - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
convert_to_celsius(temperature)
    
    
def convert_to_fahrenheit(celsius):
    return (temperature + 32)*CELSIUS_TO_FAHRENHEIT_FACTOR
convert_to_fahrenheit(temperature)

if validate == "C":
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}{degree_symbol}C is {result}{degree_symbol}F")
elif validate == "F":
    result = convert_to_celsius(temperature)
    print(f"{temperature}{degree_symbol}F is {result}{degree_symbol}C")
else:
    print("Please enter a valid temperature and unit")

    