<<<<<<< HEAD
# 문제1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초
# hour, min, sec = map(int, input("시간입력 : ").split(":")) # 입력받은 개수만큼 정수로 반환
# if(hour > 12):
#     hour -= 12
#     print(f"오후 {hour:02}시 {min:02}분 {sec:02}초")
# else:
#     print(f"오전 {hour:02}시 {min:02}분 {sec:02}초")


# 문제2. 3개의 정수를 입력 받아 최대값과 최소값 구하기
# a,b,c = map(int, input("3개의 정수를 입력 : ").split(" "))
# # if a > b :
# #     if a > c : print(a)
# #     else : print(c)
# # else :
# #     if b> c : print(b)
# #     else : print(c)
#
# max_num = max(a, b, c)  #최대값
# min_num = min(a, b, c)  #최소값
# print("입력한 정수 중 최대값은", max_num, "이고 최소값은", min_num, "입니다.") #결과출력

# 문제3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
# from datetime import datetime
# curr_year = datetime.today().year
# jumin = input("주민등록번호 : ")
# gender = int(jumin[7])
# year = int(jumin[:2])
# month = int(jumin[2:4])
# day = int(jumin[4:6])
#
# if gender == 1 or gender == 2 :
#     age = curr_year - 1900 - year
# else :
#     age = curr_year - 2000 - year
#
# if gender == 1 or gender == 3 :
#     gender_str = "남성"
# else :
#     gender_str = "여성"
#
# print(f"생년월일 : {year:02}년 {month:02}월 {day:02}일")
# print(f"성별 : {gender_str}")
# print(f"나이 : {age}")


# 문제4. 갯수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기
# list 사용
score = list(map(int,input("정수 : ").split()))
print(f"총점 : {sum(score)}")
=======
# 문제1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초
# hour, min, sec = map(int, input("시간입력 : ").split(":")) # 입력받은 개수만큼 정수로 반환
# if(hour > 12):
#     hour -= 12
#     print(f"오후 {hour:02}시 {min:02}분 {sec:02}초")
# else:
#     print(f"오전 {hour:02}시 {min:02}분 {sec:02}초")


# 문제2. 3개의 정수를 입력 받아 최대값과 최소값 구하기
# a,b,c = map(int, input("3개의 정수를 입력 : ").split(" "))
# # if a > b :
# #     if a > c : print(a)
# #     else : print(c)
# # else :
# #     if b> c : print(b)
# #     else : print(c)
#
# max_num = max(a, b, c)  #최대값
# min_num = min(a, b, c)  #최소값
# print("입력한 정수 중 최대값은", max_num, "이고 최소값은", min_num, "입니다.") #결과출력

# 문제3. 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
# from datetime import datetime
# curr_year = datetime.today().year
# jumin = input("주민등록번호 : ")
# gender = int(jumin[7])
# year = int(jumin[:2])
# month = int(jumin[2:4])
# day = int(jumin[4:6])
#
# if gender == 1 or gender == 2 :
#     age = curr_year - 1900 - year
# else :
#     age = curr_year - 2000 - year
#
# if gender == 1 or gender == 3 :
#     gender_str = "남성"
# else :
#     gender_str = "여성"
#
# print(f"생년월일 : {year:02}년 {month:02}월 {day:02}일")
# print(f"성별 : {gender_str}")
# print(f"나이 : {age}")


# 문제4. 갯수가 정해지지 않은 여러개의 정수를 입력 받아 합계와 평균 구하기
# list 사용
score = list(map(int,input("정수 : ").split()))
print(f"총점 : {sum(score)}")
>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
print(f"평균 : {sum(score)/len(score)}")