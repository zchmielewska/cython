ctypedef int calk

cdef class MyClass:
    cdef:
        int value

    cpdef int squared(self)

