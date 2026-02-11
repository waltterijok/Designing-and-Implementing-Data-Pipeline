# Imports Counter from counter.py
from coin_acceptor import CoinAcceptor
acceptor = CoinAcceptor()

print("Program starting.")

while True:
    print("1. Insert coin")
    print("2. Show coins")
    print("3. Return coins")
    print("0. Exit program")
    choice = int(input("Choice: "))

    if choice == 1:
        acceptor.insertCoin()      # runs the insertCoin object from coin_acceptor.py
        print("Coin inserted")
   
    elif choice == 2:
        current_count = acceptor.getAmount()      # pulls the current amount with getAmount from coin_acceptor.py
        print(f"Currently '{current_count}' coins in coin acceptor")
    
    elif choice == 3:
        returned_coins = acceptor.returnCoins()
        print(f"Coin acceptor returned '{returned_coins}' coins.")
    
    elif choice == 0:
        print("Program ending")
        break
    
    else:
        print("Insert a proper choice")