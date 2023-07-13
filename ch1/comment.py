# 주석

"""
    여러 줄 주석 처리 
"""
'''
    여러 줄 주석 처리
'''

#화면축력 - print() / 변수타입 확인 type()
print("hello python")
print("100")
print(25.3)
print(type(100))
print(type("100"))
print(type(True))
print(type(0.1))

# sep : 문자열 사이 구분자(기본값 spacebar)
print('t','e','s','t') # t e s t
print('t','e','s','t',sep='')
print('t','e','s','t',sep='-')

#end : 기본값은 엔터
print("Welcome To",end=' ')
print("the black prad")

# format : %s-문자열,정수,실수가능, %d-정수, %f-실수, %c(문자열 하나)
print("%d" % 100)
print("%5d" % 100) # 5자리 맞춰서 출력
print("%05d" % 100) # 5자리 맞춰서 출력(자릿수 없는 것은 0으로 채우기)
print()
print("%s" % "hi")
print("%5s" % "hi")
print()
print("%-8.2f" % 123.21345612)
print("%8.2f" % 123.2132)
print("%8.2f" % 123.21345612)

# 변수 선언(타입 선언 안함-값에 따라 타입이 결정됨)
number =3
print("I eat %d apples" % number)
print("I eat", number,"apples")

print()
print("%d : %s"%(1,"hong"))

print("I eat %s apples"% "two")

# 98%
print("Error is %d%%" % 98)

# format() 함수
print("\nformat 함수 : {}")
print("{} and {}".format("you","Me"))
print("I eat {} apples",format(3))
print("I eat {0} apples",format(3))
print("{0} and {1} and{0}".format("you","Me"))
print("{var1} and {var2}".format(var1="You",var2="me"))
print("{0} and {var2}".format("You",var2="me"))

# 이스케이프 문자 : \n, \t
print("\n줄바꿈\n연습")
print("\\ 역슬래쉬")
print("\n\t \\ 그대로 출력")
print(r"\n\t \\ 그대로 출력")

print("글자가 '강조' 되는 효과") # 문자 표현시 "", '' 허용
print('글자가 "강조" 되는 효과') # 문자 표현시 "", '' 허용

# 문자열 - "",'', """한글""",'''한글'''

str1= "Life is too short, You need Python"
str2= 'Life is too short, You need Python'
str3= '''Life is too short, You need Python'''
str3= """Life is too short, You need Python"""

num1 = num2 =10
print(num1,num2)

num1, num2 = 10,15
print(num1,num2)

# 한글+ 10=? X

# 타입변환 숫자=> 문자열 : str()
#print(num1 + str(num2))

a, b =7233,5.123456
print("a + b = %d" % (a+b))
print("a - b = %d" % (a-b))
print("a * b = %d" % (a*b))
print("a / b = %f" % (a/b))   #스크립트와 같은 개념
print("a // b = %f" % (a//b)) #자바와 같은 개념(몫)
print("a % b = " ,(a%b))
print("a ** b = ", (a**b))

# type() : 변수 타입 확인
# str() : 문자열 변환, int() : 숫자 변환, float() : 실수, bool() : boolean 변환
print(str(3.5))
print(str(3.5),type(str(3.5)))
print(int(True),type(int(True)))
print(int(False),type(int(False)))
print(bool(0.1), type(bool(0.1)))
print(float("98.99"), type(float("98.99")))
# print(int("98.99"), type(int("98.99"))) ValueError: invalid literal for int() with base 10: '98.99'
print(int(98.99), type(int(98.99))) # 숫자의 경우에는 소수값을 없애고 나오지만 문자열로 받는 경우는 그러지 못해 에러가난다

# 동전 교환
money, c500,c100,c50,c10=0,0,0,0,0

money = 7777

#500원 : 17개
c500= money // 500
money %= 500 #money = money % 500 의 나머지값

c100 = money //100
money %= 100

c50 = money //50
money %= 50

c10 = money //10
money %= 10

print("500원 {}개".format(c500))
print("100원 {}개".format(c100))
print("50원 {}개".format(c50))
print("10원 {}개".format(c10))
print("남은 돈 {}원".format(money))

# ||, &&, ! => X
a,b,c = 100,60,15
print("and : ", a> b & a>c)
print("and : ", a> b and a>c)
print("or : ", a> b or a>c)
print("not : ", not(a> b))