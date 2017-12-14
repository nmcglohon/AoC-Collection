from collections import OrderedDict


class Tree:
    def __init__(self,NodeDict=OrderedDict()):
        self.NodeDict = NodeDict

    def __contains__(self, item):
        return item in self.NodeDict.keys()

    def __str__(self):
        myStr = ""
        for node in self.NodeDict:
            myStr += str(self.NodeDict[node]) + '\n'
        return myStr

    def add(self,node):
        if node.name not in self.NodeDict:
            print("Adding %s"%(str(node)))
            self.NodeDict[node.name] = node

        if self.NodeDict[node.name].weight is -1 and node.weight is not -1:
            print("Updating %s"%(str(node)))
            self.NodeDict[node.name].weight = node.weight
            self.NodeDict[node.name].children = node.children

    def get(self,key):
        return self.NodeDict[key]

class Node:
    def __init__(self, name, weight=-1, children=[]):
        self.name = name
        self.weight = weight
        self.children = children

    def __hash__(self):
        return self.name.__hash__()

    def __str__(self):
        if len(self.children) > 0:
            myStr = "%s (%d) -> "%(self.name, self.weight)
            for child in self.children:
                myStr += child.getName() + " "
        else:
            myStr = "%s (%d)"%(self.name,self.weight)

        return myStr

    def getName(self):
        return self.name

def parseLine(lineString, progTree):
    lineString = lineString.strip()

    name = lineString.split()[0]

    weight = lineString.split('(')[1]
    weight = weight.split(')')[0]
    weight = int(weight)

    if '->' in lineString: #there are children
        children = lineString.split('-> ')[1]
        childrenList = children.split(',')
        childrenNodeList = []
        for child in childrenList:
            child = child.strip()
            if child in progTree:
                childrenNodeList.append(progTree.get(child))
            else:
                progTree.add(Node(child))
                childrenNodeList.append(progTree.get(child))

        progTree.add(Node(name,weight,childrenNodeList))

    else: #no children
        progTree.add(Node(name,weight))

def parseInput(inFilename):
    progTree = Tree()
    with open(inFilename) as f:
        for line in f:
            parseLine(line,progTree)

    return progTree

def solvePartOne(progTree):
    pass

def solvePartTwo(progTree):
    pass

def main():
    progTree = parseInput('input.txt')
    print("Part 1: " + str(solvePartOne(progTree)))
    print("Part 2: " + str(solvePartTwo(progTree)))

if __name__ == '__main__':
    main()