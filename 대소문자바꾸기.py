
# 대소문자 바꾸기
# 영어 소문자과 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램 작성

rst = ""
for e in input():   # 입력받는 문자열 만큼 자동 순회. 동적리스트랑 똑같이 운영이 됨.!
    if e.islower(): rst += e.upper()    #대문자
    else: rst += e.lower()    #소문자
print(rst)

r = ""
for i in input():
    if i.islower():
        r += i.upper()
    else:
        r += i.lower()
print(r)

