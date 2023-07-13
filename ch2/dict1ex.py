# 딕셔너리 생성하기
# "A" =90 "b" =80 "c" =70 등급을 딕셔너리로 생성하기

dict3 ={"A" :90, "B" :80, "C" :70}

# B 키에 해당하는 값 출력하기
print(dict3["B"])
print(dict3.get("B"))
# B 키 값을 삭제한 후 딕셔너리 출력하기
del dict3["B"]
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

    