def summer(double[:] mv):
    cdef:
        double ss = 0.0
        int i, N

    N = mv.shape[0]
    for i in range(N):
        ss += mv[i]
    return ss
