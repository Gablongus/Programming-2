class Time:
    def __init__(self, designing, coding, debugging, testing):
        self.designing = designing
        self.coding = coding
        self.debugging = debugging
        self.testing = testing
        self._total = 0
        self._percents = [0]*4  # [0,0,0,0]

    def _get_percent(self, number):
        return round((number/self._total) * 100, 2)

    def calculate(self):
        self._total = self.designing + self.coding + self.debugging + self.testing
        self._percents[0] = self._get_percent(self.designing)
        self._percents[1] = self._get_percent(self.coding)
        self._percents[2] = self._get_percent(self.debugging)
        self._percents[3] = self._get_percent(self.testing)

    def display(self):
        print("Task\t\t% 12Time")
        print(f"Designing:\t\t {self._percents[0]}%")
        print(f"Coding:\t\t\t {self._percents[1]}%")
        print(f"Debugging:\t\t {self._percents[2]}%")
        print(f"Testing:\t\t {self._percents[3]}%")



def main():
    print("Enter the time spent doing these things:\n")
    designing = float(input("Designing: "))
    coding = float(input("Coding: "))
    debugging = float(input("Debugging: "))
    testing = float(input("Testing: "))
    print()

    # Make a new 'Total' object, pass in the numbers to the constructor
    times = Time(designing, coding, debugging, testing)
    times.calculate()
    times.display()
    pass


if __name__ == "__main__":
    main()