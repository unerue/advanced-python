"""
"비동기 프로그래밍"절 예시
두 개의 코루틴이 블로킹 호출에 대한 이벤트 루프에서
통제를 릴리스함으로서 협업하는 방법을 설명한다.
"""
import asyncio
import random


async def waiter(name):
    for _ in range(4):
        time_to_sleep = random.randint(1, 3) / 4
        await asyncio.sleep(time_to_sleep)
        print(f"{name} waited {time_to_sleep} seconds")


async def main():
    await asyncio.gather(waiter("first"), waiter("second"))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
