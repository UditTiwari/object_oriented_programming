class Person:
    def __init__(self,fname,lname) -> None:
        self.firstname= fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname,self.lastname)

florist = Person("Jane","Mary")
florist.printname()
# print(florist.firstname)

#CHILD CLASS
# NOTE: if we create a child class without __init__() method it will inherit all methods and attribute of parents class.
class Lawyers(Person):

    def __init__(self,fname,lname,casetype) -> None:
        #if u want to keep __init__ of Parents class
        Person.__init__(self,fname,lname)
        self.casetype = casetype

        # self.firstname= fname
        # self.lastname = lname
    
    def printinfo(self):
        print(f'Hello my name is {self.firstname} {self.lastname}')



happy_lawyers = Lawyers("Jack","Sparrow","Pirate")

happy_lawyers.printname()

happy_lawyers.printinfo()

print(happy_lawyers.casetype)


