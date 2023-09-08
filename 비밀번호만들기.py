<<<<<<< HEAD
# 각 사이트 비밀번호 만들기
# 규칙1 : http://naver.com 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점 이후 제거
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자에 포함된 'o'의 개수 + 글자에 포함된 'k'의 개수 + "1" + 자신의 이니셜
file_name = "password.txt"
fd = open(file_name, "wt")  # 파일 접근 식별자
while True :
    url = input("사이트 : ")
    if url == 'exit': break    # 탈출조건
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱, 처음부터 "." 인덱스 미만, 5
    password = (my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "mjy")
    print("비밀번호 : " + password)
    fd.write(password + "\n")   # 있는그대로 출력해버리기 때문에 \n필요
fd.close()

=======
# 각 사이트 비밀번호 만들기
# 규칙1 : http://naver.com 앞의 http:// 잘라내기
# 규칙2 : 처음 만나는 점 이후 제거
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자에 포함된 'o'의 개수 + 글자에 포함된 'k'의 개수 + "1" + 자신의 이니셜
file_name = "password.txt"
fd = open(file_name, "wt")  # 파일 접근 식별자
while True :
    url = input("사이트 : ")
    if url == 'exit': break    # 탈출조건
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")]  # 슬라이싱, 처음부터 "." 인덱스 미만, 5
    password = (my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "mjy")
    print("비밀번호 : " + password)
    fd.write(password + "\n")   # 있는그대로 출력해버리기 때문에 \n필요
fd.close()

>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
