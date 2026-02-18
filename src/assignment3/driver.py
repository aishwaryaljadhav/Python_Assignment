from src.assignment3.util import find_runner_up

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    result = find_runner_up(arr)

    if result is None:
        print("Not enough unique scores")
    else:
        print(result)

if __name__ == "__main__":
    main()
