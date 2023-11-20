#composition ---- composition is a powerful way to create complex and flexible class structures

class Engine:
    def engine_start(self):
        print("Engine starts")

class Wheels:
    def rotate(self):
        print("Wheels rotating")

class Car:

    def __init__(self):
        self.engine = Engine()
        self.wheels = wheels()

    def drive(self):
        print('car is moving')

car = Car()
car.drive()
     


