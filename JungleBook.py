#jungleBook.py

from abc import ABCMeta, abstractmethod

#Abstract class and abstract method declaration

#class declaration
class Jungle (meataclass=ABCMeta):
#constructor with default values
    def __init__(self, name="Unknown"):
        self.visitorName = name
    def welcomeMessage(self):
        print("Hello %s, Welcome to the Jungle" % self.visitorName)

    # abstract method is compulsory to defined in child-class
    @abstractmethod
    def scarySound(self):
        pass

class RateJungle(Jungle):
    def __init__(self, name, feedback):
    # feedback (1-10) : 1 is the best. self.feedback = feedback # Public Attribute
        # inheriting the constructor of the class
        super().__init__(name)
    # using parent class attribute i.e. visitorName
    def printRating(self):
        print("Thanks %s for your feedback" % self.visitorName)
