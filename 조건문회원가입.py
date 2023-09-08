<<<<<<< HEAD
# 회원가입을 위한 아이디와 패스워드 입력 받기
user = input("아이디 입력 : ")
if len(user) >= 8 : # 입력 받은 아이디의 길이가 8과 같거나 커야함.
    pw = input("비밀번호 입력 : ")
    #if pw.__len__() < 8 or pw.__len__() > 16: #내부함수 이용
    if len(pw) < 8 or len(pw) > 16:   #외부함수 이용
        print("비밀번호는 8자 에서 16자 사이여야 합니다.")
    elif pw.find(user) >= 0:
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else:
=======
# 회원가입을 위한 아이디와 패스워드 입력 받기
user = input("아이디 입력 : ")
if len(user) >= 8 : # 입력 받은 아이디의 길이가 8과 같거나 커야함.
    pw = input("비밀번호 입력 : ")
    #if pw.__len__() < 8 or pw.__len__() > 16: #내부함수 이용
    if len(pw) < 8 or len(pw) > 16:   #외부함수 이용
        print("비밀번호는 8자 에서 16자 사이여야 합니다.")
    elif pw.find(user) >= 0:
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else:
>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
    print("아이디는 반드시 8자리 이상 이어야 합니다.")