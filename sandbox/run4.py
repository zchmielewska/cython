from cy_model import foo, bar, baz

import random
import time


if __name__ == "__main__":
    start = time.time()
    for _ in range(10_000):
        QUX = random.randint(100, 500)
        QUUX = random.randint(150, 750)

        for t in range(1000):
            foo(t)
            bar(t)
            baz(t)

        foo.cache_clear()
        bar.cache_clear()
        baz.cache_clear()
    end = time.time()
    print("Elapsed seconds:", end - start)
    # 13 seconds
