from threading import Thread


def my_function():
    print("printing from thread")


if __name__ == "__main__":
    thread = Thread(target=my_function)
    print("Starting thread...")
    thread.start()
    thread.join()
    print("Ending thread...")
