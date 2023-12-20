import time
from multiprocessing.pool import Pool as ProcessPool, ThreadPool
from typing import Dict, Tuple

import requests


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")
POOL_SIZE = 4
Rates = Dict[str, float]


def fetch_rates(base: str) -> Tuple[str, Rates]:
    response = requests.get(f"https://api.vatcomply.com/rates?base={base}")
    response.raise_for_status()
    rates = response.json()["rates"]
    rates[base] = 1.0 # same currency exchanges to itself 1:1
    return base, rates


def present_result(base: str, rates: Rates) -> None:
    rates_line = ", ".join([
        f"{rates[symbol]:7.03} {symbol}"
        for symbol in SYMBOLS
    ])
    print(f"1 {base} = {rates_line}")


def main(use_threads=False):
    if use_threads:
        pool_cls = ThreadPool
    else:
        pool_cls = ProcessPool
    with pool_cls(POOL_SIZE) as pool:
        results = pool.map(fetch_rates, BASES)
    for result in results:
        present_result(*result)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))
