class Student:
    def __init__(self,name,number,grade,details) ->None:
        #생성자(오버로딩 없음)
        self.name =name
        self.number=number
        self.grade=grade
        self.details=details

    def __str_(self) ->str:

        #toString 역할

        pass

#객체 생성
student1 = Student("Kim",1,1,{"gender":"male","score1":93,"score2":54})
student2 = Student("Kim",1,1,{"gender":"male","score1":93,"score2":54})
student3 = Student("Kim",1,1,{"gender":"male","score1":93,"score2":54})

