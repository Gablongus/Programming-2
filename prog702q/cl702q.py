class Vehicle:
    def __init__(self, name, tires):
        self.name = name
        self.tires = tires
        self.value = 0

class Car(Vehicle):
    def __init__(self, name, tires, worth):
        super().__init__(name, tires) # Or Vehicle.__init__(name, tires)
        self.worth = worth

class Truck(Vehicle):
    def __init__(self, name, tires, mileage):
        super().__init__(name, tires)
        self.mileage = mileage
        self.value = 50000

class Bus(Vehicle):
    def __init__(self, name, tires, hometown):
        super().__init__(name, tires)
        self.hometown = hometown
        self.value = 50000