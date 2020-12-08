with open('09-input', 'r') as f:
    data = f.read()

in_garbage = False
num_layers = 0
score = 0
num_garbage = 0

index = 0
while index < len(data):
    c = data[index]

    if c == '!':
        index += 2
    elif c == '>':
        in_garbage = False
        index += 1
    elif in_garbage:
        num_garbage += 1
        index += 1
    elif c == '<':
        in_garbage = True
        index += 1
    elif c == '{':
        num_layers += 1
        score += num_layers
        index += 1
    elif c == '}':
        num_layers -= 1
        index += 1
    else:
        index += 1

print('Part A:', score)
print('Part B:', num_garbage)
