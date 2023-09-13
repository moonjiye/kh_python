# 고정비용 :1000
# 가변비용 :70
# 판매비용 :170
fix, var, sell = map(int, input().split())
cnt=0
while True:
    if cnt >fix // (sell - var) : break
    cnt += 1
print(cnt)


# 손익분기를 도달할 수 없는경우
if sell <= var : print(-1)
else: print(fix //(sell - var)+1)