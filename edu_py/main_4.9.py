from collections import deque

def brackets(line):
    if  line == '':
        return True
    if line[0] == ')':
        return False
    count = 0
    for i in line:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    
    return [False, True][count == 0]


