from src.assignment1.util import process_commands

def test_basic_operations():
    commands = [
        "append 1",
        "append 2",
        "insert 1 3",
        "remove 2"
    ]
    assert process_commands(commands) == [1, 3]


def test_sort_reverse():
    commands = [
        "append 5",
        "append 1",
        "append 3",
        "sort",
        "reverse"
    ]
    assert process_commands(commands) == [5, 3, 1]
