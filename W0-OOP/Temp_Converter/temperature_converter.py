class TemperatureConverter:

    # sets default value at 0.0 / asettaa oletusarvoksi 0.0
    def __init__(self):
        self.temperature = 0.0

    # receives the input from main and stores it / ottaa vastaan main-tiedoston input arvon
    def setTemperature(self, value):
        self.temperature = value

    # returns the celsius value given / palauttaa annetun celsius arvon
    def toCelsius(self):
        return self.temperature

    # calculates and returns the converted value
    def toFahrenheit(self):
        return self.temperature * 9/5 + 32

    # calculates and returns the calculated value
    def toKelvin(self):
        return self.temperature + 273.15