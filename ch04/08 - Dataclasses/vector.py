class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+ 연산자를 이용해 두 벡터를 더한다"""
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        """- 연선자를 이용해 두 벡터를 뺀다"""
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __repr__(self):
        """벡터의 텍스트 표현을 반환한다"""
        return f"<Vector: x={self.x}, y={self.y}>"

    def __eq__(self, other):
        """두 백터의 동일 여부를 비교한다"""
        return self.x == other.x and self.y == other.y
