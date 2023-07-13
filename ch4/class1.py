# class

# 학생 3 명의 정보(이름,학년, 반,성별, 과목 점수) 저장

student_name_1 = "kim"
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {"gender" : "male"},
    {"score" : 95},
    {"score2" : 1},
]
student_name_2 = "sim"
student_number_2 = 1
student_grade_2 = 2
student_detail_2 = [
    {"gender" : "female"},
    {"score" : 95},
    {"score2" : 11},
]
student_name_3 = "jim"
student_number_3 = 1
student_grade_3 = 3
student_detail_3 = [
    {"gender" : "male"},
    {"score" : 5},
    {"score2" : 91},
]


# 출력

print("name : ",student_name_1,"학년 : %d",student_grade_1)
print("name : {}, 학년 : {}, 반 : {},학생정보 :{}"
      .format(student_name_1,student_number_1,student_grade_1,student_detail_1))


student_name_list= ["kim","sim","jim"]
student_grade_list= [2,1,3]
student_number_list= [1,2,3]
student_number_list= [
    {"gender" : "male","score":91,"score2":20},
    {"gender" : "male","score":91,"score2":20},
    {"gender" : "male","score":91,"score2":20},
]

# print(
#     "name" : {}, "학년" : {}, "class" : {},"stuInfo" :{}.format(
#         student_name_list[1],
#         student_grade_list[1],
#         student_number_list[1],
#         student_detail_list[1],
#     )
# )