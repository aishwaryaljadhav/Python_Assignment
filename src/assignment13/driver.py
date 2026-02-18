from src.assignment13.util import calculate_determinant

def main():
    N = int(input())
    matrix = []

    for i in range(N):
        row = list(map(float, input().split()))
        matrix.append(row)

    result = calculate_determinant(matrix)
    print(result)

if __name__ == "__main__":
    main()
