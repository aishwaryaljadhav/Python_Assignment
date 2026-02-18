from src.assignment12.util import max_of_row_mins

def test_basic_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ]
    assert max_of_row_mins(matrix) == 4


def test_negative_numbers():
    matrix = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    assert max_of_row_mins(matrix) == -3

