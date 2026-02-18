from src.assignment8.util import finding_day

def main():
    month, day, year = map(int, input().split())

    result = finding_day(month, day, year)

    if result is None:
        print("Invalid date")
    else:
        print(result)

if __name__ == "__main__":
    main()
