"""피보나치 수열 함수를 제공하는 파이썬 모듈"""


def fibonacci(n):
    """피보나치 수열의 n번째 요소를 재귀적으로 계산해서 반환한다."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
