class User:
    """stores users information"""
    def __init__(self, first_name, last_name):
        """stores first and last name"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """describes user information"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()

    def greet_user(self):
        """greeting user"""
        print(f" Hello {self.first_name} {self.last_name}")

myUser = User("Filmon", "Araya")
print(myUser.describe_user())
myUser.greet_user()
