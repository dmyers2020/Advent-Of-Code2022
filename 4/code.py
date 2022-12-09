# Advent of code Year 2022 Day 4 solution
# Author = David Myers
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')




#input = [each.split(',') for each in input]
fully_contained = 0
overlap = 0

for each in input:
    #print(each)
    sections = each.split(',')
    section1 = sections[0].split('-')
    section2 = sections[1].split('-')
    #print(section1[0],section1[1])
    #print(section2[0],section2[1])
    '''
    if int(section1[0])>=int(section2[0]) and int(section1[1])<=int(section2[1]):
        fully_contained +=1
    elif int(section2[0])>=int(section1[0]) and int(section2[1])<=int(section1[1]):
        fully_contained +=1
'''
    
    if int(section1[0]) in range(int(section2[0]),int(section2[1])+1) or int(section1[1]) in range(int(section2[0]),int(section2[1])+1):
        overlap +=1
    elif int(section2[0]) in range(int(section1[0]),int(section1[1])+1) or int(section2[1]) in range(int(section1[0]),int(section1[1])+1):
        overlap +=1

print("Part One : "+ str(fully_contained))



print("Part Two : "+ str(overlap))