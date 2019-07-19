import asyncio
import sys
from time import time, sleep
from asyncio_ex import fib


def process_input():
    text = sys.stdin.readline()
    n = int(text.strip())
    print('fib({}) = {}'.format(n, fib.timed_fib(n)))


def time_loop():
    while True:
        print("aaa")
        sleep(3)


@asyncio.coroutine
def print_hello():
    while True:
        print("{} - Hello world!".format(int(time())))
        yield from asyncio.sleep(3)


def main():
    loop = asyncio.get_event_loop()
    loop.add_reader(sys.stdin, process_input)
    loop.add_reader(sys.stdout, time_loop)
    loop.run_until_complete(print_hello())


if __name__ == '__main__':
    main()
