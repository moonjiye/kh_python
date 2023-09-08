# 리스트의 특징
# 크기가 정해지지 않은 요소들에 대한 값을 저장하기 위한 자료형
# 아무 자료형이나 와도 된다.
# 중첩 사용이 가능하다. [[],[],[],[[[]]] ]
# 뮤터블 객체(읽고,쓰기가 가능)

number = [1,2,3,4,5,6]
fruits = ["apple","banana", "orange"]
mixed = [1, True, "seoul", 12.3456]
dup = [[1,2,3,4,5], ["apple","banana", "orange"]]

# 변수와 리스트를 비교 해보기
# kor, eng, mat = map(int, input("성적 입력 : ").split())
# print(f"합계 : {sum([kor, eng, mat])}")
#
# # 리스트, 성적의 개수에 상관없이 입력 받을 수 있음
# score = list(map(int, input("성적 입력 : ").split()))
# print(f"평균 : {sum(score)/len(score)}")


str_name = ["seoul", "gangnam", "suwon", "inchun"]
# 인덱싱
# print(str_name) # 리스트 전체 출력
# print(str_name[1])  # 1번째 요소 출력
# print(str_name[1][2]) # 1번째 요소의 2번째 문자를 출력
#
# # 슬라이싱
# slice = str_name[1:3]   #1번에서 3번 미만까지 잘라냄
# print(slice)
# print(len(slice))   # 길이 확인
# print(len(slice[0])) # 7

# primes = [2,3,5,7]
# print(primes[0])    # 2
# print(primes[-1])   # 7
# print(primes[-2:])  # [5,7]


# 리스트 연산자 : 연결(+), 반복(*), len()
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a + list_b)
# print(list_a * 3)
# print(len(list_a + list_b))


# 리스트 요소 추가하기 :
# append() : 리스트의 맨 마지막에 추가
# insert(index, 값) : 해당 인덱스에 값을 삽입
# list_a = [1,2,3]
# list_a.append(4)
# list_a.append(5)
# list_a.insert(1,10)
# print(list_a)


# 리스트 제거하기 : pop(), remove(), clear(), del() : 리스트명[index]
# pop() : 인덱스가 없으면 마지막 인덱스의 값을 반환, 인덱스가 있으면 해당 위치의 값을 삭제
# remove(값) : 해당하는 값을 제거, 만약 동일한 값이 여러개인 경우 낮은 인덱스 값을 제거
# clear() : 모든 값을 삭제, 리스트를 지우지 않음
# 반환 : 값을 보여줄지 안보여줄지의?
# list_all = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,"a","b","c","d","korea"]
# print(list_all)
# print(list_all.pop(11)) # 해당 인덱스의 값을 삭제하면서 보여줌
# print(list_all.pop())   # pop()과 같이 인덱스가 없으면 맨 마지막 값이 제거
# print(list_all.remove(2)) # 해당 값을 제거하는데 보여주지 않음 (반환값이 없음)
# print(list_all)
# del list_all[3] #해당 인덱스의 값을 지움
# print(list_all)
# list_all.clear()
# print(list_all)


# 중복 제거
# my_list = [1,2,3,4,5,6,4,8,8,7,8,4,5,5,3,1,2]
# new_list = []
# for e in my_list:
#     if e not in new_list:
#         new_list.append(e)
# print(new_list)

# int() #int함수 : 함수형 프로그래밍
# map(반환함수, 입력자료형), filter(반환함수, 입력자료형) 동작 확인
#num1 = list(map(lambda e:int(e)*int(e), input("값 : ").split()))
# num2 = list(filter(lambda e:int(e)%2==0, input("값 : ").split()))
# #print(num1)
# print(num2)


# 리스트의 원소 스캔하기
# x = ["John", "George", "Paul", "Ringo"]
# for e in x :    # 향상된 for문과 같은 형태
#     print(e)    #값이 찍힘
# print()
# for i in range(len(x)): # 범위 기반 for문(초기값, 최종값, 증감값)
#     print(x[i])
#     print(i) # range를 넣으면 인덱스값으로 접근



