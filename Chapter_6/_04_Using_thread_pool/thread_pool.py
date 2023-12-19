"""
"An example of a threaded application" section example
showing how to implement simple thread pool.

"""
import time
from queue import Queue, Empty
from threading import Thread

import requests


THREAD_POOL_SIZE = 4
SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")


def fetch_rates(base: str) -> None:
    response = requests.get(f"https://api.vatcomply.com/rates?base={base}")
    response.raise_for_status()
    rates = response.json()["rates"]
    rates[base] = 1.0  # same currency exchanges to itself 1:1
    rates_line = ", ".join([
        f"{rates[symbol]:7.03} {symbol}"
        for symbol in SYMBOLS
    ])
    print(f"1 {base} = {rates_line}")


def worker(work_queue: Queue) -> None:
    while not work_queue.empty():
        try:
            item = work_queue.get_nowait() # Get item in non-blocking mode.
        except Empty:
            break
        else:
            fetch_rates(item)
            work_queue.task_done() # Mark item as processed


def main():
    work_queue = Queue()
    for base in BASES:
        work_queue.put(base)
    threads = [
        Thread(target=worker, args=(work_queue,))
        for _ in range(THREAD_POOL_SIZE)
    ]
    for thread in threads:
        thread.start()
    work_queue.join() # Waits until all items have been processed
    while threads:
        threads.pop().join() # Waits for all threads to finish


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))
