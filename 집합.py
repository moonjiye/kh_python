# 집합이란 ? 주로 중복제거를 목적으로 자주 사용 됩니다.
# 순서가 보장되지 않음
# 중복 불가
# mutable 특성을 가짐

# s1 = set([1,2,3,4,5])
# s2 = set([4,5,6,7,8])
#
# # 중복 제거
# s3 = set([1,2,3,4,5,6,2,3,4,5])
# print(s3)
#
# # 교집합 : 집합에서 양쪽 모두에 존재하는 요소만 선택
# print(s1.intersection(s2))
# print(s1 & s2)
#
# # 합집합 : 집합에서 한군데만 존재하면 포함됨, 중복제거
# print(s1.union(s2))
# print(s1 | s2)
#
# # 차집합 : 집합에서 앞에서 뒤를 빼서 남은 앞의 요소만 선택
# print(s1.difference(s2))
# print(s1 - s2)

import random
numbers = set()
while True :
    number = random.randrange(1, 46)
    numbers.add(number)
    if len(numbers) == 6 : break;

print(numbers)

#함수는 동작기능만 가짐. 상태를 이해할 필요는 없음, 결과에 대한 출력만
#객체는 값을 저장, 함수형 값을 가지지 않음, 객체와 함수