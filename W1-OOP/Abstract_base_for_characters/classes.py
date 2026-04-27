from abc import abstractmethod, ABC

class GameCharacter(ABC):
    __attack: str
    __defend: str
    @abstractmethod
    def __init__(self, attack: str, defend:str):
        self.__attack = attack
        self.__defend = defend
        return None
    
    def attack(self):
        print(self.__attack)
        return None
    
    def defend(self):
        print(self.__defend)
        return None
    
class Warrior(GameCharacter):
    def __init__(self):
        super().__init__("STRIKE", "SHIELD")
        return None

class Mage(GameCharacter):
    def __init__(self):
        super().__init__("FIREBOMB", "WARD")
        return None

class Archer(GameCharacter):
    def __init__(self):
        super().__init__("LOOSE", "DODGE")
        return None
    
'''Warrior().attack()
Warrior().defend()

Mage().attack()
Mage().defend()

Archer().attack()
Archer().defend()'''