import numpy as np
from src.assignment11.util import floor_ceil_rint

def test_basic_numbers():
    data = [1.1, 2.5, 3.9]
    floor_exp = np.array([1., 2., 3.])
    ceil_exp = np.array([2., 3., 4.])
    rint_exp = np.array([1., 2., 4.])

    floor_res, ceil_res, rint_res = floor_ceil_rint(data)

    np.testing.assert_array_equal(floor_res, floor_exp)
    np.testing.assert_array_equal(ceil_res, ceil_exp)
    np.testing.assert_array_equal(rint_res, rint_exp)


def test_negative_numbers():
    data = [-1.2, -2.8, 0.5]
    floor_exp = np.array([-2., -3., 0.])
    ceil_exp = np.array([-1., -2., 1.])
    rint_exp = np.array([-1., -3., 0.])

    floor_res, ceil_res, rint_res = floor_ceil_rint(data)

    np.testing.assert_array_equal(floor_res, floor_exp)
    np.testing.assert_array_equal(ceil_res, ceil_exp)
    np.testing.assert_array_equal(rint_res, rint_exp)
