from src.assignment7.util import generate_logo

def main():
    thickness = int(input())
    lines = generate_logo(thickness)

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
