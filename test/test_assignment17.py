from src.assignment17.util import calculate_happiness

def test_basic_case():
    arr = [1, 5, 3]
    A = {3, 1}
    B = {5, 7}
    assert calculate_happiness(arr, A, B) == 1

