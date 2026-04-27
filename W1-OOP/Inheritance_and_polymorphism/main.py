from objects import *

def pickEntity(choice):
    if choice == 1:
        return Player()
    elif choice == 2:
        return NPC()
    elif choice == 3:
        return Object()
    else:
        print("Can't do that choom, gotta make a decision")
        return None

def interactWithEntity(entity):
    print("Finding the correct Night City entity...")

def main():
    print("Welcome to Night City!")

    entities = []
    while True:
        print("1 - Add entity to interact with - ")
        print("2 - Interact with your chosen entities - ")
        print("3 - Exit Night City (The good ending) - ")

        try:
            choice = int(input("Make your decision...: "))

            if choice == 1:
                print("Choose Who/What to interact with:")
                print("1. V (Player Character)")
                print("2. Johnny Silverhand (NPC)")
                print("3. Arch Nazare (Motorcycle)")

                entity_choice = int(input("Your choice: "))
                entities.append(pickEntity(entity_choice))
            
            elif choice == 1:
                interactWithEntity(entities[0])

            else:
                print("Come on choom, we went over this... gotta do something")

        except ValueError:
            print("Gotta pick something choom")

main()