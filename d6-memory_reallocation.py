#d6-memory_reallocation

from numpy import loadtxt
d6 = list(loadtxt('d6-input.txt', dtype = int))
n_parts = len(d6)

repeated = {}

def update(lst):
    max_index = lst.index(max(lst))
    n_blocks = lst[max_index]
    fair_amt = n_blocks//n_parts
    left_amt = n_blocks%n_parts
    lst[max_index] = 0
    for i in range(left_amt):
        lst[max_index-n_parts+i+1] += fair_amt + 1
    for i in range(n_parts - left_amt):
        lst[max_index-i] += fair_amt
    return lst

count = 0
while tuple(d6) not in repeated:
    repeated[tuple(d6)] = count
    count += 1
    d6 = update(d6)

advent_6a = count
advent_6b = count - repeated[tuple(d6)]

print(advent_6a, advent_6b)

