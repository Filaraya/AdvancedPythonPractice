# Restaurant
class Restaurant:
    """class describes restaurant"""

    def __init__(self, name, cuisinetype):
        """two  attributes a restaurant name and cuisine type"""
        self.restaurantName = name
        self.cuisinetype = cuisinetype

    def describe_restaurant(self):
        """describes restaurant"""
        print(f" the name of the restaurant is {self.restaurantName} and type is {self.cuisinetype}")

    def open_restaurant(self, status):
        """message indicating that the restaurant is open"""
        if status == "open":
            print("open")
        else:
            print("closed")


myRestaurant = Restaurant("fila", "traditional")
myRestaurant.describe_restaurant()
myRestaurant.open_restaurant("op")
