<<<<<<< HEAD
# 회원 정보 출력 하기 (1단계는 현재 상태대로 -> 함수형태로)

### 함수표현 ###
def input_age():
    while True:
        age = input("나이 입력 : ")
        if age.isdigit():
            age = int(age)
            if 0 < age < 200: return age
        print("나이를 잘못 입력하셨습니다.")


def input_gender():
    while True:
        gender = input("성별 입력 : ")
        if gender == 'M' or gender == 'm':
            return "남성"
        elif gender == 'F' or gender == 'f':
            return "여성"
        print("성별이 잘못 입력하셨습니다.")


def input_jobs():
    while True:
        jobs = input("직업 [1]학생, [2]회사원 [3]주부 [4]무직 : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업이 잘못 입력되었습니다.")


def print_info(name, age, gender, jobs):
    jobs_str = ("", "학생", "회사원", "주부", "무직")
    print("=" * 3, "회원정보", "=" * 3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"


# 함수는 선언 이후 호출해야 동작함.
member_info = "member.txt"
fd = open(member_info, "a" , encoding="utf-8")
while True:
    name = input("이름 입력 (종료하려면 quit) : ")
    if name == 'quit': break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name, age, gender, jobs)
    fd.write(rst + '\n')
fd.close()


# name = input("이름 입력 : ")
# while True:
#     age = input("나이 입력 : ")
#     if age.isdigit():   # 문자열이 숫자로 구성되어 있는지 확인
#         age = int(age)
#         if 0 < age < 200: break
#     print("나이를 잘못 입력하셨습니다.")
# while True:
#     gender = input("성별 입력 : ")
#     if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f': break
#     print("성별이 잘못 입력하셨습니다.")
# while True:
#     jobs = input("직업 [1]학생, [2]회사원 [3]주부 [4]무직 : ")
#     if jobs.isdigit():
#         jobs = int(jobs)
#         if 0 < jobs < 5: break
#     print("직업이 잘못 입력되었습니다.")
# if gender == 'M' or gender == 'm': gen_str = "남성"
# else: gen_str = "여성"
# jobs_str = ("", "학생", "회사원", "주부", "무직")    #튜플사용, 고정된 문자열을 출력하기 위함
# # 리스트와 튜플 차이 : 이미 만들어진 데이터를 넣음(튜플)
# # 튜플은 ()가 있던 없던 데이터가 있으면 자동적으로 인식을 함.
#
# print(f"""이름 : {name}
# 나이 : {age}
# 성별 : {gen_str}
# 직업 : {jobs_str[jobs]}
# """)
=======
name = input("이름 입력 : ")
while True:
    age = int(input("나이 입력 : "))
    if 0 < age < 200: break
while True:
    gender = input("성별 입력 : ")
    if gender == 'M' or gender == 'm': break
    elif gender == 'F' or gender == 'f': break
    else: continue
while True:
    job = int(input("직업 [1]학생, [2]회사원 [3]주부 [4]무직 : "))
    if 0 < job < 5: break
    print("직업이 잘못 입력되었습니다. 다시 입력해주세요.")
if gender == 'M' or gender == 'm': gen_name = "남성"
else: gen_name = "여성"
jobs_name = ("", "학생", "회사원", "주부", "무직")
print("="*3, "회원정보", "="*3)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_name}")
print(f"직업 : {jobs_name[job]}")
>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
