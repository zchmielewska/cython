from functools import lru_cache
import random

QUX = 1
QUUX = 1


@lru_cache()
def foo(x):
    if x == 0:
        return QUX
    return foo(x - 1) - bar(x)


@lru_cache()
def bar(x):
    if x == 0:
        return 0
    return QUUX - baz(x)


@lru_cache()
def baz(x):
    if x == 0:
        return 0
    return foo(x - 1) * 0.01


def main():
    for _ in range(10_000):
        QUX = random.randint(100, 500)
        QUUX = random.randint(150, 750)

        for x in range(1000):
            foo(x)
            bar(x)
            baz(x)

        foo.cache_clear()
        bar.cache_clear()
        baz.cache_clear()
