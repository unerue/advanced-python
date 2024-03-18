"""
"멀티프로세싱"절 예시
`multiprocessing` 모듈을 이용해 새로운 프로세스들을
생성하는 방법을 설명한다.
"""
from multiprocessing import Process
import os


def work(identifier):
    print(f'Hey, I am the process ' f'{identifier}, pid: {os.getpid()}')


def main():
    processes = [Process(target=work, args=(number,)) for number in range(5)]
    for process in processes:
        process.start()

    while processes:
        processes.pop().join()


if __name__ == "__main__":
    main()
