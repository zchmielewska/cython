import memviews
import numpy as np


arr = np.ones((10**6,), dtype=np.double)

memviews.summer(arr)
