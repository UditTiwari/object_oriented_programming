class Instructors:
    #Attribute(var)
    companyName="Google"
    #(__init__) is a built-in function know as Initializer used to initialize objects with intial values.
    # it is called automatically when a new object is created from a class.
    #(self) paramter is a refrence to the current instance of the class
    def __init__(self,course,duration) -> None:
        self.course = course
        self.duration = duration

    def printinfo(self):
        print(f"My company name is {Instructors.companyName} of duration {self.duration}")

# Two instance of class
elearning = Instructors("Python",8)
bls = Instructors("Javascript",5)

#Acessing Methods of a class {ObjectName.Method}
elearning.printinfo()

#Modifying existing Attribute
elearning.course = 'New python 3.12'

#Delete the Attribute
# del elearning.duration

#Acessing Attribute of a class {ObjectName.Attribute}
print(elearning.course)
print(elearning.duration)