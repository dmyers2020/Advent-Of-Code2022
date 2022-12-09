# Advent of code Year 2022 Day 8 solution
# Author = David Myers
# Date = December 2022

with open((__file__.rstrip("code.py")+"sample_input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')

wide = len(input[0])
tall = len(input)
perimiter = 2*wide +2*(tall-2)

answer = perimiter

for col in range(1,wide-1):
    for row in range(1,tall-1):
        cur_tree =input[col][row]

'''
I need to think a lot more about this before jumping in.
'''



print("Part One : "+ str(None))



print("Part Two : "+ str(None))