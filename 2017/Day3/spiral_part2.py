import sys
import math
from enum import Enum
from spiral import solvePartOne, getBottomRightValue

class Direction(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

class GameBoard:
    def __init__(self, sideLen, inputVal):
        self.sideLen = sideLen
        self.NodeArray = [x[:] for x in [[0] * (sideLen)] * (sideLen)] #initialize one in either direction
        self.origin = (int(sideLen/2),int(sideLen/2))

        self.NodeArray[self.origin[0]][self.origin[1]] = 1
        self.numAllocated = 1
        self.lastAllocatedCoord = self.origin
        self.inputVal = inputVal
        self.direction = Direction.RIGHT

    def __str__(self):
        return "GameBoard: [%d x %d]; %d allocated; last allocated coord: %s; inputVal=%d"%(self.sideLen, self.sideLen, self.numAllocated, str(self.lastAllocatedCoord), self.inputVal)

    def printGrid(self):
        for row in reversed(self.NodeArray):
            print(row)

    def __getNextCoord(self):
        if self.lastAllocatedCoord == self.origin:
            return (self.origin[0]+1, self.origin[1])

        elif self.direction is Direction.RIGHT:
            if self.getNeighborValue(self.lastAllocatedCoord, Direction.UP) > 0:
                return (self.lastAllocatedCoord[0]+1,self.lastAllocatedCoord[1])
            else:
                self.direction = Direction.UP
                return (self.lastAllocatedCoord[0],self.lastAllocatedCoord[1]+1)

        elif self.direction is Direction.UP:
            if self.getNeighborValue(self.lastAllocatedCoord, Direction.LEFT) > 0:
                return (self.lastAllocatedCoord[0],self.lastAllocatedCoord[1]+1)
            else:
                self.direction = Direction.LEFT
                return (self.lastAllocatedCoord[0]-1,self.lastAllocatedCoord[1])

        elif self.direction is Direction.LEFT:
            if self.getNeighborValue(self.lastAllocatedCoord, Direction.DOWN) > 0:
                return (self.lastAllocatedCoord[0]-1,self.lastAllocatedCoord[1])
            else:
                self.direction = Direction.DOWN
                return (self.lastAllocatedCoord[0],self.lastAllocatedCoord[1]-1)

        elif self.direction is Direction.DOWN:
            if self.getNeighborValue(self.lastAllocatedCoord, Direction.RIGHT) > 0:
                return (self.lastAllocatedCoord[0],self.lastAllocatedCoord[1]-1)
            else:
                self.direction = Direction.RIGHT
                return (self.lastAllocatedCoord[0]+1,self.lastAllocatedCoord[1])

    def __getNextVal(self,nextCoord):
        N = self.getNeighborsCoords(nextCoord)

        totalSum = 0
        for coord in N:
            try:
                totalSum += self.NodeArray[coord[1]][coord[0]]
            except:
                pass
        return totalSum

    def getNeighborsCoords(self,coords):
        N = [(i,j) for i in range(coords[0]-1,coords[0]+2) for j in range(coords[1]-1,coords[1]+2) if not (i is coords[0] and j is coords[1])]
        return N

    def getNeighborValue(self,coord,direction):
        try:
            if direction == Direction.RIGHT:
                return self.NodeArray[coord[1]][coord[0]+1]
            if direction == Direction.UP:
                return self.NodeArray[coord[1]+1][coord[0]]
            if direction == Direction.LEFT:
                return self.NodeArray[coord[1]][coord[0]-1]
            if direction == Direction.DOWN:
                return self.NodeArray[coord[1]-1][coord[0]]
        except:
            return 0

    def __allocate(self,x,y,val):
        self.NodeArray[y][x] = val
        self.numAllocated += 1
        self.lastAllocatedCoord = (x,y)

    def allocateNext(self):
        nextCoord = self.__getNextCoord()
        val = self.__getNextVal(nextCoord)
        self.__allocate(nextCoord[0],nextCoord[1],val)
        return val
        
    def findAnswer(self):
        curVal = 0
        while curVal < self.inputVal:
            curVal = self.allocateNext()

        return curVal


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