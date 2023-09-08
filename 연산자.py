<<<<<<< HEAD
# 산술연산자 : 사칙연산자(+,-,*,/) //(몫), **(제곱연산자), %(나머지 연산자)
i = 10  # 값을 대입할 때 데이터 형이 결정됨, 왜냐면 파이썬은 데이터형이 없음 (키워드X)
j = 3
# 변수를 집어넣으려면 f 선언
print(f"덧셈 : {i+j}")
print(f"뺄셈 : {i-j}")
print(f"곱셉 : {i*j}")
print(f"나눗셈 : {i/j}")
print(f"몫 : {i//j}")
print(f"나머지 : {i%j}")
print(f"제곱연산 : {i**j}")

test = "Python !!!"
print(test + "Hello")   # 문자열, 문자를 더함. 문자열과 숫자는 더할 수 없다.
print(test + str(100))
print(test * 3)         # test 문자열을 3번 반복하겠다는 의미
i += 1  # 파이썬은 증감 연산자가 없음.
print(f"증감연산자 : {i}") # 파이썬에서는 증감연산자가 없다. 값을 지정하는 수식을 넣을 수 없다.

# 간단 예제 : 파이썬은 변수를 상수로 만드는 방법은 없으며, 관례상 변수 이름을 모두 대문자로 표시하면 상수로 간주
# TAX_RATE = 0.10
# income = int(input("당신의 수입이 얼마입니까? "))
# print(f"당신이 내야할 세금은 {income * TAX_RATE:.2f} 입니다.")
'''
# 파이썬은 상수가 없기  때문에 값을 변경할 수 있다.
# 상수를 쓰려면 이름을 가지고 명시. 아니면 튜플(리스트)을 써야한다.
# 값을 읽고 쓰기가 가능,
'''

# 관계 연산자 : AND(&&) => and, OR(||) => or, NOT(!) => not
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y      # False
rst2 = x > 0 or x > y       # True
rst3 = not(x > 0 or x > y)  # False
print(rst1, rst2, rst3, sep="\t")   # 구분자

# 다항(삼항) 연산자 : 조건문에 사용할 수 있는 Switch 대신 사용
num = int(input("정수 입력 : "))
rst = (num % 2 == 0) and "짝수" or "홀수"
# (조건식)? (참):(거짓) => ? 대신 and, : 대신 or 을 사용함.
# 람다식 표현 : e => (e % 2 == 0) and "짝수" or "홀수"
print(f"{num}은 {rst}입니다.")

# 2진수 입력 받기 (0b)
number = 0b101010101
# 8진수 입력 받기 (0o)
number = 0o1234567
# 16진수 입력 받기 (0x)
=======
# 산술연산자 : 사칙연산자(+,-,*,/) //(몫), **(제곱연산자), %(나머지 연산자)
i = 10  # 값을 대입할 때 데이터 형이 결정됨, 왜냐면 파이썬은 데이터형이 없음 (키워드X)
j = 3
# 변수를 집어넣으려면 f 선언
print(f"덧셈 : {i+j}")
print(f"뺄셈 : {i-j}")
print(f"곱셉 : {i*j}")
print(f"나눗셈 : {i/j}")
print(f"몫 : {i//j}")
print(f"나머지 : {i%j}")
print(f"제곱연산 : {i**j}")

test = "Python !!!"
print(test + "Hello")   # 문자열, 문자를 더함. 문자열과 숫자는 더할 수 없다.
print(test + str(100))
print(test * 3)         # test 문자열을 3번 반복하겠다는 의미
i += 1  # 파이썬은 증감 연산자가 없음.
print(f"증감연산자 : {i}") # 파이썬에서는 증감연산자가 없다. 값을 지정하는 수식을 넣을 수 없다.

# 간단 예제 : 파이썬은 변수를 상수로 만드는 방법은 없으며, 관례상 변수 이름을 모두 대문자로 표시하면 상수로 간주
# TAX_RATE = 0.10
# income = int(input("당신의 수입이 얼마입니까? "))
# print(f"당신이 내야할 세금은 {income * TAX_RATE:.2f} 입니다.")
'''
# 파이썬은 상수가 없기  때문에 값을 변경할 수 있다.
# 상수를 쓰려면 이름을 가지고 명시. 아니면 튜플(리스트)을 써야한다.
# 값을 읽고 쓰기가 가능,
'''

# 관계 연산자 : AND(&&) => and, OR(||) => or, NOT(!) => not
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y      # False
rst2 = x > 0 or x > y       # True
rst3 = not(x > 0 or x > y)  # False
print(rst1, rst2, rst3, sep="\t")   # 구분자

# 다항(삼항) 연산자 : 조건문에 사용할 수 있는 Switch 대신 사용
num = int(input("정수 입력 : "))
rst = (num % 2 == 0) and "짝수" or "홀수"
# (조건식)? (참):(거짓) => ? 대신 and, : 대신 or 을 사용함.
# 람다식 표현 : e => (e % 2 == 0) and "짝수" or "홀수"
print(f"{num}은 {rst}입니다.")

# 2진수 입력 받기 (0b)
number = 0b101010101
# 8진수 입력 받기 (0o)
number = 0o1234567
# 16진수 입력 받기 (0x)
>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
number = 0xffffff