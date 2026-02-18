import numpy as np

def calculate_determinant(matrix):
    arr = np.array(matrix, dtype=float)
    det = np.linalg.det(arr)
    return round(det, 2)
