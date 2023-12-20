"""
"Asynchronous programming" section example showing how
to use aiohttp to perform asynchronous HTTP calls

"""
import asyncio
import time
from typing import Dict, Tuple

from aiohttp import ClientSession as Session


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")
Rates = Dict[str, float]


async def fetch_rates(session: Session, base: str) -> Tuple[str, Rates]:
    url = f"https://api.vatcomply.com/rates?base={base}"
    async with session.get(url) as response:
        rates = (await response.json())["rates"]
        rates[base] = 1.0  # same currency exchanges to itself 1:1
        return base, rates


def present_result(base: str, rates: Rates) -> None:
    rates_line = ", ".join([
        f"{rates[symbol]:7.03} {symbol}"
        for symbol in SYMBOLS
    ])
    print(f"1 {base} = {rates_line}")


async def main():
    async with Session() as session:
        for result in await asyncio.gather(*[
            fetch_rates(session, base)
            for base in BASES
        ]):
            present_result(*result)


if __name__ == "__main__":
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))
