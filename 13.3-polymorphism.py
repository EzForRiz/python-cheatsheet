# Polymorphism in object-oriented programming (OOP) is the ability of an object or method to take on multiple forms or behaviors, allowing a single interface to interact with different object types




# Polymorphism example
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()  # Works for any object with speak()

dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!
