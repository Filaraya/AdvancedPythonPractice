class User:
    """stores users information"""

    def __init__(self, first_name, last_name):
        """stores first and last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """describes user information"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()

    def greet_user(self):
        """greeting user"""
        print(f" Hello {self.first_name} {self.last_name} and tried {self.login_attempts}")

    def increment_login_attempts(self):
        """increment login attempts"""
        self.login_attempts += 1

    def reset_login_attempt(self):
        """reset the value of attempt to 0"""
        self.login_attempts == 0



myUser = User("Filmon", "Araya")
print(myUser.describe_user())
myUser.increment_login_attempts()
myUser.increment_login_attempts()
myUser.greet_user()
myUser.reset_login_attempt()
myUser.greet_user()
