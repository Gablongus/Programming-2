from cl702q import  *


def main():
    try:
        vehicles: list[Vehicle] = []
        with (open("../Langdat/prog702q.dat", 'r') as f):
            num = int(f.readline())
            while num != 99:
                name = f.readline()
                tires = f.readline()
                if num == 1:
                    worth = float(f.readline())
                    v = Car(name, tires, worth)
                    vehicles.append(v)
                elif num == 2:
                    mileage = int(f.readline())
                    v = Truck(name, tires, mileage)
                    vehicles.append(v)
                elif num == 3:
                    hometown = f.readline().strip()
                    v = Bus(name, tires, hometown)
                    vehicles.append(v)
                num = int(f.readline())
            totalnum = 0   #Total Number of Vehicles
            cartot = 0.0   #Total Amount that CARS are worth
            tot = 0.0      #Total Amount that all Vehicles are worth
            truckleast = 0 #Smalles Milage on a Truck
            cartires = 0   #Total of Tires on Cars
            trucktires = 0 #Total of Tries on Trucks
            bustires = 0   #Total of tires on Busses
            largehome = "" #Longest Home Destination
            for vehicle in vehicles:
                if isinstance(vehicles, Car):
                    tot += vehicle.worth
                    totalnum += 1
                    cartot += vehicle.worth
                    cartires += vehicle.tires
                elif isinstance(vehicles, Truck):
                    tot += vehicle.worth
                    tl = vehicle.mileage
                    if tl < truckleast:
                        truckleast = tl
                    totalnum += 1
                    trucktires += vehicle.tires
                elif isinstance(vehicles, Truck):
                    tot += vehicle.worth
                    ht = vehicle.hometown
                    if len(ht) > len(largehome):
                        largehome = ht
                    totalnum += 1
                    bustires += vehicle.tires




            print("Total Number of Vehicles:", totalnum)
            #TODO Fix and Finish
            print("Total number of students taught:", tot_stus)
            print("Smallest favorite admin word:", small)
            print("Largest favorite admin word:", large)
    except OSError as e:
        print("Error: ", e)
    pass

if __name__ == "__main__":
    main()