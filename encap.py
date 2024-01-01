class Cars:
    def __init__(self,speed,color) -> None:
        # self.speed = speed
        # self.color = color
        #making variable Private
        self.__speed = speed
        self.__color = color
    
    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed
    
ford = Cars(250,"Green")
nissan = Cars(300,"red")
toyota = Cars(350,"blue")

#change the speed using method
ford.set_speed(450)

#change the  Directly using speed var
ford.speed = 500

print(ford.get_speed())
# print(ford.__color)