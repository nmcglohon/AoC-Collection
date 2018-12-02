from collections import OrderedDict


class Tree:
    def __init__(self,NodeDict=OrderedDict()):
        self.NodeDict = NodeDict
        self.root = None
        self.totalLevels = 0

    def __contains__(self, item):
        return item in self.NodeDict.keys()

    def __iter__(self):
        return self.NodeDict.values().__iter__()

    def __next__(self):
        return self.NodeDict.values().__next__()

    def __str__(self):
        myStr = ""
        for node in self.NodeDict:
            myStr += str(self.NodeDict[node]) + '\n'
        return myStr

    def add(self,node):
        if node.name not in self.NodeDict:
            # print("Adding %s"%(str(node)))
            self.NodeDict[node.name] = node

        if self.NodeDict[node.name].weight is -1 and node.weight is not -1:
            # print("Updating %s"%(str(node)))
            self.NodeDict[node.name].weight = node.weight
            self.NodeDict[node.name].children = node.children

    def get(self,key):
        return self.NodeDict[key]

    def calculateRoot(self):
        maxNodeLevels = 0
        maxNode = None
        for node in self:
            levels = node.getLevelsBelow()
            if levels > maxNodeLevels:
                maxNodeLevels = levels
                maxNode = node
        self.root = maxNode
        self.totalLevels = maxNodeLevels

    def getRoot(self):
        return self.root

    def getRootLevels(self):
        return self.totalLevels

    def getCorrectedWeight(self,eroot):
        if len(eroot.children) > 0:
            childWeights = []
            for child in eroot.children:
                childWeights.append(child.getTotalWeight())

            modeWeight = max(set(childWeights), key=childWeights.count)
            incorrectChildIndex = -1
            for i,weight in enumerate(childWeights):
                if weight is not modeWeight:
                    #this is the incorrect weight!
                    incorrectChildIndex = i
                    break

            if incorrectChildIndex is -1:
                #all children are balanced, eroot is the problem program
                return -1

            ret = self.getCorrectedWeight(eroot.children[incorrectChildIndex])
            if ret is 0: #child was leaf
                return modeWeight
            elif ret is -1:
                #incorrect child index is the problem child, its weight needs to be changed so that its total weight is equal to mode weight
                incorrectChildTotalWeight = eroot.children[incorrectChildIndex].getTotalWeight()
                changeToChildWeight = modeWeight - incorrectChildTotalWeight
                return eroot.children[incorrectChildIndex].weight + changeToChildWeight
            else:
                return ret

        else:
            return 0

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

    def getLevelsBelow(self):
        if len(self.children) > 0: #am parent
            maxFoundBelow = 0
            for child in self.children:
                childLevels = child.getLevelsBelow()
                if childLevels > maxFoundBelow:
                    maxFoundBelow = childLevels
            return maxFoundBelow+1
        else: #am leaf
            return 0

    def getTotalWeight(self):
        sumBelow = 0
        if len(self.children) > 0:
            for child in self.children:
                sumBelow += child.getTotalWeight()
        return self.weight + sumBelow


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
    progTree.calculateRoot()
    return "%s with %s levels"%(progTree.getRoot().name,progTree.getRootLevels())

def solvePartTwo(progTree):
    progTree.calculateRoot()
    return progTree.getCorrectedWeight(progTree.getRoot())


def main():
    progTree = parseInput('input.txt')
    print("Part 1: " + str(solvePartOne(progTree)))
    print("Part 2: " + str(solvePartTwo(progTree)))

if __name__ == '__main__':
    main()