# https://adventofcode.com/2024/day/1
import input

puzzle = input.read_puzzle_input("data/2024/02/real.txt")
lines = puzzle.split("\n")
reports = [line.split(" ") for line in lines]
reports = [[int(digit) for digit in reports] for reports in reports]


def is_safe(report):
    difference = [report[i] - report[i + 1] for i in range(0, len(report) - 1)]
    all_positive = all([diff > 0 for diff in difference])
    all_negative = all([diff < 0 for diff in difference])
    all_gradual = all([diff in [-3, -2, -1, 1, 2, 3] for diff in difference])
    return (all_positive or all_negative) and all_gradual


def problem_dampener(report):
    difference = [report[i + 1] - report[i] for i in range(0, len(report) - 1)]
    mostly_positive = sum([diff > 0 for diff in difference]) == len(difference) - 1
    mostly_negative = sum([diff < 0 for diff in difference]) == len(difference) - 1
    sharp_jump = any([diff not in [-3, -2, -1, 1, 2, 3] for diff in difference])

    for i, diff in enumerate(difference):
        if mostly_positive:
            if diff not in [1, 2, 3]:
                a = report[:i] + report[i + 1 :]
                if is_safe(a):
                    return a
                b = report[: i + 1] + report[i + 2 :]
                return b

        if mostly_negative:
            if diff not in [-1, -2, -3]:
                a = report[:i] + report[i + 1 :]
                if is_safe(a):
                    return a
                b = report[: i + 1] + report[i + 2 :]
                return b
        if sharp_jump:
            if diff < -3 or diff > 3 or diff == 0:
                a = report[:i] + report[i + 1 :]
                if is_safe(a):
                    return a
                b = report[: i + 1] + report[i + 2 :]
                return b

    return report


total = sum(
    [
        True if is_safe(report) else is_safe(problem_dampener(report))
        for report in reports
    ]
)
print("total:", total)
