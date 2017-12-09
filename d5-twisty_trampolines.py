#d5-twisty_trampolines

from numpy import loadtxt
d5 = list(loadtxt('d5-input.txt', dtype = int))
within = range(len(d5))

d5_a = d5.copy()
d5_b = d5.copy()

def update(lst, index, n):
    lst[index] += n
    return lst[index] - n

def count_jumps_5a():
    index = 0
    count = 0
    while index in within:
        count += 1
        index += update(d5_a, index, 1)
    return count

def count_jumps_5b():
    index = 0
    count = 0
    while index in within:
        count += 1
        offset = d5_b[index]
        if offset >= 3:
            index += update(d5_b, index, -1)
        else:
            index += update(d5_b, index, 1)
    return count

#takes a very long time to run
#advent_5a = count_jumps_5a()
advent_5b = count_jumps_5b()
#print(advent_5a, advent_5b)

        


    

