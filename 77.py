class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

d = Dog()
c = Cat()
animal_sound(d)
animal_sound(c)

