<<<<<<< HEAD
# 값을 할당하는 방법
a = b = c = 1
print(a,b,c)

a, b, c = 1, False, "곰돌이"  # 여러 개의 변수를 한번에 대입
print(a,b,c)

# 타입 확인
# age = int(input("나이를 입력 하세요 : "))
# print(type(age))

# 진수
value = 0o77  # ver 3.11 부터 8진수 표현방법
print(value)

value = 0xffffff # 16진수 표현방법
print(value)

# 불리언 타입 : 참과 거짓의 값을 가짐
print(bool(1))      # True
print(bool(0))      # False
print(bool(-1000))  # True
print(bool(""))     # False
print(bool(None))   # False, 값이 정해지지 않았음을 의미
val = None



# 문자열 타입 : 인덱싱, 슬라이싱에 대한 강점?
str1 = "Hello Python!!!!"
print(str1)
print(str1[0])   # H, 인덱싱
print(str1[2:5]) # llo, 2번 인덱스에서 5번 인덱스 미만까지
print(str1[2:])  # llo Python!!!!, 2번 인덱스에서 끝까지
print(str1 * 3)  # Hello Python!!!!Hello Python!!!!Hello Python!!!!, 3번 반복 출력
print(str1 + "TEST") # Hello Python!!!!TEST, 문자열 추가


# 형변환 : 파이썬은 값이 할당되는 순간 형이 결정됨. 이후 데이터형을 변경하고자 할 때 형변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(1 + 3.141592 + float("4.44"))


=======
# 값을 할당하는 방법
a = b = c = 1
print(a,b,c)

a, b, c = 1, False, "곰돌이"  # 여러 개의 변수를 한번에 대입
print(a,b,c)

# 타입 확인
# age = int(input("나이를 입력 하세요 : "))
# print(type(age))

# 진수
value = 0o77  # ver 3.11 부터 8진수 표현방법
print(value)

value = 0xffffff # 16진수 표현방법
print(value)

# 불리언 타입 : 참과 거짓의 값을 가짐
print(bool(1))      # True
print(bool(0))      # False
print(bool(-1000))  # True
print(bool(""))     # False
print(bool(None))   # False, 값이 정해지지 않았음을 의미
val = None



# 문자열 타입 : 인덱싱, 슬라이싱에 대한 강점?
str1 = "Hello Python!!!!"
print(str1)
print(str1[0])   # H, 인덱싱
print(str1[2:5]) # llo, 2번 인덱스에서 5번 인덱스 미만까지
print(str1[2:])  # llo Python!!!!, 2번 인덱스에서 끝까지
print(str1 * 3)  # Hello Python!!!!Hello Python!!!!Hello Python!!!!, 3번 반복 출력
print(str1 + "TEST") # Hello Python!!!!TEST, 문자열 추가


# 형변환 : 파이썬은 값이 할당되는 순간 형이 결정됨. 이후 데이터형을 변경하고자 할 때 형변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(1 + 3.141592 + float("4.44"))


>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
