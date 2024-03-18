"""
"비동기 프로그래밍"절 예시
numbers 수열을 비동기 출력하는 간단한 예시다.
"""
import asyncio
import random


async def print_number(number):
    await asyncio.sleep(0)
    print(number)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(
        asyncio.gather(*[print_number(number) for number in range(10)])
    )
    loop.close()
