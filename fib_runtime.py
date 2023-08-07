import fib
import timeit


def fib_python(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = a + b, a

    return a


x = timeit.repeat(setup="from fib import fib",
                  stmt="fib(1000)",
                  repeat=1,
                  number=100000)
print(x)

y = timeit.repeat(setup="from __main__ import fib_python",
                  stmt="fib_python(1000)",
                  repeat=1,
                  number=100000)
print(y)
