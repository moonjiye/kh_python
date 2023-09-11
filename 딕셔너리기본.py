# 딕셔너리 : 키와 값이 한쌍으로 이루어진 구조 (자바의 맵과 동일)
# 중괄호{} 감싸서 선언, 쉼표(,)로 구분
# 키와 값은 콜론(:)으로 구분
coffee_menu = {"Americano": 2500, "Espresso":2500, "Lattee":4000, "Moca":4500}
tea_menu = {"Black tea": 4000, "Green tea": 4000, "Milk tea":3500}
food_menu = {"Cake":5000, "Bakery":6000, "Icecream":7000}

print(coffee_menu)
print(tea_menu)
print(food_menu)
print(coffee_menu["Americano"]) # 키로 값을 확인하는 방법
print(coffee_menu.get("Lattee")) # get 메서드로 키를 넣어서 값을 확인하는 방법

# update 메서드(함수) : 딕셔너리의 데이터를 한꺼번에 변경
dict = {"곰돌이":90, "안유진":88, "장원영":77}
print(dict)
dict.update({"곰돌이":80, "안유진":98, "장원영":87})
print(dict)

# 정보 얻기 : keys(), values(), items()
dict1 = {"자바":80, "JavaScript":90, "HTML":70}
print(dict1.keys())     # 딕셔너리에 포함된 키를 확인
print(dict1.values())   # 딕셔너리에 포함된 값을 확인
print(dict1.items())    # 딕셔너리에 포함된 키와 값을 확인

# 키의 포함 여부 확인
print("HTML" in dict1)  # True, 딕셔너리에 키가 포함되어 있는지 확인
print("파이썬" in dict1)  # False
print(dict1.get("파이썬")) # 없으면 None, 있으면 키에 해당하는 값을 보여줌

# 반복문에 키를 사용해 값을 가져오기
for key in coffee_menu : # 딕셔너리를 for문으로 순회하면 요소의 키 값을 자동으로 접근할 수 있음
    #향상된 for문 단점: 무조건 끝까지, 내부값을 변경하지 못함
    print(key, ":", coffee_menu[key])