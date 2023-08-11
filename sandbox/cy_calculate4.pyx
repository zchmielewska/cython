import ctypes
from cython.parallel import prange


ftype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)


cdef class Variable:
    cdef f

    def __cinit__(self, func):
        self.f = ftype(func)

    cdef calculate(self, int t):
        return self.f(t)



cpdef void calculate(Variable v):
    cdef:
        int t

    for t in prange(1000, nogil=True):
        with gil:
            v.calculate(t)
