# Advent of code Year 2022 Day 1 solution
# Author = David Myers
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
input = input.split('\n\n')
per_elf = [each.split('\n') for each in input]

leader = [0]
for elf in per_elf:
    elf_calories = 0
    for calories in elf:
        elf_calories += int(calories)
    leader.append(elf_calories)

leader.sort(reverse=True)
print(sum(leader[0:3]))
