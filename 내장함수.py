# 내장함수 : 파이썬이 기본적으로 제공, import가 필요없음
# # 외장함수 : 파이썬이 기본적으로 제공, import가 필요함

# # 큰 값, 작은 값 찾기
# print(max(1,2,3,434,5,56,6,7,889))
# print(min(1,2,3,434,5,56,6,7,889))

# # 총합 구하기
# print(sum([1,2,3,434,5,56,6,7,889]))    # 리스트에 대한 총합
# print(sum((1,2,3,434,5,56,6,7,889)))    # 튜플에 대한 총합
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력 받은 수의 총합 : {sum(num)}")
# print(f"입력 받은 수의 평균 : {sum(num)/len(num)}")

# # 몫과 나머지 구하기
# print(f"몫과 나머지 : {divmod(10,4)}")   # 튜플의 동작원리, 두개의 반환값으로 받음

# 여러개의 값을 한번에 입력 받아 리스트로 만들기
# 최대값, 최솟값, 합계, 평균, 몫과 나머지
# num1 = list(map(int, input("정수값 입력 : ").split()))
# print(f"최대값 : {max(num1)}")
# print(f"최솟값 : {min(num1)}")
# print(f"합계 : {sum(num1)}")
# print(f"평균 : {sum(num1)/len(num1)}")
# print(f"몫과 나머지 : {divmod(sum(num1),5)}")

# 정렬
my_list = [1,2,3,434,5,56,6,7,889]
print(sorted(my_list, reverse=True))    #내림차순 정렬
print(sorted(my_list))  #오름차순 정렬