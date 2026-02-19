from src.assignment19.util import can_stack_cubes

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))

        if can_stack_cubes(cubes):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
