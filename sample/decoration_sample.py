#!/usr/bin/env python3
from time import sleep

from hideout import resumable


@resumable()
def generate_large_object(times):
    sleep(10)
    result = []
    for x in range(times):
        result.append(x*2)
    return result


def cmd():
    result = generate_large_object(20)
    print(result)


if __name__ == '__main__':
    cmd()
