"""
"멀티프로세싱"절 예시
POSIX 시스템에서 os.fork를 이용해
새로운 프로세스를 생성하는 방법을 소개한다
"""
import os

pid_list = []


def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()

    if child_pid == 0:
        pid_list.append(os.getpid())
        print()
        print("CHLD: hey, I am the child process")
        print("CHLD: all the pids I know %s" % pid_list)

    else:
        pid_list.append(os.getpid())
        print()
        print("PRNT: hey, I am the parent ")
        print("PRNT: the child pid is %d" % child_pid)
        print("PRNT: all the pids I know %s" % pid_list)


if __name__ == "__main__":
    main()
