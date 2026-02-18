from src.assignment13.util import calculate_determinant

def test_basic_matrix():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    assert calculate_determinant(matrix) == -2.0

def test_identity_matrix():
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    assert calculate_determinant(matrix) == 1.0

