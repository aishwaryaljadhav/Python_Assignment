from src.assignment2.util import calculate_average

def main():
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    result = calculate_average(student_marks, query_name)

    if result is None:
        print("Student not found")
    else:
        print(f"{result:.2f}")

if __name__ == "__main__":
    main()
