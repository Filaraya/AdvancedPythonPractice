class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #default values 0
    def get_descriptive_name(self):
        """Return a neatly formatted name"""
        listName = f"{self.year} {self.make} {self.model}"
        return listName.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles")
    def update_odometer(self,milage):
        """updating odometer"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("not able to roll back")

    def incrimental_odometer(self, miles):
        """incremental milage adding"""
        self.odometer_reading += miles


class ElectricCar(Car):
"""Represent aspects of a car, specific to electric vehicles."""
 
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) 
        self.battery_size = 75



myCar = Car("Acura", "TL", 2003)
print(myCar.get_descriptive_name())
myCar.odometer_reading = 23 #updating the odometer reading
myCar.update_odometer(50)
myCar.incrimental_odometer(10)
myCar.read_odometer()
yourCar = Car("Toyota","corolla",2020)
yourCar.odometer_reading = 23 #updating the odometer reading
yourCar.update_odometer(50)
yourCar.incrimental_odometer(10)
yourCar.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


