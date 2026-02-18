from src.assignment9.util import calculate_average

def test_average_calculation():
    n = 3
    columns = ["ID", "NAME", "MARKS"]
    students = [
        ["1", "Aish", "50"],
        ["2", "B", "60"],
        ["3", "C", "70"]
    ]

    assert calculate_average(n, columns, students) == 60.00


def test_missing_column():
    n = 2
    columns = ["ID", "NAME"]
    students = [["1", "A", "50"], ["2", "B", "60"]]

    assert calculate_average(n, columns, students) is None
