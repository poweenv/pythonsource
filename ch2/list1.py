#  파이썬 자료형
# 2. 리스트 (자바 배열,List 같은 계념)
#[]

#리스트 생성
list1 =[]
list2 =["a",1,3.14,True]
print(list1)
print(list2)
list3 = ["a",1,3.14,True,["b",1,34]]
print(list3)
#list4 =list(1,2,3)
#print(list4)

# 리스트 인덱싱
print(list2[0])
print(list2[2])
print(list2[-1])
print(list3[-1])
print(list3[-1][1])

#리스트 슬라이싱
print(list2[0:2])
print(list2[:-1])
print(list3[4:]) #[['b', 1, 34]]
print(list3[4]) #['b', 1, 34]
print(list3[4][:2])

list4=[1,2,["a","b",[1,2,3,4,"ldad","is"]]]
#is 문자열 
print(list4[2][2][5])
print(list4[-1][-1][-1])

# 연산자 +(연결)
a= [1,2,3]
b=[3,4,5]
print(a,b)
print(a[0]+b[1])

print(a*3)

# 리스트 특정 요소 수정
a[1] = "LiFe"
print(a)


b[1] = [10,11,12]
print(b)

del b[1]
print(b)

b[0:1] =[]
print(b)

numbers =[273,103,5,2,63,2,5,1,54,222]
for number in numbers:
    if number >= 100:
        print("100이상의 수",number)

# 273 는 3자릿수 입니다.
#103dms 3자릿수 입니다.
# 5는 1 자릿수 입니다.
for number in numbers:
    if number >= 100:
        print(number,"는 3자릿수 입니다")
    elif number < 10 :
        print(number,"는 1자릿수 입니다")

# () : 튜플
list4 =list([1,2,3])
print(list4)

# 리스트 함수
# append() : 리스트 위에 뒤에 요소 추가 
list4.append(12)
print(list4)
list4.append([6,7,8])
print(list4)

#sort(): 원본을 정렬 함
print("정렬 전",numbers)
numbers.sort()
print("정렬 후",numbers)

alpha = ["a","c","d","s","t"]
print(alpha)

alpha = ["a","C","d","S","t"]
alpha.sort()
print(alpha)

han = ["고양이","강이지","원숭이","호랑이"]
han.sort()
print(han)

numbers =[273,103,5,2,63,2,5,1,54,222]
numbers.sort(reverse=True)
print(numbers)

#reverse() : 리스트 뒤집기
han.reverse()
print("reverse 후",han)

#index(찾고자 하는 요소) : 요소가 존재하면 위치 반환
print(han[0])
print(han.index("호랑이"))
#없는 요소를 반환하려 하면 에러남

# insert(위치, 요소)
han.insert(1,"악어")
print("insert 후",han)  #insert 후 ['호랑이', '악어', '원숭이', '고양이', '강이지']
han.remove("고양이")
print("remove 후",han)

#pon() : 리스트 요소중 마지막 요소 꺼내기
a=[1,2,3,4,5,6,6,7]
print("리스트에 포함된 1의 개수",a.count(1))

#a.clear()
a.clear()
print("clear 후 : ",a)

list4 =[]
if list4:
    print("true")
else:
    print("false")

# in
print("a" in "python")

frus=["apple","emlon","banana"]

#리스트 출력
for fru in frus:
    print(fru)

# enumberate() : index 부여
for fur in enumerate(frus):
    print(fru,end=" ")

print(

)

for idx, fru in enumerate(frus,start=1):
    print(idx,fru)

# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# 70,60,52,89,48,100,25,62
# 중간고사 점수를 리스트로 생성하고, A 학급의 평균을 구하기
jums=[70,60,52,89,48,100,25,62]
total=0
for num in jums:
    total +=num
print("평균 : %.2f" % (total/ len(jums)))

#sum() 이용
print("평균 : %.2f" % (sum(jums)/ len(jums)))

# 1~20 리스트 생성: [1,2,3,4....]

list1 = list(range(1,21))
print(list1)

list3=[]
for x in range(1,101):
    list3.append(x)
print(list3)

#comprehension
list3=[x for x in range(1,101)]
print(list3)

list4 = ["갑","을","병","정","경"]
# 정을 제외하고 출력
for x in list4:
    if x !="정":
        print(x)

#
list5= [x for x in list4 if x != "정"]
print(list5)

#1~100 숫자 중에서 홀수만 리스트로 생성
list6=list(range(1,101,2))
list7=[]
for i in range(1,101,2):
    list7.append(i)
print(list7)

list8=[x for x in range(1,101,2)]
print(list8)

list9 =["A","b","d","D","e","E","S","W"]

list10 =[]
for x in list9:
    if x.islower():
        list10.append(x)
print(list10)

list10= [x for x in list9 if x.islower()]
print(list10)

# [1,2,3,4] ==> [2,4,6,8]
print([ x*2 for x in [1,2,3,4]])


#[0,1,2,3,4] =>[0,1,4,9,16]
print([ x**2 for x in [0,1,2,3,4]])

# [1,2,3], [2,3,4],[3,4,5]
# i=range(0,4)
# print([ x*i for x in [1,2,3]])

list2 =[]

for x in list1:
    list2.append([x,x+1,x+2])

print(list2)

print()

print([x,x+1,x+2] for x in list1)