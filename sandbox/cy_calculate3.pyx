import ctypes
from cython.parallel import prange

ctypedef double (* someFunctionPointer) (double tt) nogil

ftype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)


cpdef void calculate(func):
    f = ftype(func)

    cdef:
        int t

    for t in prange(1000, nogil=True):
        with gil:
            f(t)
