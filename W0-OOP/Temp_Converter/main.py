# imports TemperatureConvertor from temperature_converter.py
from temperature_converter import TemperatureConverter
converter = TemperatureConverter()

print("Program starting.")
print("Initializing temperature converter...")
print("Temperature converter initialized.")


while True:
    print("\nOptions:")
    print("1. Set temperature")
    print("2. Convert to Celsius")
    print("3. Convert to fahrenheit")
    print("4. Convert to kelvin")
    print("0. Exit program")
    choice = int(input("Choice: "))

    if choice == 1:
        temperature = float(input("Enter temperature: "))
        converter.setTemperature(temperature)               #sends 'temperature' to the object for handling
        print(f"Temperature set to {temperature}")
    elif choice == 2:
        in_celsius = converter.toCelsius()
        print(f"Temperature in celsius: {in_celsius}")
    elif choice == 3:
        in_fahrenheit = converter.toFahrenheit()
        print(f"Temperature in fahrenheit: {in_fahrenheit}")
    elif choice == 4:
        in_kelvin = converter.toKelvin()
        print(f"Temperature in kelvin: {in_kelvin}")
    elif choice == 0:
        print("Program ending.")
        break
    else:
        print("Please insert choice between 1 and 4")
