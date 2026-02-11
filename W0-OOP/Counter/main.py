# Imports Counter from counter.py
from counter import Counter 
counter = Counter()

print("Program starting.")
print("Initializing counter...")
print("Counter initialized")

while True:
    print("\n -- Counter menu --")
    print("1. Add count")
    print("2. Get count")
    print("3. Zero count")
    print("0. Exit program")
    choice = int(input("Choice: "))

    if choice == 1:
        counter.addCount()      # runs the addCount object from counter.py
        print("Count increased")
    
    elif choice == 2:
        current_count = counter.getCount()      # pulls the current count with getCount from counter.py
        print(f"Current count '{current_count}'")
    
    elif choice == 3:
        counter.zeroCount()         # resets the count with zeroCount from counter.py
        print("Count zeroed")
    
    elif choice == 0:
        print("Program ending")
        break
    
    else:
        print("Insert a proper choice")