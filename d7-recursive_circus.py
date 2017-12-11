#d7-recursive_circus

from random import choice

d7 = open('d7-input.txt').read().split('\n')
nodes = {}

class Node():

    def __init__(self, name, weight, *children):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None

    def get_weight(self):
        return self.weight + sum(map(lambda child: nodes[child].get_weight(), self.children))

def process_data():

    #add name, weight, children
    for node in d7:
        node = node.split(' ')
        node_name = node[0]
        node_weight = int(node[1].strip('()'))
        nodes[node_name] = Node(node_name, node_weight, *node[3:])
    
    #add parent
    for node_name, node_info in nodes.items():
        try:
            for child_name in node_info.children:
                nodes[child_name.strip(',')].parent = node_name
        except IndexError:
            pass

process_data()

def find_root_parent():

    r = choice(list(nodes.values()))
    while r.parent:
        r = nodes[r.parent]

    return r.name

advent_7a = find_root_parent()          
            


