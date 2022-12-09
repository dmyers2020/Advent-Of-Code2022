# Advent of code Year 2022 Day 2 solution
# Author = David Myers
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().split('\n')

input = [each.split(' ') for each in input]
#input = [['A', 'Y'],['B', 'X'],['C','Z']]

def lose(i):
    if i == 'A':
        return('Z')
    if i == 'B':
        return('X')
    else:
        return ('Y')

def draw(i):
    if i == 'A':
        return('X')
    if i == 'B':
        return('Y')
    else:
        return ('Z')

def win(i):
    if i == 'A':
        return('Y')
    if i == 'B':
        return('Z')
    else:
        return ('X')

for duel in input:
    if duel[1] == 'X': #goal is to lose
        duel[1] = lose(duel[0])
    elif duel[1] =='Y': #goal is to draw
        duel[1] = draw(duel[0])
    else: #goal is to win
        duel[1] = win(duel[0])

def rpc_selection(i):
    #takes in a single character string (i), outputs an int (selection_value)
    if i == 'X':
        selection_value = 1
    elif i == 'Y':
        selection_value = 2
    else: 
        selection_value = 3
        
    return (selection_value)

def rpc_result(i,j):
    if (i == 'A' and j == 'X') or (i =='B' and j =='Y') or (i == 'C' and j == 'Z'):
        return(3) #draw
    elif (i == 'A' and j == 'Y') or (i =='B' and j =='Z') or (i == 'C' and j == 'X'):
        return(6) #loss
    else:
        return(0) #win

expected_score = 0

for duel in input:
    expected_score += rpc_selection(duel[1])
    expected_score += rpc_result(duel[0],duel[1])
    
    #print(duel[0],duel[1])
print(expected_score)
