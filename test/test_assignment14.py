from src.assignment14.util import mean_var_std
import numpy as np

def test_basic_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    row_mean, col_var, std_dev = mean_var_std(matrix)

    np.testing.assert_array_almost_equal(row_mean, np.array([2.,5.]))
    np.testing.assert_array_almost_equal(col_var, np.array([2.25,2.25,2.25]))
    assert round(std_dev, 11) == 1.70782512766

