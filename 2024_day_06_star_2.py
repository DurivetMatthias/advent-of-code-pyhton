# https://adventofcode.com/2024/day/6
import input

debug = False
day = "06"
year = "2024"
filename = f"data/{year}/{day}/{'example' if debug else 'real'}.txt"
puzzle = input.read_puzzle_input(filename)
original_grid = puzzle.split("\n")
width = max([len(line) for line in original_grid])
height = len(original_grid)
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"
WALL = "#"

for y, line in enumerate(original_grid):
    x = line.find(UP)
    if x != -1:
        guard_start_x = x
        guard_start_y = y
        break


def get_next(guard):
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


def turn_right(guard):
    direction = guard["direction"]
    if direction == UP:
        guard["direction"] = RIGHT
    elif direction == RIGHT:
        guard["direction"] = DOWN
    elif direction == DOWN:
        guard["direction"] = LEFT
    elif direction == LEFT:
        guard["direction"] = UP


def step(guard, grid):
    next_position = get_next(guard)
    while grid[next_position["y"]][next_position["x"]] == WALL:
        turn_right(guard)
        next_position = get_next(guard)

    guard["x"] = next_position["x"]
    guard["y"] = next_position["y"]
    guard["steps"] += 1
    guard["visited"].append((guard["y"], guard["x"]))


def simulate(grid):
    guard = {
        "x": guard_start_x,
        "y": guard_start_y,
        "direction": UP,
        "steps": 0,
        "out_of_bounds": False,
        "visited": [(guard_start_y, guard_start_x)],
    }
    distinct_trajectories = set([(guard["y"], guard["x"], guard["direction"])])
    previous = 0
    current = len(distinct_trajectories)
    while not guard["out_of_bounds"] and previous != current:
        previous = current
        step(guard, grid)
        distinct_trajectories.add((guard["y"], guard["x"], guard["direction"]))
        current = len(distinct_trajectories)
    return guard


total = 0
original_guard = simulate(original_grid)
visited_positions = original_guard["visited"]

unique_locations = set()

for index, visited_position in enumerate(set(visited_positions)):
    y, x = visited_position
    if x == guard_start_x and y == guard_start_y:
        continue
    new_grid = original_grid.copy()
    new_grid[y] = new_grid[y][:x] + WALL + new_grid[y][x + 1 :]
    new_guard = simulate(new_grid)
    if not new_guard["out_of_bounds"]:
        unique_locations.add((y, x))
        if debug:
            new_grid[y] = new_grid[y][:x] + "O" + new_grid[y][x + 1 :]
            for visited_position in new_guard["visited"]:
                y, x = visited_position
                new_grid[y] = new_grid[y][:x] + "+" + new_grid[y][x + 1 :]
            print("\n".join(new_grid))
            print()

print("total:", len(unique_locations))
