from dataclasses import dataclass


@dataclass
class Vector:
    x: int
    y: int

    def __add__(self, other):
        """+ 연산자를 이용해 두 벡터를 더한다"""
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        """- 연산자를 이용해 두 벡터를 뺀다"""
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )


@dataclass(frozen=True)
class FrozenVector:
    x: int
    y: int
