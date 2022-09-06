from random import *
import random
from random import seed

inputs = []
def init():
    """
    This function establishes the paramaters needed for the following function,
    along with allowing input for the paramaters and establishing random picks
    Paramaters: null (but does use user input for grid_size (number of rows of the grid)
    and seed_value which maainly allows the computer to run a random generator)
    Returns: null, but does add the grid size to a global
    variable to be used when making the grid

    """
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    inputs.append(grid_size)


def make_grid(grid_size):
    """
    This function creates the the grid, a gid_size by
    grid_size row of random intergers
    which then turn into ascii characters with sopaces inbetween
    Paramaters: the grid_size which is pulled from the gridsize
    saved in inputs
    Returns: the grid completed
    """
    lists = []
    row = []
    for i in range(grid_size):
        row.append(chr(randint(97, 122)))
    for i in range(grid_size):
        lists.append(row)
        row = []
        for i in range(grid_size):
            row.append(chr(randint(97, 122)))
    inputs.append(lists)
    for list in lists:
        grid = "".join(list)
        return grid


def print_grid(grid):
    """
    This function prints the grid of N ascii characters
    Paramaters: the grid produced by make_grid
    Returns: null, prints
    """
    for list in grid:
        rows = ",".join(list)
        print(rows.strip())


def main():
    """
    This function retrieves the paramaters needed to make
    and print the grid
    Paramaters: null
    Returns:null (prints the grid of N rows)
    """
    init()
    make_grid(inputs[0])
    print_grid(inputs[1])


main()