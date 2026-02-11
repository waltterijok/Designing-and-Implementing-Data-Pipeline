class Calculator:

    def __init__(self):
        pass

    # Lisää parametrit yhteen ja palauttaa tuloksen
    def add(self, num1, num2):
        return num1 + num2

    # miinustaa 1. paramterin 2. parametristä ja palauttaa tuloksen
    def subtract(self, num1, num2):
        return num1 - num2

    # kertoo parametrit keskenään ja palauttaa tuloksen
    def multiply(self, num1, num2):
        return num1 * num2

    # jakaa 1. parametrin 2. parametrillä (paitsi jos parametri on 0, palauttaa errorin)
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"