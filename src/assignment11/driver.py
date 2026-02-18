from src.assignment11.util import floor_ceil_rint
import numpy as np

def main():
    np.set_printoptions(legacy='1.13')

    data = input().split()
    floor, ceil, rint = floor_ceil_rint(data)

    print(floor)
    print(ceil)
    print(rint)

if __name__ == "__main__":
    main()
