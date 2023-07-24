class Dog():
    
    def __init__(self,name) -> None:
        self.name = name
        
    def speak(self):
        return self.name + "say woof!"
    
    
    
class Cat():
    
    def __init__(self,name) -> None:
        self.name = name
        
    def speak(self):
        return self.name + "say meow!"
    
    
#Lets create instance of that 

niko = Dog("niko")
niko = Cat("felic")