# python startup file
import atexit
import os

try:
    import readline
except ImportError:
    print("Completion unavailable: readline module not available")
else:
    import rlcompleter

    # 탬 완성
    readline.parse_and_bind("tab: complete")

    # 사용자의 홈 디렉터리에 대한 히스토리 파일 경로.
    # 사용자 경로를 이용해도 좋다.
    history_file = os.path.join(os.environ["HOME"], ".python_shell_history")
    try:
        readline.read_history_file(history_file)
    except IOError:
        pass

    atexit.register(readline.write_history_file, history_file)
    del os, history_file, readline, rlcompleter
