# 반복문
# while, for

# 1~10 출력

i =1
while i <11:
    print(i,end=" ")
    i += 1

i =2
while i <101:
    print(i)
    i += 2

i =1
while i <10:
    print("{} * {} = {}".format(3,i,3*i))
    i +=1

#in
print("in 기호")
print("y" in "python")

# range() - 특정 범위를 지정
print(range(5))
print(list(range(1,5)))

# for
for i in range(10):
    print(i)

#사용자로부터 숫자 입력 받기 / 입력한 숫자까지 합계를 구한 후 출력

# num1 = int(input("숫자 입력"))
# hap =0
# for i in range(1,num1+1):
#     hap +=i
# print("1 ~ {} : 합계 : {}".format(num1,hap))

# sum() : 
print("sum 함수")
print(sum(range(1,11)))

for i in range(10,-1,-1):
    print(i, end=" ")
print()

for i in range(5):
    for j in range(5):
        print(i + j,end=" ")
    print()

# : 2~9단 작성
for i in range(2,9):
    for j in range(1,10):
        print("| 구구단 {} * {}={}".format(i,j,i*j),end=" ")
    print()

# break, continue: 자바 개념과 동일

i=1
while i <=10:
    if i==5:
        break
    print(i,end=" ")
    i += 1