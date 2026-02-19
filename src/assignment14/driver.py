from src.assignment14.util import mean_var_std

def main():
    N, M = map(int, input().split())
    matrix = []

    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    row_mean, col_var, std_dev = mean_var_std(matrix)

    print(row_mean)
    print(col_var)
    print(std_dev)

if __name__ == "__main__":
    main()
