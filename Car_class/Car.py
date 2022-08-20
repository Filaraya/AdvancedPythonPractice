#Car.py
class Car:
    """abstract of car class"""
    def __init__(self,make,model,year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #setting a default value of an attribute
        #self.color = " "
    def get_description(self):
        """Return the information of car"""
        info= f"this car is {self.make}, {self.model}, on {self.year}"
        return info.title()
    
    def read_odometer(self):
        """print car's milage"""
        print(f"This is car has {self.odometer} milage")
    
    def update_odometer(self,mileage):
        """update the car milage on the method"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print ("You can't roll back an odometer")
            
    def incrimental_odometer(self,miles):
        """adding the miles to the orginal reading"""
        self.odometer += miles
        
    """
    def car_color(self):
        #info about car's color
        print (f"the car color is {self.color} color")
        """
    
myCar = Car("Acura", "TL", "2003")
print (myCar.get_description())
print(myCar.read_odometer())
myCar.odometer = 124000 #updating the new milage
myCar.read_odometer()
myCar.update_odometer(126000)
myCar.read_odometer()
myCar.incrimental_odometer(10)
myCar.read_odometer()

yourCar= Car("Toyota", "RAV4",2020)
print(yourCar.get_description())

myUsedCar = Car("Sabaru","outback",2017)
print(myUsedCar.get_description())



