from model import foo, bar, baz

import cy_calculate2

import random
import time


def main():
    for _ in range(10_000):
        QUX = random.randint(100, 500)
        QUUX = random.randint(150, 750)

        cy_calculate2.calculate(foo)
        cy_calculate2.calculate(bar)
        cy_calculate2.calculate(baz)

        foo.cache_clear()
        bar.cache_clear()
        baz.cache_clear()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed seconds:", end-start)
    # 44 seconds
