from src.assignment16.util import probability_at_least_one_a

def test_basic_case():
    n = 4
    letters = "aabc"
    k = 2

    result = probability_at_least_one_a(n, letters, k)
    assert round(result, 3) == 0.833

