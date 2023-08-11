from model import foo, bar, baz

import cy_calculate3

import random
import time


def main():
    for _ in range(10_000):
        QUX = random.randint(100, 500)
        QUUX = random.randint(150, 750)

        cy_calculate3.calculate(foo)
        cy_calculate3.calculate(bar)
        cy_calculate3.calculate(baz)

        foo.cache_clear()
        bar.cache_clear()
        baz.cache_clear()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed seconds:", end-start)
    # 76 seconds
