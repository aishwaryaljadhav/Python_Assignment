from src.assignment4.util import mutate_string

def test_basic_mutation():
    assert mutate_string("hello", 1, "a") == "hallo"


def test_invalid_position():
    assert mutate_string("python", 10, "z") is None
