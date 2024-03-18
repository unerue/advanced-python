from random import shuffle

import ctypes
from ctypes.util import find_library

libc = ctypes.cdll.LoadLibrary(find_library("c"))

CMPFUNC = ctypes.CFUNCTYPE(
    # 반환 타입
    ctypes.c_int,
    # 첫 번째 인수 타입
    ctypes.POINTER(ctypes.c_int),
    # 두 번째 인수 타입
    ctypes.POINTER(ctypes.c_int),
)


def ctypes_int_compare(a, b):
    # 인수는 포인터이므로 [0] 인덱스를 이용해 접근한다.
    print(" %s cmp %s" % (a[0], b[0]))

    # qsort 명세에 따라 이는 다음을 반환한다:
    # * 0 미만의 값, if a < b
    # * 0, if a == b
    # * 0 초과의 값, if a > b
    return a[0] - b[0]


def main():
    numbers = list(range(5))
    shuffle(numbers)
    print("shuffled: ", numbers)

    # numbers 리스트의 길이와 동일한 길이의 배열을
    # 나타내는 새로운 타입을 생성한다
    NumbersArray = ctypes.c_int * len(numbers)
    # 새로운 타입을 이용해 새로운 C 배열을 생성한다
    c_array = NumbersArray(*numbers)

    libc.qsort(
        # 정렬된 배열에 대한 포인터
        c_array,
        # 배열의 길이
        len(c_array),
        # 배열의 개별 요소의 크기
        ctypes.sizeof(ctypes.c_int),
        # 콜백(C 해당 함수에 대한 포인터)
        CMPFUNC(ctypes_int_compare),
    )
    print("sorted:   ", list(c_array))


if __name__ == "__main__":
    main()
