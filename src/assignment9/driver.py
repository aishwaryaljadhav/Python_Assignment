from src.assignment9.util import calculate_average

def main():
    n = int(input())
    columns = input().split()

    students = []
    for _ in range(n):
        students.append(input().split())

    result = calculate_average(n, columns, students)

    if result is None:
        print("Invalid data")
    else:
        print(result)

if __name__ == "__main__":
    main()
