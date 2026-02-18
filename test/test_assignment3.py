from src.assignment3.util import find_runner_up

def test_runner_up_basic():
    arr = [2, 3, 6, 6, 5]
    assert find_runner_up(arr) == 5


def test_runner_up_with_duplicates():
    arr = [1, 1, 1, 2, 2, 3]
    assert find_runner_up(arr) == 2



