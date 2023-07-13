# csv 읽기
import csv #python 에서 csv 모듈

# with open("resource/sample1.csv","r") as f:
#     content = csv.reader(f)
#     print(content)
#     print(dir(content))
#     print(type(content))


#     next(content) # 헤더명 제거
#     for c in content:
#         print(c)

# with open("resource/sample2.csv","r") as f:
#     content = csv.reader(f,delimiter="!")

#     next(content) # 헤더명 제거
#     for c in content:
#         print(c)
# with open("resource/sample2.csv","r") as f:
#     content = csv.DictReader(f,delimiter="!")

#     next(content) # 헤더명 제거
#     for c in content:
#         print(c)
with open("resource/sample3.csv","r") as f:
    content = csv.reader(f)

    for row in content:
        for i in row:
            print(i, end="")
        print()


# csv 쓰기
data = [[1,2,3],[1,2,3],[13,22,31],[14,23,32],[11,21,31]]

with open("resource/sample5.csv","w",newline="") as f:
    wt = csv.writer(f)

    # for v in data:
    #     wt.writerow(v)
    wt.writerows(data)