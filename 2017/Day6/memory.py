import collections


def redistribute(states):
    maxval, maxi = getMaxAndIndex(states)
    # print("Box %d is Max (%d)"%(maxi, maxval))
    numBanks = len(states)

    blocksToDistribute = maxval

    states[maxi] = 0
    steps = 0
    index = maxi+1
    while blocksToDistribute > 0:
        states[(index+steps)%numBanks] += 1
        blocksToDistribute -= 1
        steps+=1
    return states


def getMaxAndIndex(L):
    maxVal = float('-inf')
    maxPos = 0
    for i,item in enumerate(L):
        if item > maxVal:
            maxVal = item
            maxPos = i
    return (maxVal, maxPos)

def getInputState(filename):
    inputList = []
    with open(filename) as f:
        statesString = f.readline()
        statesString = statesString.strip()
        inputList = statesString.split('\t')
        inputList = list(map(int,inputList))
    return inputList

def findRepeated(bankStates):
    seenConfigs = collections.OrderedDict()
    seenConfigs[tuple(bankStates)] = 1
    # print(bankStates)

    cycleCount = 0
    foundRepeated = False
    while not foundRepeated:
        bankStates = redistribute(bankStates)
        # print(bankStates)
        cycleCount += 1
        if tuple(bankStates) not in seenConfigs:
            seenConfigs[tuple(bankStates)] = 1
        else:
            seenConfigs[tuple(bankStates)] += 1
            foundRepeated = True
    return cycleCount, seenConfigs

def solvePartOne(bankStates):
    cycleCount, seenConfigs = findRepeated(bankStates)
    return cycleCount

def solvePartTwo(bankStates):
    cycleCount, seenConfigs = findRepeated(bankStates)

    repeatedState = max(seenConfigs, key=seenConfigs.get)
    start = [i for i,x in enumerate(seenConfigs) if x == repeatedState]
    return (len(seenConfigs)-start[0])

def main():
    bankStates = getInputState('input.txt')
    print("Part 1: " + str(solvePartOne(bankStates.copy())))
    print("Part 2: " + str(solvePartTwo(bankStates.copy())))

if __name__ == '__main__':
    main()