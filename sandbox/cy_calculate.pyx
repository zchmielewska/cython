cpdef void calculate(func):
    cdef:
        int t

    for t in range(1000):
        func(t)