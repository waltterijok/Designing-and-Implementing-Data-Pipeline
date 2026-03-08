class Animal:
    def __init__(self, sound):
        self.sound = sound
    def makeSound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self):
        super().__init__("Meow!")

class Dog(Animal):
    def __init__(self):
        super().__init__("Bark!")
    def makeSound(self):
        print("Who let the dogs out!?")

Cat().makeSound()
Dog().makeSound()