class Dog():
    
    #Class object attribute
    #Same for any instance of a class
    species = 'mammal'
    
    def __init__(self,breed:str,name:str,spots:bool) -> None:
        
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        # self.my_attribute = mybreed
        self.breed = breed
        self.name = name
        self.spots = spots
    
my_dog = Dog(breed = 'Huskie',name='jojo',spots=True)

print(Dog.species)




print(my_dog.name)
print(my_dog.breed)
print(my_dog.spots)