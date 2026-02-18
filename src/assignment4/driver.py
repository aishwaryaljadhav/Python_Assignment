from src.assignment4.util import mutate_string

def main():
    s = input()
    i, c = input().split()

    result = mutate_string(s, int(i), c)

    if result is None:
        print("Invalid position")
    else:
        print(result)

if __name__ == "__main__":
    main()
