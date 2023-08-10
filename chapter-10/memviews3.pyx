from cython import boundscheck, wraparound

def summer(double[:] mv):
    cdef:
        double ss = 0.0
        int i, N

    N = mv.shape[0]
    with boundscheck(False), wraparound(False):
        for i in range(N):
            ss += mv[i]

    return ss
