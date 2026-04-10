class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def start(self):
        print("Vehicle started !")

    def stop(self):
        print("Vehicle stopped !")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

class Truck(Vehicle):
    def load_goods(self):
        print("Truck is loading goods")

brand = input("Enter vehicle brand: ")
fuel_type = input("Enter  fuel type of the vehicle: ")

c = Car(brand, fuel_type)
b = Bike(brand, fuel_type)
t = Truck(brand, fuel_type)

#Car -
c.start()
c.drive()
c.stop()

#Bike -
b.start()
b.ride()
b.stop()

#Truck -
t.start()
t.load_goods()
t.stop()
