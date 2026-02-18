from src.assignment1.util import process_commands

def main():
    N = int(input())
    commands = []

    for _ in range(N):
        commands.append(input())

    result = process_commands(commands)
    print(result)

if __name__ == "__main__":
    main()
