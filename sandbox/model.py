from functools import lru_cache

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
