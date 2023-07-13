# 주차장 프로그램

# 메뉴
# [1] 자동차 넣기 : [2]자동차 빼기: [3]종료 :

# 주차장 리스트 생성
parking_lot =[]

top, car_name =0,"A"
menu ="[1] 자동차 넣기 : [2]자동차 빼기: [3]종료 :"
while True:
    no = int(input(menu))

    if no <= 3:
        if no ==1:
            if top >=5:
                print("주차장 꽉 찼음")
            else:
                parking_lot.append(car_name)
                print("{} 자동차 들어감. 주차장 상태 ==>{}".format(car_name,parking_lot))
                top +=1
                car_name=chr(ord(car_name)+1)
        elif no==2:
            if top >0:
                out_car = parking_lot.pop()
                print("{} 자동차 나감. 주차장 상태 ==>{}".format(out_car,parking_lot))
                top -=1
                car_name=chr(ord(car_name)-1)
            pass
        else:
            print("프로그램 종료")
            break
    else:
        print("check your number")

# print(ord("A"))
# print(chr(65))