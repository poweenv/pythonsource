
class userInfo:
    """
    Author : Hong
    Date : 2023.06.21
    Description : 클래스 작성법
    """
    def __init__(self,name,age,email=None)->None:
        self.name =name
        self.age = age
        self.email = email
    
    def user_info(self):
        print("method run")
        return "name : {}, age : {}".format(self.name,self.age,self.email)

# 두 명의 객체 생성
user1 = userInfo("hong",30,"hong23@naver.com")
user2 = userInfo("kong",20)
# user_info 호출
print(user1.user_info())
print(user2.user_info())


"""
    Author : Hong
    Date : 2023.06.21
    Description : 클래스 작성법
    """


