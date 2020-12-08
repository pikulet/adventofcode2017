from numpy import loadtxt

data_a = list(loadtxt('05-input', dtype = int))
data_b = data_a.copy()

def update_rule_a(num):
    return 1

def update_rule_b(num):
    if num >= 3:
        return -1
    else:
        return 1

def count_jumps(update_rule, data_arr):
    index = 0
    num_jumps = 0

    while 0 <= index and index < len(data_arr):
        step_size = data_arr[index]
        data_arr[index] += update_rule(data_arr[index])
        index += step_size
        num_jumps += 1

    return num_jumps

print('Part A:', count_jumps(update_rule_a, data_a)) 
print('Part B:', count_jumps(update_rule_b, data_b)) 
