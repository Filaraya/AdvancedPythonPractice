
class Restaurant:
    """class describes restaurant"""

    def __init__(self, name, cuisinetype):
        """two  attributes a restaurant name and cuisine type"""
        self.restaurantName = name
        self.cuisinetype = cuisinetype
        self.number_served = 0 #default value 0

    def describe_restaurant(self):
        """describes restaurant"""
        print(f" the name of the restaurant is {self.restaurantName} and type is {self.cuisinetype} and number served {self.number_served}")

    def open_restaurant(self, status):
        """message indicating that the restaurant is open"""
        if status == "open":
            print("open")
        else:
            print("closed")
    def set_number_served(self,number):
        """customer served"""
        self.number_served = number

    def increment_number_served(self,added):
        """added served person"""
        self.number_served += added




myRestaurant = Restaurant("fila", "traditional")
myRestaurant.set_number_served(30) #set the number of served
myRestaurant.increment_number_served(10) #added the value
myRestaurant.describe_restaurant()
yourRestaurant("Asmara","Habesha") #adding new object
yourRestaurant.describe_restaurant()  


myRestaurant.open_restaurant("op")
