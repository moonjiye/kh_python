<<<<<<< HEAD
# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원
n = int(input())    # 통화 횟수
call = list(map(int, input().split()))  # 통화 횟수에 대한 통화 시간
#list 크기를 알 수 없기 때문에 list 사용, split():빈공간이면 공백기준으로 갖게됨.
y_pay = m_pay = 0
for i in range(n):
    y_pay += (call[i] // 30) * 10 + 10
    m_pay += (call[i] // 60) * 15 + 15
if y_pay > m_pay: print("M", m_pay)
elif y_pay < m_pay: print("Y", y_pay)
=======
n = int(input())
call = list(map(int, input().split()))
y_pay = m_pay = 0
for i in range(n):
    y_pay += (call[i] // 30) * 10 + 10
    m_pay += (call[i] // 60) * 15 + 15
if y_pay > m_pay: print("M", m_pay)
elif y_pay < m_pay: print("Y", y_pay)
>>>>>>> 8a553a3510317d5b1ea59d726f8a4de62c9c22d6
else: print("Y M", y_pay)