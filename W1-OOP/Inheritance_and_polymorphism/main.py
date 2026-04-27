from objects import *

def pickEntity():

def interactWithEntity():

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