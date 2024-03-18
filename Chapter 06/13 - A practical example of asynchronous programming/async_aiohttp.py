"""
"비동기 프로그래밍"절 예시
aiohttp를 이용해 비동기 HTTP 호출을 수행하는 방법을 설명한다
"""
import asyncio
import time

import aiohttp

from asyncrates import get_rates

SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")


def present_result(base, rates):
    rates_line = ", ".join([f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


async def main():
    async with aiohttp.ClientSession() as session:
        for result in await asyncio.gather(
            *[get_rates(session, base) for base in BASES]
        ):
            present_result(*result)


if __name__ == "__main__":
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.time() - started

    print()
    print("time elapsed: {:.2f}s".format(elapsed))
