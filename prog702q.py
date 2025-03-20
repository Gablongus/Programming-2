from cl702q import  *


def main():
    try:
        vehicles: list[Vehicle] = []
        with (open("Langdat/prog702q.txt", 'r') as f):
            num = int(f.readline())
            while num != 99:
                name = f.readline()
                tires = f.readline()
                if num == 1:
                    worth = int(f.readline())
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
            truckleast = 0 #Smalles Value on a Truck
            cartires = 0   #Total of Tires on Cars
            trucktires = 0 #Total of Tries on Trucks
            bustires = 0   #Total of tires on Buses
            largehome = "" #Longest Home Destination
            for vehicle in vehicles:
                if isinstance(vehicles, Car):
                    tot += vehicles.worth
                    totalnum += 1
                    cartot += vehicles.worth
                    cartires += vehicles.tires
                elif isinstance(vehicles, Truck):
                    tot += vehicles.value-(0.25*mileage)
                    tl = vehicles.value-(0.25*mileage)
                    if tl < truckleast:
                        truckleast = tl
                    totalnum += 1
                    trucktires += vehicle.tires
                elif isinstance(vehicles, Bus):
                    #TODO: actually finally figure ts out
                    tot += vehicles.value
                    ht = vehicles.hometown
                    if len(ht) > len(largehome):
                        largehome = ht
                    totalnum += 1
                    bustires += vehicles.tires




            print("Total Number of Vehicles:", totalnum)
            print("Total Worth of Cars: ", cartot)
            print("Total Worth of Vehicles ", tot)
            print("Longest Home Destination: ", ht)
            print("Lowest Value of Truck: ", tl)
            print("Total Number of Car Tires: ", cartires)
            print("Total Number of Truck Tires: ", trucktires)
            print("Total Number of Bus Tires: ", bustires)
    except OSError as e:
        print("Error: ", e)
    pass

if __name__ == "__main__":
    main()