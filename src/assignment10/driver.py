from src.assignment10.util import time_delta

def main():
    t = int(input())

    for i in range(t):
        t1 = input().strip()
        t2 = input().strip()

        result = time_delta(t1, t2)
        print(result)

if __name__ == "__main__":
    main()
