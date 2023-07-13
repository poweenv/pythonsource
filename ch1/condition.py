# 조건문
# if, if~else, if~elif~else

if True:
    print("True")

a= 200
if a < 100:
    print("a는 100보다 작다")
print("조건문에서 하나의 블럭 개념은 들여쓰기로 구분")

# a는 100보다 크고 200보다 작거나 같다
if   100< a <=200:  #a>100 and a<=200:
    print("a는 100보다 ㅋ고 200보다 작거나 같다")

# 3 개의 변수 선선, 12, 6 ,18 담기
# 가장 큰 수 찾기
a,b,c = 12,6,18
max =a
if max <b:
    max =b

if max <c:
    max =c

a = 55
if a <100:
    print("작다")
else:
    print("크다")

import datetime
now = datetime.datetime.now()
print(now)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second) )

#오전/오후 출력
if now.hour < 12:
    print("오전")
else:
    print("오후")

# 삼항 연잔사 now.hour <12 ? "오전" : "오후"
# 참일때 실행 구문 if 조건 else 거짓일때 실행 구문

str="안녕하세요" if True else "반갑습니다"
print(str)
str="오후" if now.hour < 12 else "오후"
print(str)

# 다중조건 if ~elif ~else
num =90
if num >=90:
    print("a")
elif num>=80:
    print("b")
elif num>=70:
    print("c")
elif num>=60:
    print("d")
else:
    print("f-")

# age, height 변수 선언, 27, 180 값 담기
# age 가 20이상 지원 가능
#       키가 170 이상이면 A 지만 지원 가능 ㅜㅊㄹ력
#       키가 160 이상이면 B 지망 지원 ㄱ나을 출력
#       나머지 "지원불가" 출력
# 나이가 20세 미만 이라면 " 20세 이상 지원 가능"

age,height=27,180
if age >20:
    if height > 170:
        print("A 지망 지원 가능")
    elif height > 160:
        print(" B 지망 지원 가능")    
    else:
        print("지원불가")
else:
    print("20세 이상 지원 가능")

# 계산기 : 두 개의 수 입력, 연산자(+,-,/,//,*,%,**) 입력

num1 = input("num1")
num2 = input("num2")
sel = input("1.+ 2.- 3.* 4./ 5.// 6.** 7.%")

result=0
if op == "+":
    result = num1 +num2
elif op == "-":
    result = num1 -num2
elif op == "*":
    result = num1 *num2
elif op == "/":
    result = num1 /num2
elif op == "//":
    result = num1 //num2
elif op == "**":
    result = num1 **num2
elif op == "%":
    result = num1 %num2

print("{} {} {} = {}.".format(num1,op,num2,result))