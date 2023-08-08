ctypedef int calk

cdef class MyClass:
    cdef:
        int value

    def __cinit__(self, v):
        self.value = v

    def doubled(self):
        return self.value + self.value

    cpdef int squared(self):
        return self.value * self.value


