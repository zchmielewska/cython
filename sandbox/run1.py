from model import foo, bar, baz

import random
import time


def calculate(func):
    for t in range(1000):
        func(t)


if __name__ == "__main__":
    start = time.time()
    for _ in range(10_000):
        QUX = random.randint(100, 500)
        QUUX = random.randint(150, 750)

        calculate(foo)
        calculate(bar)
        calculate(baz)

        foo.cache_clear()
        bar.cache_clear()
        baz.cache_clear()
    end = time.time()
    print("Elapsed seconds:", end - start)
    # 37 seconds
