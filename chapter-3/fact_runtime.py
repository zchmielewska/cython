import fact
import timeit


def interpreted_fact(n):
    if n <= 1:
        return 1
    return n * interpreted_fact(n - 1)


x = timeit.repeat(setup="from fact import wrap_c_fact",
                  stmt="wrap_c_fact(100)",
                  repeat=1,
                  number=10000)
print("wrap_c_fact", x)

x = timeit.repeat(setup="from fact import py_fact",
                  stmt="py_fact(100)",
                  repeat=1,
                  number=10000)
print("py_fact", x)

x = timeit.repeat(setup="from __main__ import interpreted_fact",
                  stmt="interpreted_fact(100)",
                  repeat=1,
                  number=10000)
print("interpreted_fact", x)
