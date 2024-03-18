from random import shuffle
from cffi import FFI

ffi = FFI()

ffi.cdef("""
void qsort(void *base, size_t nel, size_t width,
int (*compar)(const void *, const void *));
""")
C = ffi.dlopen(None)


@ffi.callback("int(void*, void*)")
def cffi_int_compare(a, b):
    # 콜백 시그니처는 타입이 정확하게 일치해야 한다.
    # ctypes 보다는 적은 마술을 필요로 하지만,
    # 보다 구체적이어야 하며, 보다 명시적인
    # 캐스팅을 해야 한다.
    int_a = ffi.cast('int*', a)[0]
    int_b = ffi.cast('int*', b)[0]
    print(" %s cmp %s" % (int_a, int_b))

    # qsort 명세에 따라 이는 다음을 반환한다:
    # * 0 미만의 값, if a < b
    # * 0, if a == b
    # * 0 초과의 값, if a > b
    return int_a - int_b


def main():
    numbers = list(range(5))
    shuffle(numbers)
    print("shuffled: ", numbers)
    
    c_array = ffi.new("int[]", numbers)

    C.qsort(
        # 정렬된 배열에 대한 포인터
        c_array,
        # 배열의 길이
        len(c_array),
        # 배열의 개별 요소의 크기
        ffi.sizeof('int'),
        # 콜백(C 해당 함수에 대한 포인터)
        cffi_int_compare,
    )
    print("sorted: ", list(c_array))


if __name__ == "__main__":
    main()