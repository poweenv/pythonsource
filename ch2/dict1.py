# # 파이썬 자료형
# # 4. 딕셔너리 (자바의 Map 동일 : key, value)
# # {} 사용

# # key 값은 str, int 가능
# # value 값은 str,int,list,tuple,dict

dict1 ={"name":"park","age":12}
# print(dict1)

# #특정 키에 해당하는 value 출력
# print(dict1["name"])
# print(dict1["age"])
# #print(dict1["addr"]) keyerror:'addr'

dict2 ={0: "Hello Python",1: "Hello Java"}
# print(dict2)
# print(dict2[0])

# dict3={"arr":[1,2,3,4]}
# print(dict3)
# print(dict3["arr"])

# #요소 추가
dict1["birth"]="0616"
# print(dict1)

dict2[2] = ["Hello Spring","Hello JSP"]
# print(dict2)

# dict3["rank"]=(16,17,18)
# print(dict3)

# # 각 숫자가 몇 개씩 나오는지 구한 후 딕셔너리 생성
# # {1:3, 2:4, 3:6}
# numbers = {1,2,3,4,5,6,5,5,6,5,4,8,7,9,5,4,1,2,2,5,8,8,}

# # 비어 있는 dict 생성
# # counter =[]
# # #counter[1]=3
# # for number in numbers:
# #     counter[number] =numbers.count(number)

# # print(counter)

# # 요소 삭제
# print(dict1)
# del dict1["birth"]
# print(dict1)

# #함수
# #get(키값)
# print(dict1.get("name"))
# print(dict1.get("addr"))

#keys : 키값 가져오기
print(dict1.keys())

#values()
print(dict1.values()) #dict_values(['park',12])

#itens() : key_values 쌍으로 가져오기
print(dict1.items()) #dict_items([('name','park'),('age',12)])

#in
print("name" in dict1) #true
print(4 in dict2) #false

my_info = {"name":"kim","age":35,"city":"seoul"}

for k in my_info.keys():
    print(k)


for v in my_info.values():
    print(v)


for k, v in my_info.items():
    print(k,v)

info = (v for v in my_info.values())

print(info)

info = (v for v in my_info.values())

print(info)

info = {((k,v) for k,v in my_info.items())}

# 딕셔너리 생성하기
# "A" =90 "b" =80 "c" =70 등급을 딕셔너리로 생성하기

dict3 ={"A" :90, "B" :80, "C" :70}

# B 키에 해당하는 값 출력하기
print(dict3["B"])
# B 키 값을 삭제한 후 딕셔너리 출력하기

# 성인 : 10000, 청소년 : 7000, 아동 : 3000 데이터를 딕셔너리 생성

person = {"성인" : 10000, "청소년" : 7000, "아동" : 3000}

# 위 딕셔너리에 소아 : 0항목 추가
person["소아"]=0
# 키 값만 출력하기
for p in person.keys():
    print(p)
# values 값만 출력하기
for p in person.values():
    print(p)


#list(),tuple()
print(list(dict2.keys()))
print(tuple(dict2.keys())) # <class 'dict1'>

# key,value 전부 지우기
dict1.clear()
print(dict1)