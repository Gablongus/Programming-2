class Vehicle:
    def __init__(self, name, tires):
        self._name = name
        self._tires = tires

    def get_name(self):
        return self._name

    def get_tires(self):
        return int(self._tires)

class Car(Vehicle):
    def __init__(self, name, tires, worth):
        super().__init__(name, tires) # Or Vehicle.__init__(name, tires)
        self.worth = worth

class Truck(Vehicle):
    def __init__(self, name, tires, mileage):
        super().__init__(name, tires)
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, tires, hometown):
        super().__init__(name, tires)
        self.hometown = hometown