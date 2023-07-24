#ase class
class Animal():
    
    def __init__(self) -> None:
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animnal") 
    
    def eat(self):
        print("I am eating")



#inheritance - reuse methods of other class
class Dog(Animal):
    
    def __init__(self) -> None:
        Animal.__init__(self)
        print("Dog Creted")
        
    #Overide the older method
    def who_am_i(self):
        print("I am Dog")
        
    #Also add on methods
    def bark(self):
        print("Woof!")



mydog = Dog()
print(mydog)
#all the methods avaivble to Animal now avainle to my Dog class
print(mydog.who_am_i())
print(mydog.bark())


myanimal = Animal()
print(myanimal)