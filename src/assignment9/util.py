def calculate_average(n, columns, students):
    try:
        marks_index = columns.index("MARKS")
    except ValueError:
        return None

    total = 0

    for student in students:
        total += int(student[marks_index])

    return round(total / n, 2)
