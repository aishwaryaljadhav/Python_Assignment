from src.assignment8.util import finding_day

def test_known_date():
    assert finding_day(8, 8, 2021) == "SUNDAY"


def test_invalid_date():
    assert finding_day(2, 30, 2021) is None
