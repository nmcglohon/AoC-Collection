import sys
import math
from spiral import solvePartOne, getBottomRightValue

class GameBoard:
    def __init__(self, sideLen, inputVal):
        self.NodeArray = [x[:] for x in [[0] * sideLen] * sideLen]
        self.origin = (int(sideLen/2),int(sideLen/2))

        self.NodeArray[self.origin[0]][self.origin[1]] = 1
        self.numAllocated = 1
        self.lastAllocatedCoord = self.origin
        self.inputVal = inputVal

    def __str__(self):
        return(str(self.NodeArray))

    def __getNextCoords(self):
        pass

    def allocateNext(self):
        pass

    def findAnswer(self):
        pass

class Node:
    def __init__(self,x,y,init_dat):
        self.x = x
        self.y = y
        self.dat = init_dat

    def getNeighborsCoords(self):
        N = [(i,j) for i in range(self.x-1,self.x+2) for j in range(self.y-1,self.y+2) if not (i is self.x and j is self.y)]
        return N

def solvePartTwo(inputVal):
    bottomRightVal = getBottomRightValue(inputVal)
    lenOfSide = int(math.sqrt(bottomRightVal))

    theBoard = GameBoard(lenOfSide, inputVal)
    return theBoard.findAnswer()



def main():
    inputVal = 312051
    if len(sys.argv) > 1:
        inputVal = int(sys.argv[1])
    print("Part 1: " + str(solvePartOne(inputVal)))
    print("Part 2: " + str(solvePartTwo(inputVal)))


if __name__ == '__main__':
    main()