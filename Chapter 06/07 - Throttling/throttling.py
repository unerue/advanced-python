"""
"스로멀티스레드 애플리케이션 예시"절 예시
멀티스레드 애플리케이션에서 스로탈링/비율 제한을 
구현하는 방법을 소개한다
"""
import time
from queue import Queue, Empty
from threading import Thread, Lock

import requests


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")

THREAD_POOL_SIZE = 4


class Throttle:
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0
        self.last = None

    def consume(self, amount=1):
        with self._consume_lock:
            now = time.time()

            # 시간 측정은 첫 번째 토큰에 대해 초기화함으로써
            # 초기 부하를 줄인다.
            if self.last is None:
                self.last = now

            elapsed = now - self.last

            # 초과된 시간이 새로운 토큰을 추가할 만큼
            # 충분히 긴 지 확인한다
            if elapsed * self.rate > 1:
                self.tokens += elapsed * self.rate
                self.last = now

            # 버킷을 초과해서 채우지 않는다	
            self.tokens = min(self.rate, self.tokens)

            # 마지막으로 가능한 경우 토큰을 보낸다
            if self.tokens >= amount:
                self.tokens -= amount
                return amount

            return 0


def fetch_rates(base):
    response = requests.get(f"https://api.vatcomply.com/rates?base={base}")

    response.raise_for_status()
    rates = response.json()["rates"]
    # 노트: 동일 화폐는 1:1로 환전한다
    rates[base] = 1.0
    return base, rates


def present_result(base, rates):
    rates_line = ", ".join([f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


def worker(work_queue, results_queue, throttle):
    while not work_queue.empty():
        try:
            item = work_queue.get_nowait()
        except Empty:
            break

        while not throttle.consume():
            time.sleep(0.1)

        try:
            result = fetch_rates(item)
        except Exception as err:
            results_queue.put(err)
        else:
            results_queue.put(result)
        finally:
            work_queue.task_done()


def main():
    work_queue = Queue()
    results_queue = Queue()
    throttle = Throttle(10)

    for base in BASES:
        work_queue.put(base)

    threads = [
        Thread(target=worker, args=(work_queue, results_queue, throttle))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()

    while not results_queue.empty():
        result = results_queue.get()
        if isinstance(result, Exception):
            raise result

        present_result(*result)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started

    print()
    print("time elapsed: {:.2f}s".format(elapsed))
