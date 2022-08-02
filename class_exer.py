#class declaration
class Jungle:
    #constructor with default values
    def __init__(self, name="Unknown"):
        self.visitorName = name
        
    def welcomeMessage(self):
        print("Welcome to the Jungle")

j= Jungle() #create object of class Jungle
print(j.welcomeMessage()) #welcome to the Jungle

#create object of class Jungle
f = Jungle("Meher")
f.welcomeMessage() # Hello Meher, Welcome to the Jungle

