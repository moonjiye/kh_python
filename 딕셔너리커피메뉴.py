menu_dic = {
        # 딕셔너리 값:리스트
    # 메뉴이름      카테고리    가격    설명
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],    # 키와 값으로 구성되며, 값을 리스트로 만들어 여러가지 정보를 포함시킴
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}
while True :
    print("메뉴를 선택 하세요.")
    menu = input("[1] 메뉴 보기, [2] 메뉴 조회, [3] 추가 하기, [4] 삭제 하기, [5] 종료 하기 : ") # input 기본 문자열로 변환 됨
    if menu == "1":
        for key in menu_dic:
            print(key, ":", menu_dic[key])
    elif menu == "2":
        rtrv_name = input("조회 할 메뉴를 입력 하세요 : ")
        if rtrv_name in menu_dic: #딕셔너리에 키가 있는지 확인하는 조건문
            print(menu_dic[rtrv_name])
        else :
            print("찾는 메뉴가 없습니다.")
    elif menu == "3":
        add_name = input("추가 할 메뉴를 입력 하세요 : ")
        if add_name not in menu_dic:    # 포함 되어있지 않으면 추가
            category = input("카테고리 입력 : ")
            price = int(input("가격 입력 : "))
            desc = input("제품 설명 : ")
            menu_dic[add_name] = [category, price, desc] # 추가: 딕셔너리[키]=값(새로운 키와 값을 추가)
            for key in menu_dic:  # 메뉴가 추가되면 업데이트된 메뉴리스트를 다시 보여줌
                print(key, ":", menu_dic[key])
        else:
            print("메뉴가 이미 존재 합니다.")
    elif menu == "4":
        del_name = input("삭제 할 메뉴를 입력 하세요 : ")
        if del_name in menu_dic :
            del menu_dic[del_name]  # 삭제: del 딕셔너리[키] 형식
            for key in menu_dic:    # 메뉴가 삭제되면 업데이트 된 메뉴 리스트를 다시 보여줌
                print(key, ":", menu_dic[key])
        else :
            print("삭제 할 메뉴가 없습니다.")
    elif menu == "5" :
        print("영업을 종료 합니다.")
        break
    else :
        print("선택하신 메뉴가 없습니다.")