import sys
import math
from enum import Enum, auto

class Edge(Enum):
    BOTTOM = auto()
    LEFT = auto()
    TOP = auto()
    RIGHT = auto()
    CORNER = auto()

def getBottomRightValue(inputVal):
    sr = math.sqrt(inputVal)
    srOfBottomRight = 0
    floorSR = int(sr)
    if sr % 1 == 0 and sr%2 != 0:
        srOfBottomRight = floorSR #we already had the perfect odd square
    elif floorSR%2 is 0:
        srOfBottomRight = floorSR+1 #floorSR was even so we need to just move up one
    else:
        srOfBottomRight = floorSR+2 #floorSR was odd and we need an odd bigger than this one
    return int(srOfBottomRight**2)

def distToOriginPlaneFromEdge(inputVal):
    bottomRightVal = getBottomRightValue(inputVal)
    perfectOddSquares = [int(math.sqrt(i)) for i in range(bottomRightVal+1) if math.sqrt(i)%1 == 0 and math.sqrt(i)%2 != 0]
    return len(perfectOddSquares)-1


def solvePartOne(inputVal):
    bottomRightVal = getBottomRightValue(inputVal)
    lenOfSide = int(math.sqrt(bottomRightVal))
    # print(lenOfSide)

    bottomLeftVal = bottomRightVal - (lenOfSide-1)
    topLeftVal = bottomLeftVal - (lenOfSide-1)
    topRightVal = topLeftVal - (lenOfSide-1)

    # print(bottomRightVal, bottomLeftVal, topLeftVal, topRightVal)

    whichEdge = 0
    if inputVal > bottomLeftVal and inputVal < bottomRightVal:
        whichEdge = Edge.BOTTOM
    elif (inputVal > topLeftVal) and (inputVal < bottomLeftVal):
        whichEdge = Edge.LEFT
    elif (inputVal > topRightVal) and (inputVal < topLeftVal):
        whichEdge = Edge.TOP
    elif (inputVal < topRightVal):
        whichEdge = Edge.RIGHT
    else:
        whichEdge = Edge.CORNER
    # print(whichEdge)

    dist = 0
    if whichEdge is Edge.CORNER:
        dist = lenOfSide-1
    else:
        middleVal = 0
        if whichEdge is Edge.BOTTOM:
            middleVal = (bottomLeftVal + bottomRightVal)/2
        elif whichEdge is Edge.TOP:
            middleVal = (topLeftVal + topRightVal)/2

        elif whichEdge is Edge.LEFT:
            middleVal = (topLeftVal + bottomLeftVal)/2

        elif whichEdge is Edge.RIGHT:
            middleVal = (topRightVal - int(lenOfSide/2))

        distToMiddle = abs(inputVal-middleVal)
        # print("Dist To Middle of Edge: %d"%distToMiddle)
        # print("Dist To Origin Plane: %d"%distToOriginPlaneFromEdge(inputVal))
        dist = int(distToMiddle + distToOriginPlaneFromEdge(inputVal))

    return dist

def main():
    inputVal = 312051
    if len(sys.argv) > 1:
        inputVal = int(sys.argv[1])
    print("Part 1: " + str(solvePartOne(inputVal)))


if __name__ == '__main__':
    main()