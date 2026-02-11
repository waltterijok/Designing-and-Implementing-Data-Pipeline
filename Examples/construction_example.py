'''
Use class-level attributes (root of the class) only for values that are the same for every object

Examples: 
    - Number of wheels on a car
    - Pi constant
    - Configuration shared by all instances
    - version numbers...
'''

class Car:
    wheels = 4      # this is same for all Car(s) as a default

'''
These attributes live on the same class, not the object.

Use constructor (__init__) for instance: specific data. These are unique to the object.

Example:
    - Car color
    - Max speed
    - Current car
    - Registration number
'''

class Car:
    wheels = 4      # Shared by all Car(s)

    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

'''
Every time you create a new object, the constructer (__init__) runs and gives that specific object its own attributes.

Why are these attributes not in the root? Because the attributes in the root are shared unless they're overwritten.
'''

class Person:
    hobbies = []

person1 = Person()
person2 = Person()

person1.hobbies.append("football")
person1.hobbies.append("reading")
person2.hobbies.append("singing")
print(person2.hobbies)

'''
If the list was inside a constructor (__init__), each would get its own list
'''

class Student:
    def __init__(self):
        self.hobbies = []

student1 = Student()
student2 = Student()

student1.hobbies.append("music")
student1.hobbies.append("gym")
student2.hobbies.append("cars")

print(student2.hobbies, student1.hobbies)