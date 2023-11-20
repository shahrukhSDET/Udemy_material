class Animal:
    def eat(self):
        print('Animals can eat')

    def Mammals(self):
        print('Mammals can evolve and reproduce')

class Dog(Animal):
    def bark(self):
        print('Dog can bite')

class Fish(Animal):
    def swim(self):
        print('fishes can swim')

dogs = Dog()
dogs.bark()
dogs.eat()
dogs.Mammals()

fish = Fish()
fish.swim()
