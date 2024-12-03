# https://adventofcode.com/2024/day/3
import input
import re

puzzle = input.read_puzzle_input("data/2024/03/real.txt")
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)")
instructions = pattern.findall(puzzle)

total = 0
is_enabled = True
pattern = re.compile(r"\d{1,3}")
for instruction in instructions:
    if instruction == "do()":
        is_enabled = True
        continue
    if instruction == "don't()":
        is_enabled = False
        continue

    if is_enabled:
        numbers = pattern.findall(instruction)
        total += int(numbers[0]) * int(numbers[1])

print("total:", total)
