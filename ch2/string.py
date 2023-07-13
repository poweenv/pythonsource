# 파이썬 자료형
# 1. 자료형
# "", '', """""",''''''

# + : 결합
print("Python "+ "is fun")

# * : 복제
print("Python" *3)

print("*" * 50)
print("내 프로그램")
print("*" * 50)

# 인덱싱 : 문자열은 인덱스 값을 가지고 있음(0부터 시작)

str1 ="Life is too short"
print(str1[3])

# 슬라이싱 [시작위치 : 끝위치] => 끝 위치 포함하지 않음
print("str1[2:8]",str1[2:8])
print("str1[:6]",str1[:6]) #시작위치 지정하지 않은 경우 0
print("str1[:6]",str1[:]) #시작위치,끝나는 위치 지정하지 않은 경우 0~끝
print("str1[:-4]",str1[:-4]) # -값은 오른쪽 끝에서부터 위치를 잡는 경우 -1시작

#len(): 길이 함수
print("str1 길이",len(str1))

str2 = "20230615Sunny"
#년도, 날짜를 구별해서 변수에 담기
date = str2[0:8]
weather= str2[8:]
print(date,weather)

#date 변수에 담긴 값을 년~월~일
year = str2[0:4]
month=str2[4:6]
day = str2[6:8]
print(year+"년"+month+"월"+day+"일"+" 날씨: "+weather)

#주민 등록번호 001205-3234567
#남자(1,3) / 여자(2,4) 출력

# str3 = "001234-1234567"
# no = str3[7]

# #no 가 1 or 3  man, 2 or 4 woman
# if no == "1" or no =="3":
#     print("남")
# elif no =="2" or no =="4":
#     print("여")

# if int(no) % 2 ==1:
#     print("남")
# else:
#     print("여")

# str1= "대한민국"
# for s in str1:
#  #   print(s) # 대$한$민$국
#     print(s+"$",end="")

# 입력받은 숫자만큼 하트 출력
# 54321
# ♥♥♥♥♥
# ♥♥♥♥
# ♥♥♥
# ♥♥
# ♥

# hart = input("숫자를 입력해 주세요")
# for i in range(len(hart)):
#     for j in range(int(hart[i])):
#         print("♥",end="")
#     print()

# 문자열 관련 함수
# count 
print()
str1 = "hobby"
print("원본 문자열에 포함된 특정 문자 개수: ",str1.count("b"))
#find() : 찾을시 찾은 문자의 시작 위치 반환 , 없는 문자의 경우 -1 반환
str2 = "python is best choice"
print(str2.find("o"))
print(str2.find("k"))
print(str2.find("i",10)) # 10자리 위치부터 찾기시작
print(str2.rfind("c"))

# index() : 못찾는 경우 ValueError 발생
print(str2.index("o"))
#print(str2.index("k"))

# startswith() / endswith()
print(str2.startswith("p"))
print(str2.endswith("p"))

#join 
str3 =","
print("문자열 삽입",str3.join("abcde"))

#upper() / lower()
print("abcdef".upper())

#swapcase() : 대문자 ->소문자, 소문자-> 대문자
str4= "Python is Easy"
print(str4.swapcase())

# 대소문자 구별
print("abc" == "ABC")

# 공백제거 : 왼쪽,오른쪽,양쪽
str1="    hi     "
print(str1)
print("왼쪽 공백 제거",str1.lstrip())
str1="    hi     "
print(str1)
print("오른쪽 공백 제거",str1.rstrip())

#replace()
str1 = "Life is too short"
print("특정 문자열 변경",str1.replace("Life","Your leg"))

# split() => [](list)로 반환
print(str1.split()) #['Life','is','too','short']

a = "abcd"
print(a.split()) #['abcd']

a= "a:b:c:d"
print(a.split(":"))

a= "하나\n둘\n셋"
print(a.splitlines())#['하나','둘','셋']
print(a.split())#['하나','둘','셋']

# 문자열 구성 파악 -isdigit(),isalpha(),isalnum(),isupper(),islower()
print("12345".isdigit()) # 숫자로만 구성되어 있는가?
print("12345".isalpha()) # 알파벳로만 구성되어 있는가?
print("12345".isalnum()) # 알파벳+숫자로만 구성되어 있는가?

# 사이트별 비밀번호를 만들어 주는 프로그램
# hppts://www.naver.com

# 규칙 1 : https:// 제외 => naver.com
# 규칙 2 : 처음 나오는 . 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자개수 + 글자 내 e 개수 +! 구성
# 완성된 비밀번호 : nav51!

str1= "hppts://www.naver.com"
print(str1)

# 규칙 1 적용
# str1 = str1[12:]
str1 = str1.replace("https://www","")

#규칙 2 적용
# idx = str1.find("")
# str1 = str1[:idx]
str1 = str1[: str1.find(".")]

#규칙 3 적용
password = str1[:3] + str(len(str1)) + str(str1.count("e"))+ "!"

print(password)