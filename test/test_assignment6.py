from src.assignment6.util import print_formatted

def test_width_alignment():
    result = print_formatted(5)
    assert len(result) == 5

def test_invalid_input():
    assert print_formatted(0) == []

