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

def main():
     #create object of class Jungle
    j = Jungle("Meher")
    j.welcomeMessage() # Hello Meher, Welcome to the Jungle
    # if no name is passed, the default value i.e. Unknown will be used
    k = Jungle()
    k.welcomeMessage() # Hello Unknown, Welcome to the Jungle
# standard boilerplate to set 'main' as starting function
if __name__=='__main__':
    main()