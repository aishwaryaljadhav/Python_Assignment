from src.assignment16.util import probability_at_least_one_a

def main():
    n = int(input())
    letters = input().strip()
    k = int(input())

    result = probability_at_least_one_a(n, letters, k)
    print(result)

if __name__ == "__main__":
    main()
