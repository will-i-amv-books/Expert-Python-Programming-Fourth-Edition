"""
"Asynchronous programming" section example showing
how to employ `futures` and threading/multiprocessing
to use non-async libraries in asyncio-based applications

"""
import asyncio
import time
from typing import Dict, Tuple

import requests

SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")
THREAD_POOL_SIZE = 4
Rates = Dict[str, float]


async def fetch_rates(base: str) -> Tuple[str, Rates]:
    url = f"https://api.vatcomply.com/rates?base={base}"
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None, # Executor defaults to ThreadPoolExecutor 
        requests.get, # Function to execute 
        url # Args of function
    )
    response.raise_for_status()
    rates = response.json()["rates"]
    rates[base] = 1.0  # same currency exchanges to itself 1:1
    return base, rates


def present_result(base: str, rates: Rates) -> None:
    rates_line = ", ".join([
        f"{rates[symbol]:7.03} {symbol}"
        for symbol in SYMBOLS
    ])
    print(f"1 {base} = {rates_line}")


async def main():
    for result in await asyncio.gather(*[
        fetch_rates(base) 
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
