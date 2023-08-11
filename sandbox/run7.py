from model import foo, bar, baz

import cy_calculate4

import random
import time


def main():
    v1 = cy_calculate4.Variable(foo)
    v2 = cy_calculate4.Variable(bar)
    v3 = cy_calculate4.Variable(baz)


    for _ in range(10_000):
        QUX = random.randint(100, 500)
        QUUX = random.randint(150, 750)

        cy_calculate4.calculate(v1)
        cy_calculate4.calculate(v2)
        cy_calculate4.calculate(v3)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Elapsed seconds:", end-start)
    # 82 seconds
