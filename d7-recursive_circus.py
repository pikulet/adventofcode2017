#d7-recursive_circus

from random import choice

d7 = open('d7-input.txt').read().split('\n')
nodes = {}

class Node():

    def __init__(self, name, weight, *children):
        self.name = name
        self.weight = weight
        self.children = list(map(lambda child_name: child_name.strip(','), children))
        self.children_weights = ()
        self.parent = None

    def get_children_weight(self):
        if not self.children_weights:       #a little optimisation achieved when reused later
            self.children_weights = tuple(map(lambda child: nodes[child].get_weight(), self.children))  
        return sum(self.children_weights)

    def get_weight(self):
        return self.weight + self.get_children_weight()

    def children_balanced(self):
        if self.children:
            return len(set(self.children_weights)) == 1
        return True
    
def process_data():
    #convert data to dict[name] = Node

    #add name, weight, children
    for node in d7:
        node = node.split(' ')
        node_name = node[0]
        node_weight = int(node[1].strip('()'))
        nodes[node_name] = Node(node_name, node_weight, *node[3:])
    
    #add parent, set children weight
    for node_name, node_info in nodes.items():
        
        try:
            for child_name in node_info.children:
                nodes[child_name].parent = node_name
        except IndexError:
            pass

process_data()

def find_root_parent():

    r = choice(list(nodes.values()))
    while r.parent:
        r = nodes[r.parent]

    return r.name

#advent_7a = find_root_parent()
#root_parent = nodes[advent_7a]
root_parent = nodes['ahnofa']               #already solved
    
def find_bad_child(node):

    #bad child must be among 3 or more children, else you cannot tell who is bad
    bad_weight = list(filter(lambda weight: node.children_weights.count(weight) == 1, node.children_weights))[0]
    bad_name = node.children[node.children_weights.index(bad_weight)]
    return nodes[bad_name]

def find_unbalanced_weight():

    r = root_parent
    r.get_weight()                          #self.children_weights is filled in for all nodes

    while True:
        for child_name in r.children:
            node = nodes[child_name]
            if not node.children_balanced():
                r = node
                has_unbalanced_child = True
                break
            has_unbalanced_child = False
        if not has_unbalanced_child:
            break
        
    bad_child = find_bad_child(r)
    r.children.remove(bad_child.name)
    actual_weight = nodes[r.children[0]].get_weight()
    
    return actual_weight - bad_child.get_children_weight()

advent_7b = find_unbalanced_weight()

#print (advent_7a, advent_7b)
