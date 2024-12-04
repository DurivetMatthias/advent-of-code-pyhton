# https://adventofcode.com/2024/day/4
import input
import re

debug = False
day = "04"
year = "2024"
filename = f"data/{year}/{day}/{'example' if debug else 'real'}.txt"
puzzle = input.read_puzzle_input(filename)

grid = puzzle.split("\n")
height = len(grid)
width = max([len(row) for row in grid])


def create_emtpy_grid():
    empty_grid = []
    for _ in range(height):
        empty_grid.append(["."] * width)
    return empty_grid


linked_grid = create_emtpy_grid()
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        linked_char = {
            "value": char,
            "y": y,
            "x": x,
        }
        linked_grid[y][x] = linked_char


def create_emtpy_grid():
    empty_grid = []
    for _ in range(height):
        empty_grid.append(["."] * width)
    return empty_grid


def reconstruct_linked_grid():
    reconstructed_linked_grid = create_emtpy_grid()
    for row in linked_grid:
        for linked_char in row:
            reconstructed_linked_grid[linked_char["y"]][linked_char["x"]] = linked_char
    return reconstructed_linked_grid


def rotate_90_degrees(grid):
    new_grid = []
    height = len(grid)
    width = max([len(row) for row in grid])
    for row_index in range(height):
        new_row = []
        for col_index in range(width):
            old_y = height - 1 - col_index
            old_x = row_index
            new_row.append(grid[old_y][old_x])
        new_grid.append(new_row)
    return new_grid


def rotate_grid_diagonal(grid):
    diagonal = []
    height = len(grid)
    width = max([len(row) for row in grid])
    new_height = width + height - 1
    new_width = width
    for row_index in range(new_height):
        row = []
        for col_index in range(new_width):
            if row_index - col_index >= 0 and row_index - col_index < height:
                row.append(grid[row_index - col_index][col_index])
        diagonal.append(row)
    return diagonal


def grid_to_strings(grid):
    new_grid = []
    for row in grid:
        line = ""
        for linked_char in row:
            line += linked_char["value"]
        new_grid.append(line)
    return new_grid


def print_grid(grid, *, title=None):
    if debug:
        if title:
            print(title)
        for row in grid:
            line = ""
            for linked_char in row:
                line += linked_char["value"]
            print(line)
        print()


# Using the rotation functions from part 1
# Rotate the grid 90° twice, create their +45° diagonal counterparts
# Remove all the A's that are not part of a diagonal MAS or SAM, these can never form an X-MAS
# Finally, count the amount of A's in the final grid, this is will be the amount of X-MASes

# However, becasue we don't maintain the diagonal grid, we can not directly modify the letters
# Solution: Transform the items to LinkedList Items, then we can easily recover the original grid

for i in range(2):
    if i % 2 != 0:
        linked_grid = rotate_90_degrees(linked_grid)
    print_grid(linked_grid, title="Before rotation")
    linked_diagonal = rotate_grid_diagonal(linked_grid)
    print_grid(linked_diagonal, title="After rotation")
    stringified_diagonal = grid_to_strings(linked_diagonal)
    for line_index, line in enumerate(stringified_diagonal):
        valid_a_positions = []
        # Find MAS
        for group in re.finditer(string=line, pattern=r"MAS"):
            a_index = group.start() + 1
            valid_a_positions.append(a_index)
        # Find SAM
        for group in re.finditer(string=line, pattern=r"SAM"):
            a_index = group.start() + 1
            valid_a_positions.append(a_index)
        for char_index, char in enumerate(line):
            if char == "A":
                if char_index not in valid_a_positions:
                    linked_diagonal[line_index][char_index]["value"] = "."
    print_grid(linked_diagonal, title="After Removing invalid A's")

reconstructed_linked_grid = reconstruct_linked_grid()
print_grid(reconstructed_linked_grid, title="Reconstructed grid")
for row in reconstructed_linked_grid:
    for linked_char in row:
        if linked_char["value"] != "A":
            linked_char["value"] = "."

print_grid(reconstructed_linked_grid, title="Final grid")

stringified_grid = grid_to_strings(reconstructed_linked_grid)
total = "".join(stringified_grid).count("A")
print("total:", total)
