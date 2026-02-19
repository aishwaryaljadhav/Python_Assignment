import numpy as np

def mean_var_std(matrix):
    arr = np.array(matrix, dtype=float)
    row_mean = np.mean(arr, axis=1)
    col_var = np.var(arr, axis=0)
    std_dev = round(np.std(arr), 11)
    return row_mean, col_var, std_dev
