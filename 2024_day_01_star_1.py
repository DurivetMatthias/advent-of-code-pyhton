# https://adventofcode.com/2024/day/1
import input
import re

puzzle = input.read_puzzle_input("data/2024/01/real.txt")
lines = puzzle.split("\n")
pattern = re.compile(r"(\d*)\s\s\s(\d*)")
left_list = [pattern.match(line).group(1) for line in lines]
right_list = [pattern.match(line).group(2) for line in lines]

total = 0
for pair in zip(sorted(left_list), sorted(right_list)):
    total += abs(int(pair[0]) - int(pair[1]))

print("total:", total)
