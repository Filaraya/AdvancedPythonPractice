#main.py
#import class 'Jungle' from jungleBook.py
from JungleBook import Jungle

def main():
# create object of class Jungle
    j = Jungle("Meher")
    j.welcomeMessage() # Hello Meher, Welcome to the Jungle
    # if no name is passed, the default value i.e. Unknown will be used
k = Jungle()
k.welcomeMessage() # Hello Unknown, Welcome to the Jungle
# standard boilerplate to set 'main' as starting function
if __name__=='__main__':
    main()