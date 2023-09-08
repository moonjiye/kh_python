# 1번 : 초급, 상근날드
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류
# 입력 : 연속해서 3종의 햄버거, 2종의 음료 가격 입력
# 출력 : 햄버거 3종 중 가장 싼 메뉴 + 음료 2종 중 싼거 - 50원 한 결과 값

# ls = []
# for i in range(0, 5):
#     ls.append(int(input()))
# buger = min(ls[:3])
# drink = min(ls[3:5])
# print(f"{buger + drink - 50}")


# 2번 : 중급, 저항
# 입력 : 3개의 저항값 입력
# 저항에 대한 색상
# 첫번째 색상은 10의 자리수, 두번째 수는 1의 자리수, 세번째 자리수는 곱해야 하는 수

# color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# f_name = color.index(input()) #input() 으로 입력 받은 문자열이 color 튜플내의 인덱스로 반환
# s_name = color.index(input())
# t_name = color.index(input())
# print(int(str(f_name) + str(s_name)) * (10 ** t_name))

# 3번 : 중급, PC방 알바
# 1 ~ 100번까지의 컴퓨터가 있음
# 손님은 자신이 앉고 싶어하는 자리를 선택하고자 합니다. 이미 예약된 자리는 선택할 수 없으므로
# seat_num = list(map(int, input().split()))
# pc = [0] * 100 # 0으로 초기화된 100개의 리스트 생성. 리스트한개를 100개 곱해서 100개의 방이 만들어짐.
# cnt = 0
# for e in seat_num: # 향상된 for문이므로 e값은 고객이 앉고 싶어하는 좌석 번호
#         if pc[e-1] != 0: cnt += 1
#         else :pc[e-1] = 1     # 손님이 해당 좌석을 선택한 경우, 배열을 -1 해준 이유는 현실세계랑은 다르기때문ㅇ
# print(cnt) # 거절된 횟수

# 4번 : Knuth-Morris-Pratt => KMP, Mirko-Slavko => MS
upper_str = ""
for e in input() : # 입력받은 개수만큼 자동 순회
        if e.isupper() : upper_str += e
print(upper_str)