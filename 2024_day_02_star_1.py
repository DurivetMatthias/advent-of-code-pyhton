# https://adventofcode.com/2024/day/2
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


total = sum([is_safe(report) for report in reports])
print("total:", total)
