from classes import *

def pickCharacter(choice):
    if choice == 1:
        return Warrior()
    elif choice == 2:
        return Mage()
    elif choice == 3:
        return Archer()
    else:
        print("Invalid choice!")
        return None
        
def simulateBattle(combatant, enemy):
    print("The battle nears... Prepare yourself!")
    print("You move to attack...")
    combatant.attack()
    print("The enemy defends!")
    enemy.defend()
    print("They're striking back, brace!")
    enemy.attack()
    combatant.defend()
    print("You successfully defended yourelf!")
    combatant.attack()
    print("You landed a hit!")
    print("'ARGHH, you foul scoundrel, you've bested me for now!'")
    print("Congratulations, you've won!")


def main():
    print("Welcome to battle simulator!\n")

    fighters = []
    while True:
        print("1. --- Choose your fighter! (create character) ---")
        print("2. --- Start the battle! (start simulation) ---")
        print("0. --- YIELD! (exit) ---\n")

        try:
            choice = int(input("What will it be?: "))

            if choice == 0:
                print("I see a coward... for shame!")
                print("Retreating from battle...\n")
                break

            elif choice == 1:
                print("Choose your combatant!")
                print("1. Warrior")
                print("2. Mage")
                print("3. Archer")

                combatand_choice = int(input("Your combatant: "))
                fighters.append(pickCharacter(combatand_choice))

                enemy_choice = int(input("Enemy combatant: "))
                fighters.append(pickCharacter(enemy_choice))

            elif choice == 2:
                simulateBattle(fighters[0], fighters[1])
                print("\nThe battle is over... Rest now\n")

            else:
                print("What are you playing at? Give me a proper input!")

        except ValueError:
            print("Invalid input, try again!")

main()