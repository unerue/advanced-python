"""
"멀티프로세싱"절 예시
`multiprocessing` 모듈의 파이프를
커뮤니케이션 채널로 이용하는 방법을 설명한다.
"""
from multiprocessing import Process, Pipe


class CustomClass:
    pass


def worker(connection):
    while True:
        instance = connection.recv()
        if instance:
            print(f"CHLD: recv: {instance}")
        if instance is None:
            break


def main():
    parent_conn, child_conn = Pipe()

    child = Process(target=worker, args=(child_conn,))

    for item in (
        42,
        "some string",
        {"one": 1},
        CustomClass(),
        None,
    ):
        print("PRNT: send: {}".format(item))
        parent_conn.send(item)

    child.start()
    child.join()


if __name__ == "__main__":
    main()
