class Dog:
    def __init__(self):
        self.sound = "bark"

    def makeSound(self):
        print(self.sound)

class Pomeranian(Dog):
    def __init__(self):
        super().__init__()

    def showTrick(self):
        print(f"{self.sound}, I'm dancing!")

class Labrador(Dog):
    def __init__(self):
        super().__init__()

    def fetchBall(self):
        print(f"{self.sound}, Here is the ball!")

pomeranian = Pomeranian()
labrador = Labrador()

pomeranian.makeSound()
pomeranian.showTrick()

labrador.makeSound()
labrador.fetchBall()