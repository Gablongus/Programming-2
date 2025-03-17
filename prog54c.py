class Circle:
    # Constructor: sets up class data
    def __init__(self, radius, ):
        self.radius = radius
        self._diameter = 0   # _ prefix basically means 'private' so
        self._area = 0  # it should only be called in the class
        self._circum = 0
        self._pi = 3.1415926535

    def calculate(self):
        self._diameter = self.radius + self.radius
        self._area = self._pi * (self.radius ** 2)
        self._circum = 2 * self._pi * self.radius

    #TODO: Convert rest of program to circles

    # Accessor/Getter Method(s): returns class data
    def get_area(self):
        return self._area

    def get_circumference(self):
        return self._circum

def main():
    radius = int(input("Enter Radius: "))
    # Make a new 'Circle' object/instance
    circle = Circle(radius)
    circle.calculate()
    print("Area:", circle.get_area())
    print("Circumference:", circle.get_circumference())
    pass


if __name__ == "__main__":
    main()