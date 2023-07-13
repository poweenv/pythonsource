# class Parent:
#     def __init__(self) ->None:
#         self.value ="test"
#         print("Parent class __init__ 호출")

#     def test(self):
#         print("Parent 클래스의 test 호출")

# class Child(Parent):
#     def __init__(self) ->None:
#         super().__init__()
#         print("Child 클래스의 __init__ 호출")
# child = Child()
# child.test()
# print("부모의 value = {}".format(child.value))

class Car:
    speed =0

    def upSpeed(self,value):
        self.speed = self.speed + value
 #       print("현재 속도(슈퍼클래스) : %d " self.speed)


    def downSpeed(self,value):
        self.speed = self.speed - value

class Sedan(Car):
    seatNum = 0

    def upSpeed(self,value):
        """
        오버라이딩
        """
        self.speed = self.speed + value

        if self.speed >150:
            self.speed=150
#            print("현재 속도(슈퍼클래스) : %d " self.speed)

    def downSpeed(self,value):
        self.speed = self.speed - value

    def getSeatNum(self):
        return self.seatNum
    
class Truck(Car):
    capacity = 0

    def getCapacity(self):
        return self.capacity
    
sedan1, truck1 = Sedan(),Truck()

sedan1.upSpeed(1000)
sedan1.downSpeed(20)
sedan1.seatNum=10

truck1.upSpeed(150)
truck1.downSpeed(10)
truck1.capacity = 100

print("승용차의 속도는 {}km, 좌석수는 {} 개 입니다".format(sedan1.speed,sedan1.getSeatNum()))
print("트럭의 속도는 {}km, 총 중량은 {} ton 입니다".format(truck1.speed,truck1.getCapacity()))