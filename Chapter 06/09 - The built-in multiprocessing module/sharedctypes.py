"""
"멀티프로세싱"절 예시
sharedctype 서브모듈을 이용해 여러 프로세스 사이에서
데이터를 공유하는 방법을 설명한다.
"""
from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == "__main__":
    num = Value("d", 0.0)
    arr = Array("i", range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
