#d8-registers

d8 = open('d8-input.txt').read().split('\n')

do = {
    'inc':  lambda x, y: values[x]+y,
    'dec':  lambda x, y: values[x]-y
    }

conditional = {
    '==':   lambda x, y: values[x] == y,
    '!=':   lambda x, y: values[x] != y,
    '>':    lambda x, y: values[x] > y,
    '>=':   lambda x, y: values[x] >= y,
    '<':    lambda x, y: values[x] < y,
    '<=':   lambda x, y: values[x] <= y
    }

instructions = []

for instruction in d8:
    i = instruction.split(' ')
    i = (   (do[i[1]], i[0], int(i[2])), (conditional[i[5]], i[4], int(i[6]))  )
    instructions.append(i)

registers = set(map(lambda i: i[0][1], instructions))

values = {}
for r in registers:
    values[r] = 0

def check_conditional(cond):
    return cond[0](cond[1], cond[2])

max_val = 0
def update(val):
    global max_val
    max_val = max(max_val, val)

def do_action(action):
    to_change = action[1]
    values[to_change] = action[0](to_change, action[2])
    update(max(values.values()))
    
for instruction in instructions:
    if check_conditional(instruction[1]):
        do_action(instruction[0])      

advent_8a = max(values.values())
advent_8b = max_val

print (advent_8a, advent_8b)
