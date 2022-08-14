#Dog.py

class Dog: #declaration of dog class
    """to model a dog"""
    def __init__(self,name,age):
        """intialize name and age attributes."""
        self.name = name
        self.age = age
        
    def infoDog(self):
        print(f"Hello my dog is {self.name} and {self.age} years old")
        
    


s= Dog("Simba",4) #declaration of object
print(s.infoDog())