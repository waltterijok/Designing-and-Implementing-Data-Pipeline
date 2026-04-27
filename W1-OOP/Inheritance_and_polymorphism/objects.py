from abc import abstractmethod, ABC

class Entity(ABC):
    __name: str
    __position: str
    @abstractmethod
    def __init__(self, name: str, position: str):
        self.__name = name
        self.__position = position
        return None
    
    def name(self):
        print(self.__name)
        return None
    
    def position(self):
        print(self.__position)
        return None
    
class Player(Entity):
    def __init__(self):
        super().__init__("V", "Night City")
        self._chipped_in = False

    def getChipped(self):
        if not self._chipped_in:
            print("Give me the good stuff doc, none of that last gen shit either!")
            print("WHIRRRRR")
        self._chipped_in = True

    def doGig():
        print("Time to get some eddies...")


class NPC(Entity):
    def __init__(self):
        super().__init__("Johnny Silverhand", "Night City (The relic)")

    def runMouth(self):
        print("I saw corps strip farmers of water... and eventually of land. Saw them transform Night City into a machine fueled by people's crushed spirits, broken dreams and emptied pockets. Corps've long controlled our lives, taken lots... and now they're after our souls! V, I've declared war not because capitalism's a thorn in my side or outta nostalgia for an America gone by. This war's a people's war against a system that's spiraled outta our control. It's a war against the fuckin' forces of entropy, understand? Do whatever it takes to stop 'em, defeat 'em, gut 'em. If I gotta kill, I'll kill. If I need your body, I'll fuckin' take it! Fuckin' hell... You still don't see it. But you will one day")

    def beAnAsshole(self):
        print("Stick some iron in your mouth and pull the trigger!")


class Object(Entity):
    def __init__(self):
        super().__init__("Arch Nazare", "Night City (garage)")
        self._running = False

    def isRunning(self):
        print(f"The engine is running {self._running}")
        return self._running

    def turnOn(self):
        if not self._running:
            print("Firing up the engine")
        self._running = True

    def turnOff(self):
        if self._running:
            print("Shutting the bike down...")
        self._running = False

    def popWheelie(self):
        if not self._running:
            print("It aint running, gonk!")
        else:
            print("WROOM WROOM, I'M DOING A WHEELIE!")

'''NPC().runMouth()'''

johnny = NPC()

johnny.beAnAsshole()
johnny.runMouth()

'''nazare = Object()

nazare.isRunning()
nazare.popWheelie()
nazare.turnOn()
nazare.isRunning()
nazare.popWheelie()'''

