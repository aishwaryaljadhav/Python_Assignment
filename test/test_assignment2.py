from src.assignment2.util import calculate_average

def test_calculate_average_basic():
    student_marks = {
        "Aishwarya": [80, 90, 100],
        "Rahul": [70, 60, 75]
    }

    assert calculate_average(student_marks, "Aishwarya") == 90.00
    assert calculate_average(student_marks, "Rahul") == 68.33


def test_student_not_found():
    student_marks = {
        "Aishwarya": [80, 90, 100]
    }

    assert calculate_average(student_marks, "Unknown") is None
