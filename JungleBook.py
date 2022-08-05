#jungleBook.py
#class declaration
class Jungle:
#constructor with default values
    def __init__(self, name="Unknown"):
        self.visitorName = name
    def welcomeMessage(self):
        print("Hello %s, Welcome to the Jungle" % self.visitorName)
