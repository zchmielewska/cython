from cython.parallel import prange

cpdef void calculate(func):
    cdef:
        int t

    for t in prange(1000, nogil=True):
        with gil:
            func(t)
