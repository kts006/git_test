from time import sleep
from time import time
from threading import Thread

from asyncio_ex import fib


def print_hello():
    while True:
        print("{} - Hello world!".format(int(time())))
        sleep(3)


def read_and_process_input():
    while True:
        n = int(input())
        print('fib({}) = {}'.format(n, fib.timed_fib(n)))


def main():
    # Second thread will print the hello message. Starting as a daemon means
    # the thread will not prevent the process from exiting.
    t = Thread(target=print_hello)
    t.daemon = True
    t.start()
    # Main thread will read and process input
    read_and_process_input()


if __name__ == '__main__':
    main()


