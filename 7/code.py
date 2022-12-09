# Advent of code Year 2022 Day 7 solution
# Author = David Myers
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')

input = [cmd.split() for cmd in input]

from collections import defaultdict

path = []
size_dict = defaultdict(int)
for cmd in input:
    if cmd[1] == 'cd':
        if cmd[-1] =='..':
            path.pop()
        else:
            path.append(cmd[-1])
    elif cmd[1] =='ls' or cmd[0] =='dir':
        continue
    else:
        size = int(cmd[0])
        for i in range(1,len(path)+1):
            size_dict['/'.join(path[:i])] += size

print(size_dict)


answer = 0
for each in size_dict.values():
    if each<=100000:
        answer +=each
print("Part One : "+ str(answer))

#part 2

disk_space = 70000000
required = 30000000
unused = disk_space - size_dict['/']
need_to_remove = required-unused

candidates = []
for i in size_dict.keys():
    print(i)
    if size_dict[i] >=need_to_remove:
        candidates.append(size_dict[i])

print(candidates)

print("Part Two : "+ str(min(candidates)))


#goal is to find sum of dir sizes where dir size < 100000
# files CAN be counted more than once


# import re

# cmd_cd = re.compile(r'[$].[c].*')
# cmd_ls = re.compile(r'[$].[l].*')
# result_file = re.compile(r'\d+')
# result_dir = re.compile(r'(dir).\w')
'''
find size of each dir 
establish parentage of dirs
if dir_size less than <100000, sum+=
'''
# matches = cmd_ls.finditer(input)