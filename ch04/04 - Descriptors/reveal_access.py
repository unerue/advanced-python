class RevealAccess(object):
    """데이터 데커레이터로 일반적으로 값을 설정하고 반환하며,
       접근에 대한 로깅 메시지를 출력한다.
    """

    def __init__(self, initval=None, name="var"):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("Updating", self.name)
        self.val = val

    def __delete__(self, obj):
        print("Deleting", self.name)


class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5


if __name__ == "__main__":
    m = MyClass()
    m.x
    m.x = 20
    m.x
    del m.x
