# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력
# 기본방법 :
print("입력 :", end=" ")
number = list(map(int, input().split()))
even = []
odd = []
for e in number:
    if e % 2 == 0: even.append(e)
    else: odd.append(e)
print(f"홀수 : {odd}")
print(f"짝수 : {even}")

# map : 전달받은 값을 함수내부에서 가공해서 반환(입력개수와 반환개수가 동일)
# filter : 전달받은 값을 함수내부에서 조건에 일치하는것만 골라서 반환

# 람다식 방법 :
print("입력 :", end=" ")
number = list(map(int, input().split())) # 여러개의 데이터를 입력 받아서 리스트 구성
odd = list(filter(lambda x: x % 2 == 1, number))
even = list(filter(lambda x: x % 2 == 0, number))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")