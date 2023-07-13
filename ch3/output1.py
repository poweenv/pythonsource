# 파일 입출력

# 파일 출력
#f= open("파일 경로,"모드")
#파일관련 작업
#.................
#종료
#f.close()

with open("resource/test1.txt","w") as f:

#resoruce 폴더에 test1.ext 파일생성
# f = open("../resource/test1.txt","w")

# f.write("Helo Python")
# f.close
# f = open("resource/test1.txt","w",encoding="utf-8")

# f.write("안녕하세요\n반갑습니다")
# f.close
# f = open("resource/test1.txt","w",encoding="utf-8")
# for i in range(1,11):
#     data = "%d 번\n" % i
#     f.write(data)
# # f.close
# f = open("resource/test1.txt","a",encoding="utf-8")
# for i in range(1,11):
#     data = "안녕하세요\n"
#     f.write(data)
# f.close

# list1 = ["hong\n","kom\n","hom\n"]
# # test2.txt 에 리스트 안의 문자 작성
# f= open("resource/test2.txt","w",encoding="utf-8")
# f.writelines(list1)
# f.close()

dict1 = {"name":"hong","age":25,"addr":"seoul"}
# test3.txt
# name : hong
#age : 25
# addr : seoul

# f= open("resource/test3.txt","w",encoding="utf-8")
# for k,v in dict1.items():
#     f.write("{} : {}\n".format(k,v))

import random

hangules = list("가나다라마바사아자차카타파하")
#print(hangules)
#print(random.choice(hangules))

f=open("resource/info.txt","w",encoding="utf-8")
for i in range(1000):
    name =random.choice(hangules) + random.choice(hangules)
    weight = random.randrange(40,100)
    height = random.randrange(140,190)
    f.write("{}, {}, {}\n".format(name,weight,height))
f.close()














