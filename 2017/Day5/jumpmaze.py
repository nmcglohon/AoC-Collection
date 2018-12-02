






def getInputLines(filename):
    inputList = []
    with open(filename) as f:
        for line in f:
            inputList.append(int(line))
    return inputList

def solvePartOne(inputInstructions):
    stepCount = 0
    curIndex = 0
    while curIndex < len(inputInstructions):
        thisJump = inputInstructions[curIndex]
        inputInstructions[curIndex] += 1
        curIndex = curIndex + thisJump
        stepCount += 1

    return stepCount


def solvePartTwo(inputInstructions):
    stepCount = 0
    curIndex = 0
    while curIndex < len(inputInstructions):
        thisJump = inputInstructions[curIndex]
        if(thisJump >= 3):
            inputInstructions[curIndex] -= 1
        else:
            inputInstructions[curIndex] += 1
        curIndex = curIndex + thisJump
        stepCount += 1

    return stepCount

def main():
    instructions = getInputLines('input.txt')
    print("Part 1: " + str(solvePartOne(instructions.copy())))
    print("Part 2: " + str(solvePartTwo(instructions.copy())))

if __name__ == '__main__':
    main()