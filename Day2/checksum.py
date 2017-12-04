import numpy as np


def getInputLines(filename):
    inputList = []
    with open(filename) as f:
        for line in f:
            inputLine = line.strip().split('\t')
            inputLine = list(map(int,inputLine))
            inputList.append(inputLine)
    return inputList

def solvePartOne(inputArray):
    totalSum = 0
    for row in inputArray:
        totalSum += max(row) - min(row)
    return totalSum

def solvePartTwo(inputArray):
    pass



def main():
    inputArray = getInputLines('input.txt')
    print("Part 1: " + str(solvePartOne(inputArray.copy())))
    print("Part 2: " + str(solvePartTwo(inputArray.copy())))


if __name__ == '__main__':
    main()