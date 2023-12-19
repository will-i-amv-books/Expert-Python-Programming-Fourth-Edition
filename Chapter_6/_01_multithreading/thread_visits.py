from threading import Thread

thread_visits = 0


def visit_counter():
    global thread_visits
    for _ in range(100_000):
        # value = thread_visits
        # thread_visits = value + 1
        
        """
        Ironically, when using 'thread_visits += 1', it works as if it were thread-safe,
        but it doesn't when using 'thread_visits += int(1)'. 
        Thi happens for python 3.10+, see here for more details:
        https://stackoverflow.com/questions/69993959/python-threads-difference-for-3-10-and-others
        """
        # thread_visits += 1 
        thread_visits += int(1)


if __name__ == "__main__":
    thread_count = 100
    threads = [Thread(target=visit_counter) for _ in range(thread_count)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"thread_count={thread_count}, thread_visits={thread_visits}")
