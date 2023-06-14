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
