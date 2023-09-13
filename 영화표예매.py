TICKET_PRICE = 12000 #내부에서 변경하지 않으면 global을 따로 지정하지 않아도 사용이 가능하다/
seat = [0] * 10
#좌석 상태를 표시하는 메뉴
def print_seat(seat):   # 향상된 for문으로 좌석의 개수 만큼 순회
    for i in seat:
        if i == 0: print("[ ]", end=" ")    # 판매 안된 좌석
        else: print("[V]", end=" ")         # 판매된 좌석
    print()

# 총 매출액 구하기
def tot(seat):
    count = 0
    for i in seat:
        if i == 1: count += 1   # 팔린 좌석의 총 개수 구하기
    return count * TICKET_PRICE

# 좌석 예약 하기
def select_seat(seat):
    print_seat(seat)    # 현재 예약 가능한 좌석 보여주기
    index = int(input("좌석번호를 입력하세요: ")) - 1 # 선택된 좌석번호는 1부터 시작하고 인덱스는 0부터 시작하기 때문에 -1
    if seat[index] == 0:
        seat[index] = 1
    else:
        print("이미 예약된 좌석입니다")
    return seat

def run():
    total = 0  # 총 매출액
    seat = [0, 0, 0, 0, 0, 0, 0]
    while True:
        print("[1]예매하기")
        print("[2]종료하기")

        sel = int(input("메뉴를 선택하세요: "))
        if sel == 1:
            # 예매함수
            seat = select_seat(seat)
        else:
            # 가격출력하는 함수
            total = tot(seat)
            print("총 매출액 : {}원".format(total))
            break

run()