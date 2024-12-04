# https://adventofcode.com/2024/day/4
import input
import re

debug = False
day = "04"
year = "2024"
filename = f"data/{year}/{day}/{'example' if debug else 'real'}.txt"
puzzle = input.read_puzzle_input(filename)

grid = puzzle.split("\n")
pattern = re.compile(r"XMAS")
total = 0


def rotate_90_degrees(grid):
    new_grid = []
    height = len(grid)
    width = max([len(row) for row in grid])
    for row_index in range(height):
        new_row = ""
        for col_index in range(width):
            old_y = height - 1 - col_index
            old_x = row_index
            new_row += grid[old_y][old_x]
        new_grid.append(new_row)
    return new_grid


def rotate_grid_diagonal(grid):
    diagonal = []
    height = len(grid)
    width = max([len(row) for row in grid])
    new_height = width + height - 1
    new_width = width
    for row_index in range(new_height):
        row = ""
        for col_index in range(new_width):
            if row_index - col_index >= 0 and row_index - col_index < height:
                row += grid[row_index - col_index][col_index]
        diagonal.append(row)
    return diagonal


# Rotate the grid 90° 4 times, check the regular grid and the +45° diagonal
# This way you do not have to convert from diagonal back to grid :)
for i in range(4):
    if i > 0:
        grid = rotate_90_degrees(grid)
    total += len(pattern.findall("\n".join(grid)))
    if debug:
        print("\n".join(grid))
        print("total:", total)
    diagonal = rotate_grid_diagonal(grid)
    total += len(pattern.findall("\n".join(diagonal)))
    if debug:
        print("\n".join(diagonal))
        print("total:", total)


print("total:", total)
