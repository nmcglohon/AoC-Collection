import numpy as np


def getInputArray(filename):
    inputString = ''
    with open(filename) as f:
        inputString = f.readline()
    inputString = inputString.strip()

    inputArray = np.zeros(len(inputString))
    for i,char in enumerate(inputString):
        if(char != '\n'):
            inputArray[i] = int(char)

    return inputArray

def solvePartOne(inputArray):
    inputArray = np.append(inputArray, inputArray[0])
    totalSum = 0
    lastItem = -1
    for item in inputArray:
        if item == lastItem:
            totalSum += item
        lastItem = item
    return totalSum


def solvePartTwo(inputArray):
    stepsAhead = int(len(inputArray)/2)
    totalSum = 0
    for i,item in enumerate(inputArray):
        otherItem = inputArray[(i+stepsAhead)%len(inputArray)]
        if item == otherItem:
            totalSum += item
    return totalSum


def main():
    inputArray = getInputArray('input.txt')
    print("Part 1: %d"%solvePartOne(inputArray.copy()))
    print("Part 2: %d"%solvePartTwo(inputArray.copy()))


if __name__ == '__main__':
    main()