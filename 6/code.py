# Advent of code Year 2022 Day 6 solution
# Author = David Myers
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

import re
test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz' #5
test2 = 'nppdvjthqldpwncqszvftbrmjlhg' #6
test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' #10
test4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' #11
part1_tests = [test1, test2, test3, test4]
#part two
test5 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
test6 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test7 = 'nppdvjthqldpwncqszvftbrmjlhg'
test8 ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test9 ='zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
part2_tests = [test5,test6,test7,test8,test9,input]

for test in part2_tests:   
    i = 0
    while True:
        s = test[i:(i+14)]
        if len(set(list(s))) ==14:
            print(i+14)
            break
        i +=1

print("Part One : "+ str(None))



print("Part Two : "+ str(None))