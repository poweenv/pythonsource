import random
import time
import sqlite3
import datetime
words =[]

#시도횟수,정답 개수
n, cor_cnt =1,0

# with 구문 word.txt 읽어서 words 리스트에 추가
# words 출력 했을때
#['policy',....]

with open("resource/word.txt") as f:
    for w in f:
        words.append(w.strip())

#print(words)

input("Ready? Press Enter Key")
start = time.time()  # 시작 시간

while n <= 5:
    # 리스트 요소 임의로 섞기
    random.shuffle(words)
    # 리스트 요소 중 임의로 하나 추출
    q=random.choice(words)
    # 추출된 요소 화면에 출력하기
    print("Question #{}".format(n))
    print(q)
    x = input()

    print()

    if str(q).strip() == str(x).strip():
        print("pass!!")
        cor_cnt +=1 # 정답 추가
    else:
        print("Wrong!!")

    n += 1  #문제 개수 추가
# 끝난 시간
end = time.time()
# 걸린 시간
et = end - start
et = format(et,".3f")

# 게임 시간 출력
print("게임 시간 : {}초 , 정답개수 : {}".format(et,cor_cnt))
# 정답 개수가 4개이상이면 합격 출력 ,불합격
if cor_cnt >= 4:
    print("합격")
else:
    print("불합격")

#db에 저장
conn = sqlite3.connect("/source/pythonsource/resource/test.db",isolation_level=None)
cursor = conn.cursor()
cursor.execute(
    "create table if not exists records(cor_cnt integer, record text, regdate text)")

#insert 작업

now = datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
cursor.execute(
    "insert into records(cor_cnt, record, regdate) values(?,?,?)",
    (cor_cnt, et, nowDateTime),
)