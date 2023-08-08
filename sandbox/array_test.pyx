ctypedef double (*f_type)(int)


cpdef double[1000] calculate_cpp(f_type func):
    cdef:
        double result[1000]
        int t

    for t in range(1000):
        result[t] = func(t)

    return result
