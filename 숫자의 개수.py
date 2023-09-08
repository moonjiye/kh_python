<<<<<<< HEAD
# 숫자의 개수
# A = 150, B = 266, C = 427 이라면, A x B x C = 150 x 266 x 427 = 17037300

a, b, c = map(int, input("정수 3개 입력 : ").split())
total_val = str(a * b * c)  # a*b*c 결과를 문자열 변환
for i in range(10) :
    print(total_val.count(str(i)))

=======
a, b, c = map(int, input("정수 3개 입력 : ").split())
mul = str(a * b * c)
for i in range(10) :
    print(mul.count(str(i)))

>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
