# Advent of code Year 2022 Day 3 solution
# Author = David Myers
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')

import string
uppers = [letter for letter in (string.ascii_uppercase)]
lowers = [letter for letter in (string.ascii_lowercase)]
priorities = [int(i) for i in range(1,53)]

alpha_dict = dict(zip(lowers+uppers,priorities))
##print(alpha_dict)

pri_sum  = 0
for ruck in input:
##    print(ruck)
    mid = int(len(ruck)/2)
    comp1 = [letter for letter in ruck[:mid]]
    comp2 = [letter for letter in ruck[mid:]]
    for letter in comp1:
       if letter in comp2:
##           print(comp1)
##           print(comp2)
##           print(letter)
           pri_sum += alpha_dict[letter]
           break

print("Part One : "+ str(pri_sum))

##print(input)
pri2_sum = 0
for i in range(0,len(input),3):
    for letter in input[i]:
        if letter in input[i+1] and letter in input[i+2]:
##            print(letter)
            pri2_sum += alpha_dict[letter]
            break
    

print("Part Two : "+ str(pri2_sum))
