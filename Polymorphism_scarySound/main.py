#main.py
## import class 'Animal, Bird' from scarySound.py
from scarySound import Animal, Bird
def main():
    # create objects of Animal and Bird class 
    a = Animal()
    b = Bird()
    
    # polymorphism
    a.scarySound() # Animals are running away due to scary sound.
    b.scarySound() # Birds are flying away due to scary sound.
# standard boilerplate to set 'main' as starting function
if __name__=='__main__':
    main()