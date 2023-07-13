# class userInfo:
#     """
#     Author : Hong
#     Date : 2023.06.21
#     Description : 클래스 작성법
#     """
#     def user_info(self):
#         print("method run")

# user1 = userInfo()
# print(user1)
# user1.user_info()

# class userInfo:
#     """
#     Author : Hong
#     Date : 2023.06.21
#     Description : 클래스 작성법
#     """
#     def __init__(self,name,age)->None:
#         self.name =name
#         self.age = age
    
#     def user_info(self):
#         print("method run")
#         return "name : {}, age : {}".format(self.name,self.age)

# # 두 명의 객체 생성
# user1 = userInfo("hong"),30
# user2 = userInfo("kong"),30
# # user_info 호출
# print(user1.user_info())
# print(user2.user_info())

#class userInfo:
"""
    Author : Hong
    Date : 2023.06.21
    Description : 클래스 작성법
    """





class userInfo:
    """
    Author : Hong
    Date : 2023.06.21
    Description : 클래스 작성법
    """
# 클래스 변수
    user_count = 0

    def __init__(self,name,age)->None:
        self.name =name
        self.age = age

        userInfo.user_count += 1    
    
    def user_info(self):
        return "name : {}, age : {}".format(self.name,self.age)
    
    def __del__(self):
        userInfo.user_count -=1

    def function1(cls):
        print("function1 호출")

    def function2(self):
        print("function2 호출")

    #객체 생성
user1 = userInfo("hong",30)
user2 = userInfo("kong",20)

#메소드 호출
print(user1.user_info)
print(user2.user_info)

#클래스 변수 확인
print("생성된 user {} 명".format(userInfo.user_count))
print("생성된 user {} 명".format(user1.user_count))

# user 삭제
del user1 # __del__ 메소드 자동으로 실행nfo.user_count))


user2.function1()
user2.function2()