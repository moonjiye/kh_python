print("Hello, world")
# ", ' 구분안함.
print(100)
print(33.33)
print(100+23)

# 변수를 선언하고 값을 대입
num=100 # 데이터형은 값이 대입되는 순간에 결정된다.
print(num)
num = "100" # 정수형에서 문자열로 바뀜
"""
여기는 범위 주석 구간 입니다.
"""

# 변수 활용
name = "곰돌이 사육사"
email = ("mjy6088@naver.com")
age = 25
addr = "서울시 강남구 역삼동 KH정보교육언"
print(f"""
""")

print(f"""
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}
""")

# 파이썬은 불리언 값이 대문자로 시작
isAdult = True
if isAdult :
    print("나는 성인 입니다.")
else :
    print("나는 성인이 아닙니다")

"""
    작성자 : 곰돌이
    수정날짜 : 2023.09.06
"""
print([1, 2, 3]) # 리스트 출력