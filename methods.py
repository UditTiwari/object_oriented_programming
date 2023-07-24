#the key diffrence bw mthods and attribute is how we call them methods are called with () and attibute without it


class Dog():
    
    #Class object attribute
    #Same for any instance of a class
    species = 'mammal'
    
    def __init__(self,breed:str,name:str) -> None:
        self.breed = breed
        self.name = name
        
    # OPERATIONS/Actions ------> Methods    
    def bark(self,number):
        print("WOOF! my name is {} and the number is {}".format(self.name,number))
        
    
my_dog = Dog(breed = 'Huskie',name='jojo')

print(my_dog.bark(7))

# print(my_dog.name)
# print(my_dog.breed)



class Circle():
    
    #Class object attribute
    pi = 3.14
    
    def __init__(self,radius=1) -> None:
        self.radius = radius
        self.area = radius * radius * self.pi
        
    #METHOD
    def get_circumfrence(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(30)

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumfrence())