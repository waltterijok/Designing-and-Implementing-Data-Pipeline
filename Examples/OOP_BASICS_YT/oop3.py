class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def bark(self):
        print("Bark")

class Kitty:
    def meow(self):
        print("meow")

d = Dog("Tim", 34)
d.set_age(23)
print(d.get_name(), d.get_age())
k = Kitty()
