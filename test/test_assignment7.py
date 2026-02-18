from src.assignment7.util import generate_logo

def test_invalid_thickness():
    assert generate_logo(4) == []  


def test_valid_thickness():
    result = generate_logo(3)
    assert len(result) > 0
