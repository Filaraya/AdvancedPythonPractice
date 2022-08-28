class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initializw attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descirptive name"""
        listName = f"{self.year} {self.make} {self.model}"
        return listName.title()

myCar = Car("Acura", "TL", 2003)
print(myCar.get_descriptive_name())
