# Advent of code Year 2022 Day 5 solution
# Author = David Myers
# Date = December 2022
import re
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n\n')

stacks = input[0]
instrs = input[1]

rows = stacks.split('\n')
a,b,c,d,e,f,g,h,i = [],[],[],[],[],[],[],[],[]
list_of_lists = [a,b,c,d,e,f,g,h,i]
count_of_input = len(stacks)
width_of_input = len(rows[0])

start_pos = 1
list_num = 0
for listx in list_of_lists:
    for i in range(start_pos,count_of_input+1,width_of_input+1):
        listx.append(stacks[i])
    start_pos+=4
    listx.pop()
    listx.reverse()
    listx = [x for x in listx if x != ' ']
    list_of_lists[list_num] = listx
    list_num +=1
    #print(list_of_lists)

instrs = instrs.split('\n')
for instr in instrs:
    digits = re.findall(r'\d+',instr)
    digits = [int(each) for each in digits]
    #print(digits)
    multi_crate = []
    for n in range(digits[0]):
        multi_crate.append(list_of_lists[digits[1]-1].pop())
    multi_crate.reverse()
    #print(multi_crate,'\n')
    for letter in multi_crate:
        list_of_lists[digits[2]-1].append(letter)
    #for each in list_of_lists:
        #print(each)

answer = ''
for each in list_of_lists:
    answer += each[-1]

print("Part One : "+ str(answer))


print("Part Two : "+ str(None))
'''
something to keep track of the stacks.
pop and push onto those stacks 
something to track the instructions: 
instruction form: source, # in move, target
'''