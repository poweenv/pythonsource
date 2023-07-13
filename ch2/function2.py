# 람다 함수
# 단일문으로 표현되는 익명함수
# 코드 상에서 한번만 사용이 되는 상황일 때


# def square(x):
#     return x *x

# print(square(5))

square = lambda x: x *x 
print(square)

add = lambda a, b: a*b
print(add(5,6))

def str_len(s):
    return len(s)
strings = ["bob","charles","alexander","teddy"]
strings.sort(key=str_len)
print(strings)

strings.sort(key=lambda s:len(s))
print(strings)

even_list=[]

def even(arr):
    for n in arr:
        if n % 2 ==0:
            even_list.append(n)

list1  =[1,2,3,4,5,6,7,8,9]
even(list1)
print(even_list)

even_list2 = [n for n in list1 if n % 2 ==0]
print(even_list2)

def even2(n):
    return n % 2 ==0


print(list(filter(even2,list1)))


def mul(x):
    return x==2

nums= [1,2,3,4,5,6,7,8,9,10]


#map(함수,리스트)
print(list(map(mul,nums)))

print(list(map(lambda x: x**2,nums)))

nums =list(range(1,11))  # 1~10 리스트 생성


#3의 배수만  문자열로 변경한 리스트 반환 ~ str()
#[,1,2,'3',4,5,'6',7,8,'9',10]
nums_result = []

def str_check(nums):

    #리스트 안의 요소가 3의 배수인 경우 문자로 변환

    for i in nums:
        if i % 3 ==0:
            nums_result.append(str(i))
        else:
            nums_result.append(i)

    return nums_result

print(nums_result)


def str_check2(i):
    if i % 3 ==0:
        return str(i)
    else:
        return i

print(list(map(str_check2,nums)))

print(list(map(lambda i:str(i)if i % 3 ==0 else i,nums)))


