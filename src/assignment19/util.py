from collections import deque

def can_stack_cubes(cubes):
    cubes = deque(cubes)
    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            chosen = cubes.popleft()
        else:
            chosen = cubes.pop()

        if chosen <= last:
            last = chosen
        else:
            return False

    return True
