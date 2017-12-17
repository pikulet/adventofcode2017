#d3-spiral_memory

from math import sqrt

d3 = 289326

###########
# HELPERS #
###########

def find_spiral(n):
    #returns odd number, which is the spiral reference (bottom right)
    r = sqrt(n)
    while r%2 != 1:    
        r = int(r) + 1
    return int(r)

def square(x):
    return x**2

def find_trail(n, spiral):
    #index of n in the spiral
    return int(n - square(spiral-2) - 1)

def find_index(n, spiral):
    #manhanttan dist repeats on each side
    #returns a value in range(spiral-1)
    if spiral > 1:
        return find_trail(n, spiral)%(spiral-1)
    else:
        return 0

def find_round(spiral):
    return (spiral+1)//2

def generate_pattern(spiral):
    r = find_round(spiral) -1

    down_list = list(map(lambda x: x+r, range(r)))
    up_list = down_list.copy()
    up_list = list(map(lambda x: x+1, up_list))
    down_list.reverse()

    return down_list + up_list

def find_direction(n, spiral):
    #0 = right, 1 = top, 2 = left, 3 = bottom
    if spiral > 1:
        return find_trail(n, spiral)//(spiral-1)
    else:
        return 0

##############
# INCOMPLETE #
##############

def find_summands(n):
    spiral = find_spiral(n)
    index = find_index(n, spiral)
    direction = find_direction(n, spiral)

    sums = [n-1] #add previous square
    difference = 8*(find_round(spiral)-1)-2*(4-direction)+1

    if index == 0:
        if direction == 0:
            sums.append(square(spiral-4)+1)
            return sums
        elif direction > 0:
            #second corner tile
            sums.append(n-2)

    if index == (spiral-2) and direction < 3:
        #corner tile
        difference += 1
        sums.append(n-difference)
        return sums

    sums.append(n-difference)
    if index < (spiral-3):
        sums.append(n-difference+1) 
    if index > 0:
        if index == 1 and direction == 0:
            sums.append(square(spiral-2))
        else:
            sums.append(n-difference-1)

    if direction == 3 and index == (spiral-3):
        sums.append(square(spiral-2)+1)

    return sums
    

########
# MAIN #
########

def manhattan_dist(n):
    spiral = find_spiral(n)
    index = find_index(n, spiral)
    pattern = generate_pattern(spiral)
    return pattern[index]
            
def find_sum_more_than(n):
    to_add = 0
    i = 3
    spiral_sum = {1:1, 2:1}  #base case
    
    while to_add <= n:
        to_add = sum(map(lambda x: spiral_sum[x], find_summands(i)))
        spiral_sum[i] = to_add
        i+=1

    return to_add

advent_3a = manhattan_dist(d3)
advent_3b = find_sum_more_than(d3)

print(advent_3a, advent_3b)
