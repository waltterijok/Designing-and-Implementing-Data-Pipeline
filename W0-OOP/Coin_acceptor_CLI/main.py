# Imports Counter from counter.py
from coin_acceptor import CoinAcceptor
acceptor = CoinAcceptor()

print("Program starting.")
print("Welcome to coin acceptor program")

while True:
    try:
        choice = float(input("Insert new coin by typing it's value (0 returns the money, -1 exits the program): "))

        if choice == -1:
            print("Exiting program...")
            print("Program ending.")
        
        elif choice == 0:
            print("Returning coins...")
            coin_count, total_value = acceptor.returnCoins()                # uses returnCoins from coin_acceptor.py and stores the values into coin_count and total_value
            print(f"{coin_count} coins with {total_value}€ value returned")
        
        elif choice > 0:
            print("Inserting...")
            acceptor.insertCoin(choice)
            print(f"Inserted coins = {acceptor.getCoinCount()}, value = {acceptor.getAmount()}")
        
        else:
            print("Invalid coin value.")

    except ValueError:
        print("Invalid input! Please enter a number.")