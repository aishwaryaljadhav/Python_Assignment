from src.assignment12.util import max_of_row_mins

def main():
    rows, cols = map(int, input().split())
    data = []

    for i in range(rows):
        row = list(map(int, input().split()))
        data.append(row)

    result = max_of_row_mins(data)
    print(result)

if __name__ == "__main__":
    main()
