from src.assignment19.util import can_stack_cubes

def test_possible_case():
    cubes = [4, 3, 2, 1, 3, 4]
    assert can_stack_cubes(cubes) == True


def test_single_cube():
    cubes = [5]
    assert can_stack_cubes(cubes) == True
