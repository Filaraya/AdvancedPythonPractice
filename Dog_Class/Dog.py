#Dog.py

class Dog: #declaration of dog class
    """to model a dog"""
    def __init__(self,name,age):
        """intialize name and age attributes."""
        self.name = name
        self.age = age
    
    #what can a dog can do it play and sound
        
    def play(self):
        """asking a dog to play"""
        print(f"{self.name} is now playing")
        
    def sound(self):
        """when a dog make a sound/bark"""
        print(f"{self.name} is making sound")
        
    def infoDog(self):
        print(f"The dog's name is {self.name} and {self.age} years old")
        
    


myDog= Dog("Simba",4) #declaration of object
yourDog= Dog("Bob",6)
print(myDog.infoDog())
print(myDog.play())
print(myDog.sound())

print("")
print(yourDog.infoDog())
print(yourDog.play())
print(yourDog.sound())