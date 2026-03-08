class Calculator:
    @staticmethod
    def sum(a: float, b: float, c: float | None = None) -> float:
        print(f"{a} + {b}", end='')
        total = a + b
        if c != None:
            print(f" + {c}", end='')
            total += c
        print(f" = {total}")
        return total
    
    def sub(a: float, b: float, c: float | None = None) -> float:
        print(f"{a} - {b}", end='')
        total = a - b
        if c != None:
            print(f" - {c}", end='')
            total -= c
        print(f" = {total}")
        return total
    
    def multiply(a: float, b: float, c: float | None = None) -> float:
        print(f"{a} * {b}", end='')
        total = a * b
        if c != None:
            print(f" * {c}", end='')
            total *= c
        print(f" = {total}")
        return total

class Calc:
    @staticmethod
    def sum(*args) -> float:
        total = 0
        for i, arg in enumerate(args):
            if i == 0:
                print(f"{arg}", end='')
            else:
                print(f" + {arg}", end='')
            total += arg
        print(f" = {total}")
        return total


Calculator.sum(1, 2)
Calculator.sub(3, 2)
Calculator.multiply(2, 3, 2)

Calc.sum(1, 4, 5, 3)
Calc.sum(3, 6, 9, 12)