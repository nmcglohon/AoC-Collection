
node_count = 0
root_node = None


class Node:
    def __init__(self):
        global node_count
        self.gid = node_count
        node_count+= 1
        self.metadata = []
        self.children = []
        
        print("New Node: %d"%self.gid)
    
    def add_metadata(self, dat):
        self.metadata.append(dat)
    
    def add_child(self, child_node):
        self.children.append(child_node)

    def sum_self_and_children(self):
        count = 0

        print("Node %d has %d children and %d metadata"%(self.gid,len(self.children),len(self.metadata)), end='')
        print(self.metadata)

        for md in self.metadata:
            count += md

        for child_node in self.children:
            count += child_node.sum_self_and_children()

        return count

    def get_self_value(self):
        count = 0

        if len(self.children) == 0:
            for md in self.metadata:
                count += md
            return count
        else:
            for child_reference in self.metadata:
                child_index = child_reference -1
                if child_index < len(self.children):
                    count += self.children[child_index].get_self_value()
            return count



def read_input(filename):
    with open(filename,'r') as f:
        text = f.readline()
        inputs = text.split(' ')
        inputs = list(map(int,inputs))

        parse_node(inputs, 0, None)

        

def parse_node(inputs, pos, parent):
    me_node = Node()
    if parent is None:
        global root_node
        root_node = me_node
    else:
        parent.add_child(me_node)

    if pos == None or pos >= len(inputs):
        return

    num_children = inputs[pos]
    num_metadata = inputs[pos+1]

    pos = pos+2

    for i in range(num_children):
        if pos == None or pos >= len(inputs):
            return

        pos = parse_node(inputs, pos, me_node)

    for i in range(num_metadata):
        me_node.add_metadata(inputs[pos])
        pos+=1

    return pos

def sum_metadata(root_node):
    count = root_node.sum_self_and_children()
    print("Part 1: The sum of all metadata is: %d"%count)

def get_true_value(root_node):
    count = root_node.get_self_value()
    print("Part 2: The sum of all true values is: %d"%count)
    

def main():
    read_input('day8-input.txt')
    sum_metadata(root_node)
    get_true_value(root_node)

if __name__ == "__main__":
    main()