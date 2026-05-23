import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from methods.color import color
from methods.printer import title

# Classes

title('Classes')

class Car:
    pass

car = Car()

print(color('type(car)', 'magenta'), type(car))
print(color('car', 'magenta'), car)

class Bike:
    color = 'red'

    def __init__(self, size):
        self.size = size

    def run(self):
        print(color('[instancemethod] bike.run()', 'magenta'), f'Bike is running with a size of {self.size}...')

    @classmethod
    def change_factory_color(cls, new_color):
        cls.color = new_color
        print(color('[@classmethod]   bike.change_factory_color(new_color)', 'magenta'), cls.color)

    @staticmethod
    def calculate_speed():
        print(color('[@staticmethod]  Bike.calculate_speed()', 'magenta'), 'Calculating speed...')

print(Bike(45))
print(Bike.run)
print(type(Bike.run))
bike = Bike(45)
bike.run()
bike.change_factory_color('green')
Bike.calculate_speed()

# Inheritance

title('Inheritance')


class Animal:
    def __init__(self, animal_color):
        self.is_born = False
        self.color = animal_color

    def born(self):
        self.is_born = True
        print('It is born!')

    def talk(self):
        self.is_born = True
        print('It is talking...')

class Dog(Animal):
    def __init__(self, animal_color, legs):
        super().__init__(animal_color)
        self.legs = legs

    def talk(self):
        self.is_born = True
        print('It is talking as a dog...')

    def run(self):
        self.is_born = True
        print('It is running...')

class Bird(Animal):
    def __init__(self, animal_color, wings):
        super().__init__(animal_color)
        self.wings = wings

    def talk(self):
        self.is_born = True
        print('It is talking as a bird...')

    def fly(self):
        self.is_born = True
        print('It is flying...')


print(Dog.__base__)
print(Dog.__bases__)
print(Animal.__subclasses__())

print()
print(color('Dog:', 'magenta'))
dog = Dog('green', 4)
print(dog.is_born)
print(dog.color)
print(dog.legs)
dog.born()
dog.talk()
dog.run()

print()
print(color('Bird:', 'magenta'))
bird = Bird('red', 2)
print(bird.is_born)
print(bird.color)
print(bird.wings)
bird.born()
bird.talk()
bird.fly()

class Father:
    eyes_color = 'brown'
    def __init__(self, age):
        self.age = age

    def speed(self, meters_per_hour):
        print(f'It runs {meters_per_hour}m/h')

    def eat(self):
        print(f'It eats meat')

    def run(self):
        print(f'It runs mornings')

class Mother:
    eyes_color = 'blue'
    def __init__(self, age):
        self.age = age

    def speed(self, meters_per_hour):
        print(f'It runs {meters_per_hour}m/h')

    def eat(self):
        print(f'It eats salad')

class Child(Father, Mother):
    eyes_color = 'brown'

    def speed(self, meters_per_hour):
        print(f'It does not run')

    def run(self):
        print(f'It runs mornings')

    def __str__(self):
        return f"Child<{self.age}, {self.eyes_color}>"

    def __len__(self):
        return self.age

print()
child = Child(4)
child.speed(44)
child.eat()
child.run()

print(child)
print(len(child))