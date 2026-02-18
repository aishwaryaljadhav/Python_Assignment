import numpy as np

def floor_ceil_rint(data):
    arr = np.array(data, dtype=float)
    floor = np.floor(arr)
    ceil = np.ceil(arr)
    rint = np.rint(arr)
    return floor, ceil, rint
