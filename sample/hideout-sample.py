#!/usr/bin/env python3
from time import sleep

import hideout


def generate_large_object(times):
    sleep(10)
    result = []
    for x in range(times):
        result.append(x*2)
    return result


def cmd():
    result = hideout.resume_or_generate(
        func=generate_large_object,
        func_args={"times": 10}
    )
    print(result)


if __name__ == '__main__':
    cmd()
