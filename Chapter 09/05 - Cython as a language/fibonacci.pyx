"""피보나치 수열 함수를 제공하는 파이썬 모듈"""


cdef long long fibonacci_cc(unsigned int n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_cc(n - 1) + fibonacci_cc(n - 2)


def fibonacci(unsigned int n):
    """피보나치 수열의 n번째 요소를 재귀적으로 계산해서 반환한다.
    """
    with nogil:
        result = fibonacci_cc(n)

    return fibonacci_cc(n)
