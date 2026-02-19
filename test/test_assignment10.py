from src.assignment10.util import time_delta

def test_sample_case_1():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
    assert time_delta(t1, t2) == 25200


