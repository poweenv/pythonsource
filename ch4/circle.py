import math

class Circle:
    def __init__(self,radius)->None:
        self.__radius =radius

    """
    __ 변수명 private 과 동일
    """
    def getCircom(self):
        return 2 * math.pi * self.__radius
    
    def getArea(self):
        return math.pi * (self.__radius**2)
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self):
        self.__radius =radius

circle = Circle()
#print(circle.__radius) TypeError: Circle.__init__() missing 1 required positional argument: 'radius'
# __radius 접근 -> getter, sette  이용
print("반지름 : {}".format(circle.getRadius()))
print("원의 둘레 : {}".format(circle.getCircom()))
print("원의 둘레 : {}".format(circle.getArea()))

circle.setRadius(20)
print("원의 둘레 : {}".format(circle.getCircom()))
print("원의 둘레 : {}".format(circle.getArea()))