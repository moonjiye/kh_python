# import math #math 모듈을 사용하기 위해서 import 합
# print(math.sin(1))
import math
# 모듈 내에 함수(메서드) 특정한 함수만 가져오고자 하는 경우
from math import sin, cos, tan  # 3개만 골라서 import, 그외는 사용x?
print(sin(1))
print(cos(1))
print(tan(1))

# 모듈을 가져올 때 충돌이나 긴 이름을 간결하게 사용하기 위해 별칭 부여 (별칭을 부여하면 원래 이름은 사용 안됨)
import math as m
print(m.sin(1))
print(m.sin(1))

# sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈 입니다.
import sys
print("명령 줄 인수 : ", sys.argv)
print("실행 경로 : ", sys.path[0])
sys.stdout.write("Hello, world!!!\n")