class Car:
    color =""
    speed = 0

    def upSpeed(self,value):
        self.speed +=value
    
    def downSpeed(self,value):
        self.speed -=value


# Red,Blue,Yello 자동차 객체 생성
car1 = Car()
car1.color ="Red"
car1.upSpeed(222)
print(car1)
car1.downSpeed(111)

car2 = Car()
car2.color ="Blue"
car2.upSpeed(222)

car3 = Car()
car3.color ="Yello"
car3.upSpeed(222)

print("첫번째 자동차 색상은 {} 이며, 현재 속도는 {}km입니다".format(car1.color,car1.speed))
print("두번째 자동차 색상은 {} 이며, 현재 속도는 {}km입니다".format(car2.color,car2.speed))
print("세번째 자동차 색상은 {} 이며, 현재 속도는 {}km입니다".format(car3.color,car3.speed))