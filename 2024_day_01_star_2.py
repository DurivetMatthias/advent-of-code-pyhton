# https://adventofcode.com/2024/day/1
import input
import re

puzzle = input.read_puzzle_input("data/2024/01/real.txt")
lines = puzzle.split("\n")
pattern = re.compile(r"(\d*)\s\s\s(\d*)")
left_list = [pattern.match(line).group(1) for line in lines]
right_list = [pattern.match(line).group(2) for line in lines]

total = 0
for id in left_list:
    number = int(id)
    matches = right_list.count(id)
    total += number * matches

print("total:", total)
