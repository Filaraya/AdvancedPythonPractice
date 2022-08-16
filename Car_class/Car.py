#Car.py
class Car:
    """abstract of car class"""
    def __init__(self,make,model,year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        
    def get_description(self):
        """Return the information of car"""
        info= f"this car is {self.make}, {self.model}, on {self.year}"
        return info.title()
    
myCar = Car("Acura", "TL", "2003")
print (myCar.get_description())