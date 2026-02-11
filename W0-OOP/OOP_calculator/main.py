from calculator import Calculator
calculator = Calculator()

print("Welcome to Calculator Program\n")

while True:
    print("--- Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")
    
    try:
        choice = int(input("Choice: "))
        
        if choice == 0:
            print("Program ending.")
            break

        elif choice == 1:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
            
        elif choice == 2:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
            
        elif choice == 3:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
            
        elif choice == 4:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        
        else:
            print("Invalid choice!")
            
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")