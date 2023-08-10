from model import foo, bar, baz

import cy_test

import random
import time


def main():
    for _ in range(10_000):
        QUX = random.randint(100, 500)
        QUUX = random.randint(150, 750)

        cy_test.calculate_cpp(foo)
        cy_test.calculate_cpp(bar)
        cy_test.calculate_cpp(baz)

        foo.cache_clear()
        bar.cache_clear()
        baz.cache_clear()


if __name__ == "__main__":
    import cProfile
    cProfile.run("main()", sort="time")
