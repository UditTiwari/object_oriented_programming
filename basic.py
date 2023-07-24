#oops allow programmers to create their own objects that have methods and attributes.

class NameOfClass(): #class name in camel casing
    
    #looks like class its called method when its inside class
    def __init__(self,param1,param2):
        self.param1 = param1  #attribute of the function
        self.param2 = param2
        
    def some_method(self): #using self we let python know that this is know this is method connected to the class
        #perform some action
        print(self.param1)