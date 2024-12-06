# https://adventofcode.com/2024/day/6
import input

debug = False
day = "06"
year = "2024"
filename = f"data/{year}/{day}/{'example' if debug else 'real'}.txt"
puzzle = input.read_puzzle_input(filename)

grid = puzzle.split("\n")
width = max([len(line) for line in grid])
height = len(grid)
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"
WALL = "#"
guard = {
    "x": None,
    "y": None,
    "direction": UP,
    "steps": 0,
    "out_of_bounds": False,
    "visited": [],
}
for y, line in enumerate(grid):
    x = line.find(UP)
    if x != -1:
        guard["x"] = x
        guard["y"] = y
        break


def get_next():
    x = guard["x"]
    y = guard["y"]
    direction = guard["direction"]
    if direction == UP:
        y -= 1
    elif direction == DOWN:
        y += 1
    elif direction == LEFT:
        x -= 1
    elif direction == RIGHT:
        x += 1
    if x < 0 or x >= width or y < 0 or y >= height:
        guard["out_of_bounds"] = True
        return {
            "x": guard["x"],
            "y": guard["y"],
        }
    return {
        "x": x,
        "y": y,
    }


def turn_right():
    direction = guard["direction"]
    if direction == UP:
        guard["direction"] = RIGHT
    elif direction == RIGHT:
        guard["direction"] = DOWN
    elif direction == DOWN:
        guard["direction"] = LEFT
    elif direction == LEFT:
        guard["direction"] = UP


def step():
    next_position = get_next()
    if grid[next_position["y"]][next_position["x"]] == WALL:
        turn_right()
        next_position = get_next()

    guard["x"] = next_position["x"]
    guard["y"] = next_position["y"]
    guard["steps"] += 1
    guard["visited"].append((guard["x"], guard["y"]))


while not guard["out_of_bounds"]:
    step()

distinct_locations = set(guard["visited"])
print("total:", len(distinct_locations))
