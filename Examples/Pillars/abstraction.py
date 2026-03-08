from abc import abstractmethod, ABC

class Animal(ABC):
    __sound: str
    __color: str
    @abstractmethod
    def __init__(self, sound: str, color: str):
        self.__sound = sound
        self.__color = color
        return None
    
    def makeSound(self):
        print(self.__sound)
        return None
    
    def myColor(self):
        print(self.__color)
        return None
    
class Cat(Animal):
    def __init__(self):
        super().__init__("Meow!", "I am brown")
        return None
    
class Dog(Animal):
    def __init__(self):
        super().__init__("Woof!", "I am blue")
    
cat1 = Cat()
cat1.makeSound()
cat1.myColor()

dog1 = Dog()
dog1.makeSound()
dog1.myColor()

Cat().makeSound()
Dog().makeSound()


