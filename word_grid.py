from random import *
import random
from random import seed


def init():
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)



def make_grid(grid_size):
    lists = []
    row = []
    for i in range(grid_size):
        row.append(chr(randint(97, 122)))
    for i in range(grid_size):
        lists.append(row)
        row = []
        for i in range(grid_size):
            row.append(chr(randint(97, 122)))
    for list in lists:
        grid = "".join(list)
        return grid


def print_grid(grid):
    for list in grid:
        rows = ",".join(list)
        print(rows)








