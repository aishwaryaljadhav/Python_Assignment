from src.assignment6.util import print_formatted

def main():
    n = int(input())
    lines = print_formatted(n)

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
