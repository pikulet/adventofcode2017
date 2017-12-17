#d11-hex_ed

d11 = open('d11-input.txt').read().split(',')
moves = {}

def count_moves(d):
    n = d.count('n')
    s = d.count('s')
    if n > s:
        moves['n'] = n-s
    else:
        moves['s'] = s-n

    ne = d.count('ne')
    sw = d.count('sw')
    if ne > sw:
        moves['ne'] = ne-sw
    else:
        moves['sw'] = sw-ne

    nw = d.count('nw')
    se = d.count('se')
    if nw > se:
        moves['nw'] = nw-se
    else:
        moves['se'] = se-nw

count_moves(d11)
#moves will only have 3 elements
#ne + s = se

def reduce_moves(a, b, c):
    moves[c] += moves[b]
    moves[a] -= moves[b]
    del moves[b]

reduce_moves('s','ne','se')

def total_moves():
    return sum(moves.values())

advent11a = total_moves()
    
