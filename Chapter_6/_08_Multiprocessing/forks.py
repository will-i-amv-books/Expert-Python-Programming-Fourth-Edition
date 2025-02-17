"""
"Multiprocessing" section example showing how
to spawn new process using os.fork on POSIX
systems.

"""
import os

pid_list = []


def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()
    if child_pid == 0:
        pid_list.append(os.getpid())
        print()
        print("CHLD: hey, I am the child process")
        print(f"CHLD: all the pids I know: {pid_list}")

    else:
        pid_list.append(os.getpid())
        print()
        print("PRNT: hey, I am the parent ")
        print(f"PRNT: the child pid is {child_pid}")
        print(f"PRNT: all the pids I know: {pid_list}")


if __name__ == "__main__":
    main()
