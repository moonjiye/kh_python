# 기존에 없는 연산을 하고 싶을때 좌변과 우변에 모르는 데이터 타입이 올때
class Vector2D:
    pass


class Vector2D :
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other): # +연산자에 대응된다.나랑 다른 누군가를 비교
        return Vector2D(self.x + other.x, self.y+other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y*other.y)

    v1 = Vector2D(1,2)
    v2 = Vector2D(3,4)

    print(100 * 200)
    print(100.1 * 200.1)
    v3=v1 * v2
    print(v3.x,v3.y)