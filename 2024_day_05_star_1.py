# https://adventofcode.com/2024/day/5
import input

debug = False
day = "05"
year = "2024"
filename = f"data/{year}/{day}/{'example' if debug else 'real'}.txt"
puzzle = input.read_puzzle_input(filename)

rules_section, updates_section = puzzle.split("\n\n")
rules = [
    {
        "a": int(rule.split("|")[0]),
        "b": int(rule.split("|")[1]),
    }
    for rule in rules_section.split("\n")
]
updates = [list(map(int, update.split(","))) for update in updates_section.split("\n")]

grouped_rules = {}
while rules:
    rule = rules.pop(0)
    a = rule["a"]
    grouped_rules[a] = [rule["b"]]
    for i in range(len(rules) - 1, -1, -1):
        if rule["a"] == rules[i]["a"]:
            other_rule = rules.pop(i)
            grouped_rules[a].append(other_rule["b"])

total = 0
for update in updates:
    valid = True
    for i in range(len(update)):
        page = update[i]
        should_be_after = grouped_rules.get(page, [])
        after = update[i + 1 :]
        if not all([after_page in should_be_after for after_page in after]):
            valid = False
            break

    if valid:
        middle = len(update) // 2
        total += update[middle]

print("total:", total)
