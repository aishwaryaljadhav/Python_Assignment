from src.assignment18.util import word_statistics

def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]

    unique_count, frequencies = word_statistics(words)

    print(unique_count)
    print(*frequencies)

if __name__ == "__main__":
    main()
