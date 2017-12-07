#d2-corruption_checksum

from helpers import read_input
d2 = read_input('d2-input.txt')

from itertools import combinations

def row_difference(row):
    return max(row) - min(row)

def divisible(pair):
    return pair[0]%pair[1] == 0 or pair[1]%pair[0] == 0
    
def row_divide(row):
    k = list(tuple(filter(divisible, combinations(row, 2)))[0])
    k.sort()
    return k[1]//k[0]

def checksum(data, fn):
    return sum(map(lambda row: fn(row), data))

advent_2a = checksum(d2, row_difference)
advent_2b = checksum(d2, row_divide)

print (advent_2a, advent_2b)
