from threading import Thread


def my_function():
    print("printing from thread")


if __name__ == "__main__":
    threads = [Thread(target=my_function) for _ in range(10)]
    print("Starting threads...\n")
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("Ending threads...")
